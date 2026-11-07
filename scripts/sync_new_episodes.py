#!/usr/bin/env python3
"""
sync_new_episodes.py
====================
Automation script that:
  1. Fetches the YouTube playlist page and extracts video IDs/titles
  2. Compares against the saved metadata/course_metadata.json
  3. For any NEW episodes found:
     a. Fetches full video details (title, description, duration, data links)
     b. Creates the episode folder under the correct module
     c. Downloads any dataset files linked in the description
     d. Generates a README.md for the new episode
     e. Appends a row to the master README.md table
     f. Appends a row to PROGRESS_TRACKER.md
     g. Appends a row to the module README.md
     h. Commits and pushes to GitHub

Usage:
    python scripts/sync_new_episodes.py            # check and sync
    python scripts/sync_new_episodes.py --dry-run  # check only, no changes

Automation:
    Can be run automatically via:
    - GitHub Actions (.github/workflows/sync_playlist.yml)
    - Windows Task Scheduler (scripts/run_sync.bat)
    - Cron job (Linux / macOS)
"""

import json
import re
import os
import sys
import time
import argparse
import subprocess
import urllib.request
import urllib.parse
import urllib.error
from pathlib import Path
from datetime import datetime

# ── Configuration ─────────────────────────────────────────────────────────────
REPO_ROOT     = Path(__file__).parent.parent.resolve()
METADATA_FILE = REPO_ROOT / "metadata" / "course_metadata.json"
README_FILE   = REPO_ROOT / "README.md"
PROGRESS_FILE = REPO_ROOT / "PROGRESS_TRACKER.md"
PLAYLIST_ID   = "PLkYJ59mAhUsMbZQ4AmBmGt0EEyrTrg5mX"
PLAYLIST_URL  = f"https://www.youtube.com/playlist?list={PLAYLIST_ID}"

