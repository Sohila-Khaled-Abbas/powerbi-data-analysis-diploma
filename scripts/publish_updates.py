#!/usr/bin/env python3
"""
publish_updates.py
==================
All-in-one repository updater & publisher.
Run this script whenever you:
  - Add new solution models (.pbix), practice sheets (.xlsx), or notes to any folder
  - Want to check and fetch new episodes published on YouTube
  - Want to ensure all READMEs, checklists, and curriculums are synchronized
  - Want to publish all changes to GitHub in a single command

Usage:
    python scripts/publish_updates.py           # Sync, update docs, commit & push
    python scripts/publish_updates.py --dry-run # Preview changes without committing
    python scripts/publish_updates.py --no-sync # Update local docs & publish without checking YouTube
"""

import os
import re
import sys
import glob
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime

# Import sync functions from sync_new_episodes
REPO_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(REPO_ROOT / "scripts"))
try:
    import sync_new_episodes as sync_engine
except ImportError:
    sync_engine = None

EXT_DESCRIPTIONS = {
    ".pbix": ("📊", "Power BI Desktop solution model"),
    ".pbit": ("📊", "Power BI template model"),
    ".xlsx": ("📄", "Excel practice dataset"),
    ".xls":  ("📄", "Excel legacy dataset"),
    ".csv":  ("📋", "CSV data file"),
    ".tsv":  ("📋", "TSV data file"),
    ".txt":  ("📋", "Text / delimited data file"),
    ".pdf":  ("📑", "PDF source document / statement"),
    ".json": ("📦", "JSON data payload"),
}

def format_file_size(size_bytes: int) -> str:
    if size_bytes >= 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB ({size_bytes:,} bytes)"
    elif size_bytes >= 1024:
        return f"{size_bytes / 1024:.1f} KB ({size_bytes:,} bytes)"
    return f"{size_bytes:,} bytes"


def get_practice_files_section(folder_path: str) -> str:
    """Scan folder and build markdown section listing all practice files."""
    files_list = []
    has_pbix = False
    has_xlsx = False

    for root, dirs, files in os.walk(folder_path):
        for f in sorted(files):
            if f == "README.md" or f.startswith("~$") or f.endswith(".tmp") or f.endswith(".py"):
                continue
            ext = os.path.splitext(f)[1].lower()
            if ext in EXT_DESCRIPTIONS:
                icon, desc = EXT_DESCRIPTIONS[ext]
                if ext == ".pbix":
                    has_pbix = True
                if ext in [".xlsx", ".xls", ".csv"]:
                    has_xlsx = True
                full_p = os.path.join(root, f)
                size_str = format_file_size(os.path.getsize(full_p))
                rel_f = os.path.relpath(full_p, folder_path).replace("\\", "/")
                files_list.append(f"- {icon} **`{rel_f}`** (`{size_str}`) — {desc}")

    if not files_list:
        return "## 📁 Practice Files in this Repository\n\n- *Included with the lecture instructions / no local dataset required.*\n"

    section = "## 📁 Practice Files in this Repository\n\nThis episode folder contains the following hands-on practice assets:\n\n"
    section += "\n".join(files_list) + "\n\n"

    tip_parts = []
    if has_pbix:
        tip_parts.append("Open `.pbix` files in **Microsoft Power BI Desktop**")
    if has_xlsx:
        tip_parts.append("Open `.xlsx` files in **Microsoft Excel** to inspect source tables, verify data types, and follow along with the transformations")
    if tip_parts:
        section += f"> 💡 **How to use:** {'; and '.join(tip_parts)}.\n"
    return section


def update_episode_readme(folder_path: str) -> bool:
    """Update practice files section in episode README.md."""
    readme_path = os.path.join(folder_path, "README.md")
    if not os.path.exists(readme_path):
        return False

    new_section = get_practice_files_section(folder_path)

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r'## (?:📁|📂) Practice Files in this Repository.*?(?=\n---|\n## (?:📝|✅|🧭)|\Z)'
    if re.search(pattern, content, re.DOTALL):
        updated = re.sub(pattern, new_section.strip(), content, flags=re.DOTALL)
    else:
        inserted = False
        for marker in ['\n---\n\n## ✅ Self-Study Checklist', '\n## ✅ Self-Study Checklist', '\n## 📝 Self-Study & Hands-On Practice Checklist', '\n## 🧭 Navigation']:
            if marker in content:
                idx = content.find(marker)
                updated = content[:idx] + f"\n\n---\n\n{new_section.strip()}\n" + content[idx:]
                inserted = True
                break
        if not inserted:
            updated = content + f"\n\n---\n\n{new_section.strip()}\n"

    if updated != content:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated)
        return True
    return False


def refresh_all_practice_files():
    """Scan all episode folders and update their READMEs."""
    print("Refreshing practice file listings across all episode folders...")
    ep_folders = sorted(glob.glob(os.path.join(str(REPO_ROOT), "0*", "Ep*")))
    updated = []
    for f in ep_folders:
        if update_episode_readme(f):
            updated.append(os.path.basename(f))
    if updated:
        print(f"  Updated {len(updated)} episode README(s): {', '.join(updated[:5])}{'...' if len(updated) > 5 else ''}")
    else:
        print("  All episode READMEs already have accurate practice file listings.")
    return updated


