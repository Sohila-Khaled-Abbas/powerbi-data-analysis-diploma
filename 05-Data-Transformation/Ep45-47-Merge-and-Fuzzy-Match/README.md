# Episodes 45 - 47: Merge & Join Kind (Theory) | Ep. 45 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 45** | Merge & Join Kind (Theory) | Ep. 45 | Microsoft Power BI Data Analysis Diploma | `13m 10s` | [Watch on YouTube](https://www.youtube.com/watch?v=CxBN3M5kSxw) | Included in repo / Follow lecture |
| **Ep. 46** | Merge & Join Kind | Ep. 46 | Microsoft Power BI Data Analysis Diploma | `16m 13s` | [Watch on YouTube](https://www.youtube.com/watch?v=IAZ-1trfu7c) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1wdzuZge2xv5o-UmSfOzDPpmUGQGV4n1Q/edit?usp=sharing&ouid=107970738919672012073&rtpof=true&sd=true) |
| **Ep. 47** | Fuzzy Match | Ep. 47 | Microsoft Power BI Data Analysis Diploma | `22m 41s` | [Watch on YouTube](https://www.youtube.com/watch?v=G1hiA-uXyDg) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

### Part 45: Merge & Join Kind (Theory) | Ep. 45 | Microsoft Power BI Data Analysis Diploma

Theoretical deep dive into Merge Queries and Relational Join Kinds. Explains Inner, Left Outer, Right Outer, Full Outer, Left Anti, and Right Anti joins.

**Key Skills & Concepts Covered:**
- ✅ **Join Types (Inner, Left Outer, Full Outer, Anti)**
- ✅ **Relational Algebra in BI**
- ✅ **Cardinality (1:1, 1:Many, Many:Many)**
- ✅ **Hash Joins vs Nested Loops in Mashup Engine**

### Part 46: Merge & Join Kind | Ep. 46 | Microsoft Power BI Data Analysis Diploma

Hands-on execution of Merge Queries. Demonstrates performing lookups, expanding nested table columns, aggregating merged values, and avoiding cartesian explosions.

**Key Skills & Concepts Covered:**
- ✅ **Table.NestedJoin Execution**
- ✅ **Table.ExpandTableColumn vs Table.AggregateTableColumn**
- ✅ **Selecting Specific Lookup Attributes**
- ✅ **Performance Tuning Merge Steps**

### Part 47: Fuzzy Match | Ep. 47 | Microsoft Power BI Data Analysis Diploma

Fuzzy Matching and Text Clustering in Power Query. Demonstrates merging tables with spelling errors, typos, and abbreviations using similarity thresholds and transformation tables.

**Key Skills & Concepts Covered:**
- ✅ **Fuzzy Matching Algorithms (Jaccard / Levenshtein)**
- ✅ **Similarity Threshold Parameter (0.00 to 1.00)**
- ✅ **Ignore Case & Match by Combining Parts**
- ✅ **Building Custom Transformation Mapping Tables**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

#### Episode 45 Code Reference:

```powerquery
// JoinKind: Inner, LeftOuter, RightOuter, FullOuter, LeftAnti, RightAnti
```

#### Episode 46 Code Reference:

```powerquery
Table.NestedJoin(Sales, {"CustomerID"}, Customers, {"ID"}, "CustomerData", JoinKind.LeftOuter),
#"Expanded" = Table.ExpandTableColumn(#"Merged", "CustomerData", {"CustomerName", "City"})
```

#### Episode 47 Code Reference:

```powerquery
Table.FuzzyNestedJoin(Table1, {"Vendor"}, Table2, {"VendorName"}, "Matched", JoinKind.LeftOuter, [IgnoreCase=true, Threshold=0.8])
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Merge.xlsx`** (`22,819` bytes)

> 💡 **How to use:** Open `.pbix` files in **Microsoft Power BI Desktop**, or open `.xlsx` files in **Microsoft Excel** to inspect the source schemas and practice the transformations step-by-step.

---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep43-44-Append-Queries](../../05-Data-Transformation/Ep43-44-Append-Queries/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep48-Horizontal-Date-Matrix ➡️](../../06-Case-Studies/Ep48-Horizontal-Date-Matrix/README.md)
