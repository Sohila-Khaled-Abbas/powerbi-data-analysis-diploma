# Learning & Data Flow Diagrams

These are conceptual learning aids. They do not claim that every course exercise implements the exact architecture shown.

## 1. Curriculum map

~~~mermaid
flowchart TD
    A["01 · Foundations"] --> B["02 · Acquisition"]
    B --> C["03 · Advanced extraction"]
    C --> D["04 · Governance and automation"]
    D --> E["05 · Transformation"]
    E --> F["06 · Case studies"]
    F --> G["07 · M language and engine"]
    G --> H["Independent practice"]
    H -. "Reinforce fundamentals" .-> A
~~~

## 2. From source to analytical output

~~~mermaid
flowchart LR
    A["Excel / CSV / PDF"] --> E["Power Query"]
    B["SQL / enterprise DB"] --> E
    C["Web / API / JSON"] --> E
    D["Cloud services"] --> E
    E --> F["Clean and conform"]
    F --> G["Validate grain, keys, totals"]
    G --> H["Power BI semantic model"]
    H --> I["Reports and decisions"]
~~~

## 3. Transformation decision guide

~~~mermaid
flowchart TD
    A["What shape change is needed?"] --> B{"What is the goal?"}
    B -- "Stack similar datasets" --> C["Append / Table.Combine"]
    B -- "Enrich from another table" --> D["Merge / Table.NestedJoin"]
    B -- "Repeated columns become rows" --> E["Unpivot"]
    B -- "Values become headers" --> F["Pivot"]
    B -- "Summarize records" --> G["Group By / Table.Group"]
    C --> H["Validate schema and row counts"]
    D --> H
    E --> H
    F --> H
    G --> H
~~~

## 4. API pagination concept

~~~mermaid
flowchart TD
    A["Set initial page or cursor"] --> B["Request page"]
    B --> C["Check response status and shape"]
    C --> D{"More results?"}
    D -- "Yes" --> E["Extract records and next cursor"]
    E --> B
    D -- "No" --> F["Combine collected pages"]
    F --> G["Validate duplicates and completeness"]
~~~

A robust implementation should consider failed requests, rate limits, repeated cursors, and maximum-page safeguards.

## 5. Learning loop

~~~mermaid
flowchart LR
    A["Watch"] --> B["Rebuild"]
    B --> C["Experiment"]
    C --> D["Explain"]
    D --> E["Validate"]
    E --> F["Document and reuse"]
    F -.-> A
~~~

Use these diagrams with the [phase notes](../CURRICULUM.md) and the [Power Query Workflow Playbook](POWER_QUERY_WORKFLOW.md).
