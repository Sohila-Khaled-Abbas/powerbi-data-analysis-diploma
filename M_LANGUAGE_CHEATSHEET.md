# ⚡ Power Query M Language Master Cheatsheet

> Comprehensive reference guide for the **Power Query M Language** covering all functions, syntax patterns, and engineering idioms taught across the **Microsoft Power BI Data Analysis Diploma** by **Essam Elsayed**.

---

## 📑 Table of Contents
- [1. M Language Architecture & Syntax](#1-m-language-architecture--syntax)
- [2. Primitive Types & Type Casting](#2-primitive-types--type-casting)
- [3. Working with Tables (Table.*)](#3-working-with-tables-table)
- [4. Working with Lists (List.*)](#4-working-with-lists-list)
- [5. Working with Records (Record.*)](#5-working-with-records-record)
- [6. Unpivoting & Pivoting Workflows](#6-unpivoting--pivoting-workflows)
- [7. Appending & Merging Joins](#7-appending--merging-joins)
- [8. Custom Functions & Invocation](#8-custom-functions--invocation)
- [9. Robust Error Handling & Null Coalescing](#9-robust-error-handling--null-coalescing)
- [10. Advanced Dynamic Transformation Patterns](#10-advanced-dynamic-transformation-patterns)

---

## 1. M Language Architecture & Syntax

M is a **case-sensitive**, **functional**, **declarative**, and **lazy** mashup language.

### Basic `let ... in` Structure
```powerquery
let
    // Step 1: Connect to source
    Source = Excel.Workbook(File.Contents("C:\Data\Sales.xlsx"), null, true),
    
    // Step 2: Navigate to target sheet
    Sales_Sheet = Source{[Item="SalesData", Kind="Sheet"]}[Data],
    
    // Step 3: Promote headers
    #"Promoted Headers" = Table.PromoteHeaders(Sales_Sheet, [PromoteAllScalars=true]),
    
    // Step 4: Cast column types
    #"Changed Type" = Table.TransformColumnTypes(#"Promoted Headers", {
        {"OrderID", Int64.Type},
        {"OrderDate", type date},
        {"Revenue", Currency.Type}
    })
in
    #"Changed Type"
```

> **Rules:**
> 1. Steps are executed based on dependency graph, not necessarily chronological order (**lazy evaluation**).
> 2. Variable names containing spaces or special characters must be escaped with `#"Step Name"`.
> 3. Comments: `// single line` or `/* multi-line */`.

---

## 2. Primitive Types & Type Casting

| M Type Keyword | Description | Example Literal |
|:---------------|:------------|:----------------|
| `type text` | Unicode text string | `"Cairo, Egypt"` |
| `type number` | 64-bit floating point number | `123.45` |
| `Int64.Type` | 64-bit signed integer | `1005` |
| `Currency.Type` | Fixed decimal (4 decimal places) | `99.9999` |
| `type date` | Calendar date (YYYY-MM-DD) | `#date(2026, 11, 5)` |
| `type time` | Time of day (hh:mm:ss) | `#time(14, 30, 0)` |
| `type datetime` | Combined date & time | `#datetime(2026, 11, 5, 14, 30, 0)` |
| `type datetimezone` | Date, time with timezone offset | `#datetimezone(2026, 11, 5, 14, 30, 0, 2, 0)` |
| `type duration` | Elapsed time span | `#duration(5, 4, 30, 0)` *(5d 4h 30m)* |
| `type logical` | Boolean True / False | `true` / `false` |
| `type binary` | Raw binary stream | `File.Contents(...)` |

### Rounding modes and tie-breaking

`Number.Round` uses `RoundingMode.ToEven` by default when a value is exactly halfway between two results (banker's rounding). Do not assume this is the required financial or business rule; select the mode required by the reporting policy.

~~~powerquery
Number.Round(2.5)                              // 2: tie to even
Number.Round(3.5)                              // 4: tie to even
Number.Round(2.5, 0, RoundingMode.AwayFromZero) // 3
Number.Round(-2.5, 0, RoundingMode.AwayFromZero) // -3
~~~

### Locale-Sensitive Parsing
When parsing international formats (e.g. British DD/MM/YYYY vs US MM/DD/YYYY):
```powerquery
// Cast date using UK culture
Table.TransformColumnTypes(Source, {{"OrderDate", type date}}, "en-GB")

// Cast decimal using German culture (comma as decimal separator)
Table.TransformColumnTypes(Source, {{"Price", type number}}, "de-DE")
```

---

## 3. Working with Tables (Table.*)

### Adding Columns
```powerquery
// Calculated Column
Table.AddColumn(Source, "Profit", each [Revenue] - [Cost], Currency.Type)

// Conditional Column
Table.AddColumn(Source, "Tier", each 
    if [Revenue] >= 100000 then "Platinum" 
    else if [Revenue] >= 50000 then "Gold" 
    else "Standard"
)

// Index Column (0-based or 1-based)
Table.AddIndexColumn(Source, "RowIndex", 1, 1, Int64.Type)
```

### Filtering & Selecting Rows
```powerquery
// Filter rows
Table.SelectRows(Source, each [Status] = "Active" and [Amount] > 0)

// Select specific columns (ignoring missing ones dynamically)
Table.SelectColumns(Source, {"ID", "Name", "Total"}, MissingField.Ignore)

// Remove specific columns
Table.RemoveColumns(Source, {"TempCol1", "TempCol2"})
```

### Grouping & Aggregating
```powerquery
Table.Group(Source, {"Department", "Year"}, {
    {"TotalSalary", each List.Sum([Salary]), Currency.Type},
    {"EmployeeCount", each Table.RowCount(_), Int64.Type},
    {"AverageSalary", each List.Average([Salary]), type number}
})
```

---

## 4. Working with Lists (List.*)

```powerquery
// List literal
MyList = {1, 2, 3, 4, 5}

// Generate range
NumberSequence = {1..100}
DateSequence = List.Dates(#date(2026, 1, 1), 365, #duration(1, 0, 0, 0))

// List transformations
List.Sum({10, 20, 30})            // 60
List.Average({10, 20, 30})        // 20
List.Distinct({1, 1, 2, 2, 3})    // {1, 2, 3}
List.Contains({"Apple", "Banana"}, "Apple") // true

// Transform each item in a list
List.Transform({"  a ", " b"}, each Text.Trim(_)) // {"a", "b"}
```

### Advanced Stateful Looping with `List.Generate`
Used for API and Web Pagination:
```powerquery
PaginatedData = List.Generate(
    () => [Page = 1, Data = FetchApiPage(1)],
    each not List.IsEmpty([Data]),
    each [Page = [Page] + 1, Data = FetchApiPage([Page] + 1)],
    each [Data]
)
```

---

## 5. Working with Records (Record.*)

```powerquery
// Record literal
Customer = [ID = 101, Name = "Essam Elsayad", Country = "Egypt", IsActive = true]

// Field access
NameVal = Customer[Name] // "Essam Elsayad"

// Safe field access with fallback
CityVal = Record.FieldOrDefault(Customer, "City", "Unknown") // "Unknown"

// Converting record to table
TableFromRecord = Record.ToTable(Customer)
```

---

## 6. Unpivoting & Pivoting Workflows

### The Golden Rule of Unpivoting
Always prefer **Unpivot Other Columns** rather than *Unpivot Selected Columns*, because new dates/months added in future months will be automatically ingested without breaking the query!
```powerquery
// Best Practice: Unpivot all columns EXCEPT key identifiers
#"Unpivoted Other Columns" = Table.UnpivotOtherColumns(
    Source, 
    {"AccountID", "AccountName", "CostCenter"}, 
    "DateHeader", 
    "Amount"
)
```

### Pivoting Rows into Columns
```powerquery
#"Pivoted Column" = Table.Pivot(
    Source, 
    List.Distinct(Source[Attribute]), 
    "Attribute", 
    "Value", 
    List.Sum
)
```

---

## 7. Appending & Merging Joins

### Appending Tables (Vertical Stacking)
```powerquery
// Combine multiple tables into one
CombinedSales = Table.Combine({Sales2021, Sales2022, Sales2023})
```

### Merging Tables (Relational Joins)
```powerquery
// Left Outer Join
#"Merged Queries" = Table.NestedJoin(
    FctSales, {"CustomerID"}, 
    DimCustomer, {"CustomerID"}, 
    "CustomerLookup", 
    JoinKind.LeftOuter
),
#"Expanded Lookup" = Table.ExpandTableColumn(
    #"Merged Queries", 
    "CustomerLookup", 
    {"CustomerName", "Region", "Segment"}
)
```

| JoinKind Value | Meaning |
|:---------------|:--------|
| `JoinKind.Inner` | Only rows matching in BOTH tables |
| `JoinKind.LeftOuter` | All rows from Left table, matched rows from Right |
| `JoinKind.RightOuter` | All rows from Right table, matched rows from Left |
| `JoinKind.FullOuter` | All rows from both tables |
| `JoinKind.LeftAnti` | Rows in Left table that do NOT exist in Right |
| `JoinKind.RightAnti` | Rows in Right table that do NOT exist in Left |

### Fuzzy Matching with Threshold
```powerquery
Table.FuzzyNestedJoin(
    TableA, {"VendorName"},
    TableB, {"CleanVendor"},
    "Matched",
    JoinKind.LeftOuter,
    [IgnoreCase = true, Threshold = 0.85]
)
```

---

## 8. Custom Functions & Invocation

### Declaring a Typed Reusable Function
```powerquery
(DateInput as date, optional FiscalYearStartMonth as number) as text =>
let
    StartMonth = if FiscalYearStartMonth = null then 1 else FiscalYearStartMonth,
    CurMonth = Date.Month(DateInput),
    CurYear = Date.Year(DateInput),
    FY = if CurMonth >= StartMonth then CurYear + 1 else CurYear,
    Result = "FY" & Text.End(Text.From(FY), 2)
in
    Result
```

### Invoking Function Across Rows
```powerquery
Table.AddColumn(Source, "FiscalYear", each fnGetFiscalYear([OrderDate], 7))
```

---

## 9. Robust Error Handling & Null Coalescing

### Null Coalescing Operator (`??`)
Replaces `null` with a fallback value in a clean, concise expression:
```powerquery
// Return Discount if not null, otherwise return 0
[Discount] ?? 0

// Chained Coalescing: Check Phone, fallback to Mobile, fallback to "N/A"
[WorkPhone] ?? [MobilePhone] ?? "N/A"
```

### Try ... Otherwise Defensive Programming
```powerquery
// Safe type conversion that never crashes on corrupt strings
try Number.FromText([RawText]) otherwise 0

// Inspecting error metadata
let
    Attempt = try [CalculationStep],
    Output = if Attempt[HasError] then 
                 "Error: " & Attempt[Error][Message] 
             else 
                 Attempt[Value]
in
    Output
```

---

## 10. Advanced Dynamic Transformation Patterns

### Transforming All Columns Dynamically
Trim whitespace across columns declared as text. Text.Trim accepts nullable text; applying it to number, date, logical, or other non-text columns can raise type errors. Set types first, or explicitly list intended columns:
```powerquery
let
    Source = ...,
    // Table.ColumnsOfType returns only columns whose declared type is text.
    TextColumnNames = Table.ColumnsOfType(Source, {type text}),
    TransformOperations = List.Transform(
        TextColumnNames,
        each {_, Text.Trim, type text}
    ),
    CleanTable = Table.TransformColumns(Source, TransformOperations)
in
    CleanTable
```

### Dynamic Excel Folder Ingestion (Same-Named Sheet Pattern)

This version consolidates a worksheet named `Sales` from each workbook. Change the sheet name and file filters to match the actual folder contents.

~~~powerquery
let
    Source = Folder.Files("C:\DataFolder"),
    FilteredFiles = Table.SelectRows(
        Source,
        each Text.Lower([Extension]) = ".xlsx"
            and not Text.StartsWith([Name], "~$")
    ),
    AddedWorkbookObjects = Table.AddColumn(
        FilteredFiles,
        "WorkbookObjects",
        each Excel.Workbook([Content], null, true)
    ),
    ExpandedWorkbookObjects = Table.ExpandTableColumn(
        AddedWorkbookObjects,
        "WorkbookObjects",
        {"Item", "Kind", "Data"},
        {"Item", "Kind", "Data"}
    ),
    // Assumes each workbook contains a worksheet named "Sales".
    SelectedSalesSheets = Table.SelectRows(
        ExpandedWorkbookObjects,
        each [Kind] = "Sheet" and [Item] = "Sales"
    ),
    PromotedHeaders = Table.AddColumn(
        SelectedSalesSheets,
        "Rows",
        each Table.PromoteHeaders([Data], [PromoteAllScalars = true])
    ),
    Combined = Table.Combine(PromotedHeaders[Rows])
in
    Combined
~~~

**Assumptions and checks:** all selected worksheets have compatible column structures; the sheet name matches exactly; hidden/temp files are considered; and column types are applied and validated after combining. This is a same-named-sheet pattern, not a universal workbook parser.
---
*Created as part of the Microsoft Power BI Data Analysis Diploma Repository.*