def refresh_totals():
    """Ensure README.md, CURRICULUM.md, and PROGRESS_TRACKER.md reflect the current total episodes."""
    meta_path = REPO_ROOT / "metadata" / "course_metadata.json"
    if not meta_path.exists():
        return
    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)
    total_eps = len(meta)

    # 1. README.md
    readme_path = REPO_ROOT / "README.md"
    if readme_path.exists():
        t = readme_path.read_text(encoding="utf-8")
        t = re.sub(r'Lectures-\d+%20Comprehensive%20Episodes', f'Lectures-{total_eps}%20Comprehensive%20Episodes', t)
        t = re.sub(r'complete \d+-lecture Microsoft Power BI', f'complete {total_eps}-lecture Microsoft Power BI', t)
        t = re.sub(r'all \d+ video lectures into', f'all {total_eps} video lectures into', t)
        t = re.sub(r'Master Episode Directory \(All \d+ Lectures\)', f'Master Episode Directory (All {total_eps} Lectures)', t)
        t = re.sub(r'Ep\.\s*65\s*-\s*\d+', f'Ep. 65 - {total_eps}', t)
        readme_path.write_text(t, encoding="utf-8")

    # 2. PROGRESS_TRACKER.md
    pt_path = REPO_ROOT / "PROGRESS_TRACKER.md"
    if pt_path.exists():
        t = pt_path.read_text(encoding="utf-8")
        t = re.sub(r'Total Episodes:\*\* \d+ Lectures', f'Total Episodes:** {total_eps} Lectures', t)
        pt_path.write_text(t, encoding="utf-8")

    # 3. CURRICULUM.md
    cur_path = REPO_ROOT / "CURRICULUM.md"
    if cur_path.exists():
        t = cur_path.read_text(encoding="utf-8")
        t = re.sub(r'\(Ep\.\s*65\s*-\s*\d+\)', f'(Ep. 65 - {total_eps})', t)
        cur_path.write_text(t, encoding="utf-8")


def git_publish(dry_run: bool = False):
    """Stage, commit, and push changes to GitHub."""
    status = subprocess.run(["git", "status", "--porcelain"], cwd=str(REPO_ROOT), capture_output=True, text=True)
    changes = [l.strip() for l in status.stdout.splitlines() if l.strip()]

    if not changes:
        print("\n✅ Working tree is clean. Nothing new to commit or push!")
        return

    print(f"\nDetected {len(changes)} changed / untracked file(s):")
    for c in changes[:10]:
        print(f"  {c}")
    if len(changes) > 10:
        print(f"  ... and {len(changes) - 10} more.")

    if dry_run:
        print("\n[Dry-Run] Skipped commit and push.")
        return

    # Determine smart commit message
    new_files = [c[3:] for c in changes if c.startswith("??") or c.startswith("A ")]
    pbix_files = [f for f in new_files if f.endswith(".pbix")]
    
    if pbix_files:
        commit_msg = f"feat: Add user solution models & practice files ({len(pbix_files)} model(s))"
    elif any("Ep" in c for c in changes):
        commit_msg = "feat: Update episode practice files and course documentation"
    else:
        commit_msg = "chore: Sync repository updates and documentation"

    print(f"\nCommitting: '{commit_msg}'...")
    subprocess.run(["git", "add", "-A"], cwd=str(REPO_ROOT), check=True)
    subprocess.run(["git", "commit", "-m", commit_msg], cwd=str(REPO_ROOT), check=True)

    print("Pushing to GitHub (origin/main)...")
    push_res = subprocess.run(["git", "push", "origin", "main"], cwd=str(REPO_ROOT), capture_output=True, text=True)
    if push_res.returncode == 0:
        print("🚀 Successfully published to GitHub!")
    else:
        print(f"WARN: Push completed with message: {push_res.stderr or push_res.stdout}")


def main():
    parser = argparse.ArgumentParser(description="Update repo docs with new files and publish to GitHub")
    parser.add_argument("--dry-run", action="store_true", help="Preview updates without committing or pushing")
    parser.add_argument("--no-sync", action="store_true", help="Skip YouTube playlist check and only update local files")
    args = parser.parse_args()

    print("=" * 60)
    print("Power BI Diploma — Repository Updater & Publisher")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Step 1: Sync new YouTube episodes (unless --no-sync is given)
    if not args.no_sync and sync_engine:
        print("\n[1/4] Checking YouTube Playlist for new episodes...")
        try:
            # Call sync_engine main or check
            sync_engine.main()
        except Exception as e:
            print(f"  Notice: YouTube sync check completed or skipped ({e})")
    else:
        print("\n[1/4] YouTube sync skipped (--no-sync).")

    # Step 2: Refresh practice files documentation across all episodes
    print("\n[2/4] Updating episode documentation for all local practice files...")
    refresh_all_practice_files()

    # Step 3: Refresh course totals in README, CURRICULUM, PROGRESS_TRACKER
    print("\n[3/4] Synchronizing course syllabus totals...")
    refresh_totals()

    # Step 4: Commit and publish to GitHub
    print("\n[4/4] Publishing updates to GitHub...")
    git_publish(dry_run=args.dry_run)

    print("\n" + "=" * 60)
    print("🎉 All updates and documentation are in sync!")
    print("Repository: https://github.com/Sohila-Khaled-Abbas/powerbi-data-analysis-diploma")
    print("=" * 60)


if __name__ == "__main__":
    main()