# Module boundaries (ep_start inclusive, ep_end inclusive, name, folder_name)
MODULES = [
    (1,  2,   "Data Foundations",                "01-Data-Foundations"),
    (3,  14,  "Data Acquisition",                "02-Data-Acquisition"),
    (15, 23,  "Advanced Data Extraction",        "03-Advanced-Data-Extraction"),
    (24, 31,  "Governance and Automation",       "04-Governance-and-Automation"),
    (32, 47,  "Data Transformation",             "05-Data-Transformation"),
    (48, 64,  "Case Studies",                    "06-Case-Studies"),
    (65, 999, "Power Query Engine and M Language","07-Power-Query-Engine-and-M-Language"),
]

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def http_get(url: str, extra_headers: dict = None) -> str:
    """Simple HTTP GET returning the response body as text."""
    req = urllib.request.Request(url, headers=HEADERS)
    if extra_headers:
        for k, v in extra_headers.items():
            req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def http_post_json(url: str, payload: dict) -> dict:
    """Simple HTTP POST with JSON body, returns parsed JSON."""
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={
        **HEADERS,
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8", errors="replace"))


def clean_title(raw: str) -> str:
    """
    Clean YouTube video title:
      - Strip trailing '| Ep. X | Course Name'
      - Replace '|' with safe separators to avoid breaking markdown tables
    """
    t = raw.strip()
    # Strip typical diploma suffixes
    t = re.sub(r'\s*\|\s*Ep\.?\s*\d+.*$', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\s*\|\s*Case Study.*$', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\s*\|\s*Microsoft Power BI.*$', '', t, flags=re.IGNORECASE)
    
    # Specific known multi-pipe phrases
    t = t.replace("SQL | Oracle | SAP", "SQL / Oracle / SAP")
    t = t.replace("دبلومة تحليل البيانات | المحاضرة (١) | مقدمة", "دبلومة تحليل البيانات - المحاضرة (١) - مقدمة")
    t = t.replace("دبلومة تحليل البيانات | المحاضرة (1) | مقدمة", "دبلومة تحليل البيانات - المحاضرة (1) - مقدمة")

    # If any literal '|' remains, replace with '/' to never corrupt Markdown tables
    t = t.replace('|', '/')
    return t.strip(' -/').strip()


def slugify(text: str) -> str:
    """Convert a title to a filesystem-safe slug."""
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')[:50]


def format_duration(seconds: int) -> str:
    """Format seconds to 'Xh Ym Zs' or 'Ym Zs'."""
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    if h:
        return f"{h}h {m}m {s}s"
    return f"{m}m {s}s"


def get_module(ep_num: int):
    for start, end, name, folder in MODULES:
        if start <= ep_num <= end:
            return name, folder
    return MODULES[-1][2], MODULES[-1][3]


def extract_data_links(description: str) -> list:
    """Extract Google Sheets / Drive / Docs links from description."""
    patterns = [
        r'https://docs\.google\.com/spreadsheets/[^\s\)\"\']+',
        r'https://drive\.google\.com/(?:file/d|drive/folders)/[^\s\)\"\']+',
        r'https://docs\.google\.com/(?:document|presentation)/[^\s\)\"\']+',
    ]
    links = []
    for p in patterns:
        links.extend(re.findall(p, description))
    seen = set()
    return [l for l in links if not (l in seen or seen.add(l))]


def download_file(url: str, dest_path: Path) -> bool:
    """Download a Google Sheets/Drive file as xlsx. Returns True on success."""
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    if dest_path.exists():
        print(f"    Already exists: {dest_path.name}")
        return True

    # Google Sheets → export as xlsx
    if "docs.google.com/spreadsheets" in url:
        file_id_m = re.search(r'/spreadsheets/d/([^/]+)', url)
        if file_id_m:
            file_id = file_id_m.group(1)
            dl_url = f"https://docs.google.com/spreadsheets/d/{file_id}/export?format=xlsx"
            try:
                req = urllib.request.Request(dl_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=60) as resp:
                    data = resp.read()
                    if len(data) > 500:
                        dest_path.write_bytes(data)
                        print(f"    Downloaded (Sheets): {dest_path.name} ({len(data):,} bytes)")
                        return True
            except Exception as e:
                print(f"    WARN: Could not download {dl_url}: {e}")
                return False

    # Google Drive file → direct download
    if "drive.google.com/file/d" in url:
        file_id_m = re.search(r'/file/d/([^/]+)', url)
        if file_id_m:
            file_id = file_id_m.group(1)
            dl_url = f"https://drive.usercontent.google.com/download?id={file_id}&export=download&confirm=t"
            try:
                req = urllib.request.Request(dl_url, headers=HEADERS)
                with urllib.request.urlopen(req, timeout=60) as resp:
                    data = resp.read()
                    if len(data) > 500:
                        dest_path.write_bytes(data)
                        print(f"    Downloaded (Drive): {dest_path.name} ({len(data):,} bytes)")
                        return True
            except Exception as e:
                print(f"    WARN: Could not download {dl_url}: {e}")
                return False

    # Google Drive folder → create a bookmark shortcut file
    if "drive.google.com/drive/folders" in url:
        shortcut_file = dest_path.parent / f"{dest_path.stem}_GoogleDriveFolder.url"
        content = f"[InternetShortcut]\nURL={url}\n"
        shortcut_file.write_text(content, encoding="utf-8")
        print(f"    Created Google Drive folder link shortcut: {shortcut_file.name}")
        return True

    print(f"    SKIP: Unsupported link type: {url}")
    return False


# ── YouTube Playlist Fetching ─────────────────────────────────────────────────

def _extract_from_item(item: dict) -> tuple[str, str]:
    """Helper to extract (videoId, title) from either lockupViewModel or playlistVideoRenderer."""
    if "lockupViewModel" in item:
        lv = item["lockupViewModel"]
        cmd = (lv.get("rendererContext", {})
                 .get("commandContext", {})
                 .get("onTap", {})
                 .get("innertubeCommand", {})
                 .get("watchEndpoint", {}))
        vid_id = cmd.get("videoId")
        title = (lv.get("metadata", {})
                   .get("lockupMetadataViewModel", {})
                   .get("title", {})
                   .get("content", ""))
        return vid_id, title
    elif "playlistVideoRenderer" in item:
        pvr = item["playlistVideoRenderer"]
        vid_id = pvr.get("videoId")
        title = pvr.get("title", {}).get("runs", [{}])[0].get("text", "")
        return vid_id, title
    return None, None


def fetch_playlist_video_ids() -> list[dict]:
    """
    Fetch all video IDs and titles from the YouTube playlist page.
    Handles both modern lockupViewModel and classic playlistVideoRenderer layouts.
    """
    print(f"Fetching playlist: {PLAYLIST_URL}")
    html = http_get(PLAYLIST_URL)

    m = re.search(r'var ytInitialData\s*=\s*(\{.+?\});</script>', html, re.DOTALL)
    if not m:
        m = re.search(r'ytInitialData\s*=\s*(\{.+?\})(?:;|</script>)', html, re.DOTALL)
    if not m:
        raise RuntimeError("Could not extract ytInitialData from playlist page")

    data = json.loads(m.group(1))
    videos = []
    seen_ids = set()

    try:
        tabs = data.get("contents", {}).get("twoColumnBrowseResultsRenderer", {}).get("tabs", [])
        for tab in tabs:
            tab_content = tab.get("tabRenderer", {}).get("content", {})
            section_list = tab_content.get("sectionListRenderer", {})
            for section in section_list.get("contents", []):
                item_section = section.get("itemSectionRenderer", {})
                for content in item_section.get("contents", []):
                    items_to_check = [content]
                    if "playlistVideoListRenderer" in content:
                        items_to_check = content["playlistVideoListRenderer"].get("contents", [])
                    
                    for it in items_to_check:
                        vid_id, title = _extract_from_item(it)
                        if vid_id and vid_id not in seen_ids:
                            seen_ids.add(vid_id)
                            videos.append({
                                "index": len(videos) + 1,
                                "videoId": vid_id,
                                "title": title,
                            })

                civm = section.get("continuationItemViewModel")
                if civm:
                    token = (civm.get("continuationCommand", {})
                                 .get("continuationCommand", {})
                                 .get("token"))
                    if token:
                        more = fetch_continuation_videos(token, seen_ids)
                        for item in more:
                            item["index"] = len(videos) + 1
                            videos.append(item)
    except Exception as e:
        print(f"  Warn: primary parse error ({e})")

    if not videos:
        print("  Warn: attempting regex fallback for video IDs...")
        for m2 in re.finditer(r'"videoId"\s*:\s*"([A-Za-z0-9_-]{11})"', html):
            vid = m2.group(1)
            if vid not in seen_ids:
                seen_ids.add(vid)
                videos.append({
                    "index": len(videos) + 1,
                    "videoId": vid,
                    "title": f"Episode {len(videos) + 1}"
                })

    print(f"  Successfully extracted {len(videos)} videos from playlist.")
    return videos


def fetch_continuation_videos(token: str, seen_ids: set) -> list[dict]:
    """Fetch additional videos from playlist continuation token."""
    url = "https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
    payload = {
        "continuation": token,
        "context": {
            "client": {
                "clientName": "WEB",
                "clientVersion": "2.20231121.08.00",
                "hl": "en",
                "gl": "US"
            }
        }
    }
    videos = []
    try:
        resp = http_post_json(url, payload)
        actions = resp.get("onResponseReceivedActions", [])
        for a in actions:
            items = a.get("appendContinuationItemsAction", {}).get("continuationItems", [])
            for it in items:
                vid_id, title = _extract_from_item(it)
                if vid_id and vid_id not in seen_ids:
                    seen_ids.add(vid_id)
                    videos.append({"videoId": vid_id, "title": title})
    except Exception as e:
        print(f"    Continuation fetch error: {e}")
    return videos


def fetch_video_details(video_id: str) -> dict:
    """Fetch detailed video info (description, duration) using YouTube player API."""
    url = "https://www.youtube.com/youtubei/v1/player?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8"
    payload = {
        "videoId": video_id,
        "context": {
            "client": {
                "clientName": "WEB",
                "clientVersion": "2.20231121.08.00",
                "hl": "en",
                "gl": "US",
            }
        }
    }
    try:
        resp = http_post_json(url, payload)
        details = resp.get("videoDetails", {})
        duration_s = int(details.get("lengthSeconds", 0))
        description = details.get("shortDescription", "")
        return {
            "duration_seconds": str(duration_s),
            "formatted_duration": format_duration(duration_s),
            "description": description,
            "data_links": extract_data_links(description),
            "view_count": details.get("viewCount", "0"),
            "channel": details.get("author", ""),
        }
    except Exception as e:
        print(f"    WARN: Could not fetch details for {video_id}: {e}")
        return {
            "duration_seconds": "0",
            "formatted_duration": "?",
            "description": "",
            "data_links": [],
            "view_count": "0",
            "channel": "",
        }


# ── Folder and README generation ──────────────────────────────────────────────

def make_episode_folder(ep: dict) -> tuple[Path, str, str]:
    """Create the episode folder and return (folder_path, folder_name, module_folder)."""
    idx = ep["index"]
    title_clean = clean_title(ep["title"])
    module_name, module_folder = get_module(idx)
    slug = slugify(title_clean)
    folder_name = f"Ep{idx:02d}-{slug}"
    folder_path = REPO_ROOT / module_folder / folder_name
    folder_path.mkdir(parents=True, exist_ok=True)
    return folder_path, folder_name, module_folder


def generate_episode_readme(ep: dict, folder_path: Path, folder_name: str, module_folder: str):
    """Generate a README.md inside the episode folder."""
    idx = ep["index"]
    title_clean = clean_title(ep["title"])
    duration = ep.get("formatted_duration", "?")
    video_url = ep.get("url", f"https://www.youtube.com/watch?v={ep['videoId']}")
    data_links = ep.get("data_links", [])
    module_name, _ = get_module(idx)
    description = ep.get("description", "")

    data_section = ""
    if data_links:
        data_section = "## 📂 Official Dataset Links\n\n"
        for i, link in enumerate(data_links, 1):
            data_section += f"- [Dataset {i}]({link})\n"
    else:
        data_section = "## 📂 Official Dataset\n\n- Included with the lecture / no external dataset.\n"

    desc_preview = description[:500].replace('\n', '\n> ') if description else "*(No description available)*"

    readme_content = f"""# Ep {idx:02d} — {title_clean}

## 📺 Video Information

| Property | Details |
|----------|---------|
| **Episode** | {idx:02d} |
| **Module** | {module_name} |
| **Duration** | {duration} |
| **YouTube** | [Watch on YouTube]({video_url}) |

---

## 📝 Lesson Overview

> {desc_preview}

---

{data_section}

---

## ✅ Self-Study Checklist

- [ ] Watch the full episode on YouTube
- [ ] Download and open the dataset file(s)
- [ ] Reproduce the Power Query steps shown
- [ ] Take notes on key M Language expressions used
- [ ] Mark as complete in [PROGRESS_TRACKER.md](../../PROGRESS_TRACKER.md)

---

*Auto-generated by `scripts/sync_new_episodes.py` on {datetime.now().strftime('%Y-%m-%d')}*
"""
    readme_path = folder_path / "README.md"
    readme_path.write_text(readme_content, encoding="utf-8")
    print(f"    Generated README.md → {folder_name}/README.md")


def append_readme_table_row(ep: dict, folder_name: str, module_folder: str):
    """Append a new row to the Master Episode Directory table in README.md."""
    idx = ep["index"]
    title_clean = clean_title(ep["title"])
    duration = ep.get("formatted_duration", "?")
    video_url = ep.get("url", f"https://www.youtube.com/watch?v={ep['videoId']}")
    data_links = ep.get("data_links", [])
    module_name, _ = get_module(idx)
    readme_link = f"{module_folder}/{folder_name}/README.md"
    data_col = f"[Sample Data]({data_links[0]})" if data_links else "Included / Lecture"

    new_row = (
        f"| **{idx:02d}** "
        f"| `{module_name}` "
        f"| {title_clean} "
        f"| `{duration}` "
        f"| [{folder_name}]({readme_link}) "
        f"| [▶ YouTube]({video_url}) "
        f"| {data_col} |"
    )

    readme_text = README_FILE.read_text(encoding="utf-8")
    lines = readme_text.split('\n')
    insert_at = None
    in_table = False
    for i, line in enumerate(lines):
        if '## 📑 Master Episode Directory' in line:
            in_table = True
        if in_table and line.strip().startswith('|') and not line.strip().startswith('|:'):
            insert_at = i
        if in_table and line.strip() == '---' and insert_at is not None:
            break

    if insert_at is not None:
        lines.insert(insert_at + 1, new_row)
        README_FILE.write_text('\n'.join(lines), encoding="utf-8")
        print(f"    Appended row for Ep{idx:02d} to README.md")
    else:
        print(f"    WARN: Could not find table insertion point in README.md")


def append_progress_tracker_row(ep: dict, folder_name: str, module_folder: str):
    """Append a new checkbox row to PROGRESS_TRACKER.md."""
    idx = ep["index"]
    title_clean = clean_title(ep["title"])
    duration = ep.get("formatted_duration", "?")
    readme_link = f"{module_folder}/{folder_name}/README.md"

    new_row = f"| [ ] | **{idx:02d}** | {title_clean} | `{duration}` | [{folder_name}]({readme_link}) | | |"

    tracker_text = PROGRESS_FILE.read_text(encoding="utf-8")
    lines = tracker_text.split('\n')
    insert_at = None
    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip().startswith('|') and not lines[i].strip().startswith('|:'):
            insert_at = i
            break

    if insert_at is not None:
        lines.insert(insert_at + 1, new_row)
        PROGRESS_FILE.write_text('\n'.join(lines), encoding="utf-8")
        print(f"    Appended row for Ep{idx:02d} to PROGRESS_TRACKER.md")


def append_module_readme_row(ep: dict, folder_name: str, module_folder: str):
    """Append a new row to the module-level README.md table."""
    idx = ep["index"]
    title_clean = clean_title(ep["title"])
    duration = ep.get("formatted_duration", "?")
    video_url = ep.get("url", f"https://www.youtube.com/watch?v={ep['videoId']}")
    data_links = ep.get("data_links", [])
    data_col = f"[Sample Data]({data_links[0]})" if data_links else "Included"
    folder_link = f"{folder_name}/README.md"

    new_row = f"| **{idx:02d}** | {title_clean} | `{duration}` | [{folder_name}]({folder_link}) | [YouTube]({video_url}) | {data_col} |"

    module_readme = REPO_ROOT / module_folder / "README.md"
    if not module_readme.exists():
        return

    text = module_readme.read_text(encoding="utf-8")
    lines = text.split('\n')
    insert_at = None
    in_table = False
    for i, line in enumerate(lines):
        if '| Ep #' in line:
            in_table = True
        if in_table and line.strip().startswith('|') and not line.strip().startswith('|:'):
            insert_at = i
        if in_table and line.strip() == '---' and insert_at is not None:
            break

    if insert_at is not None:
        lines.insert(insert_at + 1, new_row)
        module_readme.write_text('\n'.join(lines), encoding="utf-8")
        print(f"    Appended row for Ep{idx:02d} to {module_folder}/README.md")


# ── Git operations ────────────────────────────────────────────────────────────

def git_commit_and_push(new_episodes: list):
    """Stage all changes and push to GitHub."""
    print("\nCommitting and pushing to GitHub…")
    titles = ", ".join([f"Ep{ep['index']:02d}" for ep in new_episodes])

    if os.environ.get("GITHUB_ACTIONS"):
        subprocess.run(["git", "config", "user.name", "github-actions[bot]"], cwd=str(REPO_ROOT))
        subprocess.run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], cwd=str(REPO_ROOT))

    cmds = [
        ["git", "add", "-A"],
        ["git", "commit", "-m", f"feat: Add {len(new_episodes)} new episode(s): {titles}"],
        ["git", "push", "origin", "main"],
    ]
    for cmd in cmds:
        result = subprocess.run(cmd, cwd=str(REPO_ROOT), capture_output=True, text=True)
        if result.returncode != 0 and "nothing to commit" not in result.stdout:
            print(f"  WARN: {' '.join(cmd)} exited {result.returncode}: {result.stderr}")
        else:
            print(f"  OK: {' '.join(cmd)}")


