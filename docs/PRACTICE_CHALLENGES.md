# Independent Practice Challenges

These challenges extend the diploma topics. They are **not presented as instructor solutions**. Use the linked lecture pages for the original demonstration and use this pack to test whether you can transfer the concepts to new data.

## Challenge 01 · Excel source navigation

**Related lesson:** [Episode 03 — Get Data From Microsoft Excel](../02-Data-Acquisition/Ep03-Get-Data-From-Excel/README.md)

**Scenario:** A workbook contains both formatted worksheets and named Excel Tables. A user adds new rows to a table and occasionally creates a temporary worksheet for analysis.

**Tasks**

1. Connect to the workbook with `Excel.Workbook`.
2. Inspect the navigation table and distinguish objects by `Item` and `Kind`.
3. Select the intended Excel Table explicitly rather than relying on a sheet's used range.
4. Document what happens when new rows are added to the table.
5. Test the query after a temporary worksheet is added.

**Acceptance checks:** the expected object is selected; new table rows are included on refresh; unrelated workbook objects do not enter the final result.

**Hint:** `Excel.Workbook(File.Contents(path), null, true)` exposes workbook objects for navigation. Replace `path`, `Item`, and `Kind` with values observed in your own workbook.

## Challenge 02 · Unpivot, then pivot back

**Related lesson:** [Episodes 40–41 — Unpivot and Pivot](../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/README.md)

Start with this intentionally wide sample:

~~~powerquery
let
    Source = #table(
        type table [Region = text, Product = text, Jan = number, Feb = number, Mar = number],
        {
            {"North", "A", 10, 12, 15},
            {"South", "A", 8, 9, 11},
            {"North", "B", 7, 6, 10}
        }
    ),
    LongFormat = Table.UnpivotOtherColumns(
        Source,
        {"Region", "Product"},
        "Month",
        "Sales"
    )
in
    LongFormat
~~~

**Tasks**

1. Explain why `Region` and `Product` are identifiers and should remain as key columns.
2. Build the long-format result.
3. Pivot `Month` back to columns using `List.Distinct(LongFormat[Month])`.
4. Add a duplicate key/month row and observe why an aggregation function may be required.
5. Compare row counts and values before and after the round trip.

**Acceptance checks:** the long result has one row per Region–Product–Month combination in the original sample; the pivot result reconciles to the source when keys are unique.

## Challenge 03 · Multi-source model design

**Related lesson:** [Episode 55 — Full Project from Multiple Data Sources](../06-Case-Studies/Ep55-Full-Project-Multiple-Sources/README.md)

**Scenario:** Customer, product, and sales data arrive in separate workbooks. Before building relationships, document the intended grain of each source and identify the business key used to connect them.

**Tasks**

1. Profile each source independently.
2. Write a one-sentence grain statement for each table.
3. Identify candidate primary and foreign keys; test nulls and duplicates.
4. Propose a fact-and-dimension layout.
5. Create one-to-many relationships only after checking key uniqueness on the dimension side.
6. Reconcile a total from the source sales data to the fact table after transformation.

**Acceptance checks:** no relationship is based only on similarly named columns; row multiplication is investigated; totals and key coverage are explained.

**Important:** choose the fact grain from the actual source records. Do not assume one row represents an order, an order line, or a daily aggregate without checking.

## Challenge 04 · A defensive custom function

**Related lesson:** [Episode 73 — Build Custom Functions](../07-Power-Query-Engine-and-M-Language/Ep73-Build-Custom-Functions/README.md)

**Scenario:** Several queries need the same fiscal-year label, but the fiscal start month can vary by organization.

**Tasks**

1. Create a function with a date parameter and an optional fiscal-start-month parameter.
2. Default the month only when the argument is omitted or null.
3. Reject values outside the 1–12 range rather than silently returning a misleading label.
4. Test January, the month before the fiscal-year boundary, the boundary month, and December.
5. Invoke the function over a table and validate expected labels.

**Acceptance checks:** the function is reusable, parameters are typed, invalid configuration is surfaced clearly, and boundary dates are tested.

## Evidence to save

For each challenge, keep the input shape, final output, query/M code, assumptions, and validation notes. A screenshot alone is not enough to explain why the transformation is correct.
