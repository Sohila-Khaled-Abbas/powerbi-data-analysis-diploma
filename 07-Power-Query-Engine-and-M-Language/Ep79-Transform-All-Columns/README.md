# Episode 79: Transform All Columns | Ep. 79 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 79** | Transform All Columns | Ep. 79 | Microsoft Power BI Data Analysis Diploma | `13m 43s` | [Watch on YouTube](https://www.youtube.com/watch?v=lNIszvvtH20) | [Download Sample Data](https://docs.google.com/spreadsheets/d/17x2adhYI77emsOD1O2lXztQ8JPgoqNL6/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Transform All Columns Dynamically using Table.TransformColumns. Shows how to trim whitespace, lowercase text, or clean numbers across every column without writing repetitive steps.

**Key Skills & Concepts Covered:**
- ✅ **Table.TransformColumns Advanced Usage**
- ✅ **List.Transform Over Table.ColumnNames**
- ✅ **Applying Bulk Cleaning Operations Across All Columns**
- ✅ **Dynamic Type Sanitization**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
ColNames = Table.ColumnNames(Source),
TransformList = List.Transform(ColNames, each {_, Text.Trim}),
CleanedTable = Table.TransformColumns(Source, TransformList)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Transform All Columns.xlsx`** (`145,063` bytes)

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

[⬅️ Previous: Ep78-Worksheets-Name](../../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep80-Null-Coalescing-Operator ➡️](../../07-Power-Query-Engine-and-M-Language/Ep80-Null-Coalescing-Operator/README.md)