# ── Main sync logic ───────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Sync new episodes from YouTube playlist to repo")
    parser.add_argument("--dry-run", action="store_true", help="Check for new episodes but make no changes")
    parser.add_argument("--force-ep", type=int, help="Force-add a specific episode number (for testing)")
    args = parser.parse_args()

    print("=" * 60)
    print("PowerBI Diploma — New Episode Sync")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Load existing metadata
    with open(METADATA_FILE, encoding="utf-8") as f:
        existing = json.load(f)
    existing_ids = {ep["videoId"] for ep in existing}
    max_existing_idx = max(ep["index"] for ep in existing)
    print(f"Existing episodes in metadata: {len(existing)} (up to Ep{max_existing_idx:02d})")

    # Fetch current playlist
    playlist_videos = fetch_playlist_video_ids()

    # Find new videos
    new_videos = [v for v in playlist_videos if v["videoId"] not in existing_ids]

    if args.force_ep:
        new_videos = [v for v in playlist_videos if v["index"] == args.force_ep]
        print(f"Force mode: processing Ep{args.force_ep:02d}")

    if not new_videos:
        print("\n✅ No new episodes found. Repository is up to date!")
        return

    print(f"\n🆕 Found {len(new_videos)} new episode(s):")
    for v in new_videos:
        print(f"   Ep{v['index']:02d}: {v['title'][:60]}")

    if args.dry_run:
        print("\n[Dry-run mode] No changes made.")
        return

    # Process each new episode
    processed = []
    for v in new_videos:
        idx = v["index"]
        print(f"\nProcessing Ep{idx:02d}: {v['title'][:60]}…")

        time.sleep(1)  # be polite to YouTube API
        details = fetch_video_details(v["videoId"])
        ep = {
            **v,
            **details,
            "url": f"https://www.youtube.com/watch?v={v['videoId']}",
        }

        # Create folder
        folder_path, folder_name, module_folder = make_episode_folder(ep)
        print(f"  Folder: {module_folder}/{folder_name}")

        # Download datasets
        if ep.get("data_links"):
            print(f"  Downloading {len(ep['data_links'])} dataset(s)…")
            for link in ep["data_links"]:
                slug = clean_title(ep["title"]).replace(" ", "_")[:40]
                dest = folder_path / f"{slug}.xlsx"
                download_file(link, dest)

        # Generate episode README
        generate_episode_readme(ep, folder_path, folder_name, module_folder)

        # Update Master README, Progress Tracker, and Module README
        append_readme_table_row(ep, folder_name, module_folder)
        append_progress_tracker_row(ep, folder_name, module_folder)
        append_module_readme_row(ep, folder_name, module_folder)

        # Append to metadata
        existing.append(ep)
        processed.append(ep)

    # Save updated metadata
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    print(f"\nUpdated metadata/course_metadata.json ({len(existing)} total episodes)")

    # Commit and push
    git_commit_and_push(processed)

    print(f"\n✅ Done! Added {len(processed)} new episode(s) to the repository.")


if __name__ == "__main__":
    main()
