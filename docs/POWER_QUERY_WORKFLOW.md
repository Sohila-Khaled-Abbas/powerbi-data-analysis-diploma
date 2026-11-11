# Power Query Workflow Playbook

A practical checklist for building transformations that are understandable, testable, and maintainable.

## End-to-end flow

~~~mermaid
flowchart TD
    A["Source systems: files, APIs, databases"] --> B["Connect and navigate"]
    B --> C["Profile raw data"]
    C --> D["Define grain, keys, expected schema"]
    D --> E["Transform and standardize"]
    E --> F["Validate results"]
    F --> G{"Checks pass?"}
    G -- "No" --> H["Inspect assumptions and steps"]
    H --> E
    G -- "Yes" --> I["Load to model or destination"]
    I --> J["Document refresh and ownership"]
~~~

## 1. Connect with intent

- Identify the authoritative source and its owner.
- Prefer stable paths, parameters, and supported connectors over machine-specific hardcoding.
- Understand authentication and privacy requirements before combining sources.
- For APIs, document pagination, expected response shape, rate limits, and failure behavior.
- Never embed secrets in M code or committed files.

## 2. Profile before transforming

Inspect column names and types, row count, representative values, nulls, blanks, errors, duplicates, candidate keys, row grain, locale, and unexpected or missing columns. Do not remove rows or replace missing values until their meaning is understood.

## 3. Transform in readable steps

- Use descriptive step names.
- Set types deliberately.
- Normalize headers and text consistently.
- Separate staging/helper queries from final outputs when it improves reuse.
- Use parameters for values that legitimately vary between environments.
- Use dynamic column handling only when the schema contract supports it.
- Consider query folding for supported sources; verify rather than assume it is preserved.

## 4. Choose reshape operations carefully

| Operation | Typical use | Main question |
|---|---|---|
| Filter rows | Exclude records outside scope | Is the rule justified? |
| Unpivot | Convert repeated attribute columns into attribute/value rows | Which columns define the key? |
| Pivot | Turn attribute values into columns | What aggregation applies to duplicates? |
| Append | Stack similar tables | Are schemas and meanings aligned? |
| Merge | Enrich a table from another | Are join keys compatible and cardinality understood? |
| Group By | Aggregate records to a higher grain | Which fields define each group? |

### Join validation

Inspect key uniqueness on both sides before merging. A many-to-many match can multiply rows. After expanding the nested table, compare row counts and key-level totals with expectations.

## 5. Handle imperfect data explicitly

- Distinguish null, empty text, whitespace-only text, and error values.
- Use locale-aware conversion for dates and numbers.
- Decide how to handle missing fields and schema drift.
- Use try/otherwise when a fallback is meaningful; do not hide errors indiscriminately.
- Treat fuzzy matching as a candidate-matching aid that requires review, not proof of identity.

## 6. Validate before loading

Compare input/output row counts and explain expected changes. Check uniqueness and null rates for key columns. Reconcile business totals, inspect errors and edge cases, refresh after source-shape changes where practical, and confirm output grain before modeling.

## 7. Document the result

For each important query, capture its purpose and output grain, source and refresh assumptions, transformation decisions, data-quality rules, validation performed, and known limitations.

## Reusable M patterns

### Safe field access

~~~powerquery
Record.FieldOrDefault([RecordColumn], "OptionalField", null)
~~~

### Ignore a missing column during selection

~~~powerquery
Table.SelectColumns(Source, {"CustomerID", "Region", "Revenue"}, MissingField.Ignore)
~~~

### Explicit conversion with a fallback

~~~powerquery
try Number.FromText([RawAmount], "en-US") otherwise null
~~~

Choose a fallback that preserves the distinction between a legitimate zero and an unparseable value.

Related: [M Language Cheatsheet](../M_LANGUAGE_CHEATSHEET.md) · [Learning Path](LEARNING_PATH.md)
