# Lecture Documentation Standard

This standard keeps lecture pages consistent without pretending every episode covers the same depth. Apply it incrementally when a page is next updated; do not overwrite lesson-specific observations or instructor terminology.

## Required information

| Section | What belongs here |
|---|---|
| Title & episode | Exact episode number and lecture title |
| Source | Official video URL, duration, and source-data URL when available |
| Lesson overview | Short factual summary of the problem or topic |
| Learning objectives | 2–5 observable skills tied to that lecture |
| Key concepts | Terms, decisions, and important distinctions |
| Demonstration notes | Steps actually shown or explicitly labelled as an independent extension |
| M reference | Minimal, runnable code where practical; state assumptions and placeholders |
| Practice assets | Actual repository files and original-source links; never invent filenames |
| Hands-on task | A task learner can attempt without copying the video |
| Validation | Expected checks, edge cases, and acceptance criteria |
| Reflection | What changed, why it worked, and what remains uncertain |
| Navigation | Previous / module / course / next links verified against the tree |

## Accuracy rules

1. Separate **course content** from **independent practice extensions**.
2. Never claim a transformation, metric, table, or output exists unless the source material or repository file confirms it.
3. Mark placeholders such as file paths, worksheet names, column names, and API URLs clearly.
4. Explain whether code is illustrative or expected to run as written.
5. Do not recommend checking query folding for connectors or steps where native-query inspection is unavailable.
6. Do not silently replace errors or nulls with zero; explain the business meaning of the fallback.
7. A "practice file" list must reflect files that actually exist in that episode folder.
8. Keep original instructor and sample-data links intact.

## Recommended page structure

Use [the episode template](../templates/EPISODE_README_TEMPLATE.md). For older pages, add missing sections gradually rather than rewriting lesson notes from memory.

## Review checklist

- [ ] Episode number, title, duration, and links are correct.
- [ ] Learning objectives are specific and lecture-aligned.
- [ ] Course notes and independent extensions are distinguished.
- [ ] Code has complete inputs, output, and assumptions.
- [ ] Text says whether the example is illustrative or runnable.
- [ ] Practice asset names match the repository.
- [ ] Validation checks fit the data problem.
- [ ] Previous/next links point to existing pages.
- [ ] No credentials, personal data, or restricted assets are committed.
