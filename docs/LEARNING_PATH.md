# Learning Path & Study Method

A practical guide for studying the 83-episode diploma. Adapt the pace to your schedule; prioritize practice and the ability to explain your decisions.

## Study in six passes

| Pass | What to do | Evidence |
|---|---|---|
| Preview | Read the phase overview and identify prerequisites | Questions to answer |
| Learn | Watch the lesson and capture the problem | Notes in your own words |
| Rebuild | Reproduce the demonstrated steps | Working query or PBIX where applicable |
| Experiment | Change the source shape or test an edge case | A note describing what changed |
| Explain | Describe why each transformation is needed | Concise explanation without copying |
| Review | Rebuild key steps after a delay | Tracker entry and reusable pattern |

## Recommended sequence

1. **Foundations (01–02):** BI workflow and analytical raw-data structure.
2. **Acquisition (03–14):** files, cloud sources, and databases.
3. **Advanced extraction (15–23):** web tables, APIs, pagination, and nested JSON.
4. **Governance (24–31):** privacy, credentials, storage modes, dataflows, and parameters.
5. **Transformation (32–47):** types, locale, custom columns, reshaping, append, and merge.
6. **Case studies (48–64):** practical data-cleaning and integration problems.
7. **M and engine (65–83):** M fundamentals, custom functions, errors, and dynamic transformations.

## Session checklist

- [ ] State the data problem in one sentence.
- [ ] Identify source tables, grain, keys, and expected output.
- [ ] Watch the lesson and record terminology.
- [ ] Rebuild the transformation using practice material when available.
- [ ] Test an edge case: null, blank, duplicate, missing field, unexpected type, or new column.
- [ ] Validate row counts, distinct keys, totals, and types where relevant.
- [ ] Save a note: problem → approach → why → validation → lesson learned.
- [ ] Update the [progress tracker](../PROGRESS_TRACKER.md).

## Validate your work

| Check | Questions |
|---|---|
| Row count | Did rows disappear or multiply unexpectedly? |
| Grain | Does one row still represent the intended entity or event? |
| Keys | Are key columns populated and unique where expected? |
| Types | Are dates, numbers, and identifiers typed correctly? |
| Nulls/errors | Are missing values and errors understood? |
| Reconciliation | Do important totals match a trusted source? |
| Schema drift | What happens when columns are added or removed? |
| Refresh | Does the solution still work after a refresh? |

## Build evidence of learning

Keep a before/after sample, a readable query or M snippet, a short explanation of a design choice, a validation result, and a note about assumptions. Only publish material you are permitted to share. Never commit credentials or private data.

## Mastery checkpoints

- After phase 2: connect to a new source and explain the connector choices.
- After phase 3: explain pagination termination and API failure handling.
- After phase 5: reshape unfamiliar tables while preserving grain and validating results.
- After phase 6: defend an end-to-end cleaning strategy and its assumptions.
- After phase 7: write a typed custom function and handle missing fields safely.

**Study principle:** explain the reason behind a transformation. Memorizing button sequences is not the same as understanding the data problem.
