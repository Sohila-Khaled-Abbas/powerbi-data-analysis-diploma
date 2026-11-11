# Episodes 40 - 41: UnPivot Columns

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 40** | UnPivot Columns | `21m 54s` | [Watch on YouTube](https://www.youtube.com/watch?v=Y2FpX7VS73g) | [Download Sample Data](https://docs.google.com/spreadsheets/d/19dxijDLYslNs31k91lsvSEsJW4CB6tB4/edit?usp=sharing&ouid=107970738919672012073&rtpof=true&sd=true) |
| **Ep. 41** | Pivot Columns | `10m 53s` | [Watch on YouTube](https://www.youtube.com/watch?v=SsMiqmbTLFM) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

### Part 40: UnPivot Columns | Ep. 40 | Microsoft Power BI Data Analysis Diploma

Unpivoting Columns: The most critical transformation in Power Query. Explains transforming horizontal summary reports (matrix headers) into normalized vertical datasets.

**Key Skills & Concepts Covered:**
- ✅ **Table.UnpivotOtherColumns Best Practice**
- ✅ **Unpivot Selected Columns vs Unpivot Other Columns**
- ✅ **Handling Dynamic New Columns (Schema Resiliency)**
- ✅ **Normalizing Cross-Tabular Reports**

### Part 41: Pivot Columns | Ep. 41 | Microsoft Power BI Data Analysis Diploma

Pivoting Columns in Power Query. Demonstrates turning unique row values into column headers and aggregating intersecting numeric metrics.

**Key Skills & Concepts Covered:**
- ✅ **Table.Pivot Function**
- ✅ **Aggregating Metrics (Sum, Count, Average, Don't Aggregate)**
- ✅ **Matrix Construction in ETL**
- ✅ **Solving Pivoting Errors with Duplicate Keys**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

#### Episode 40 Code Reference:

```powerquery
Table.UnpivotOtherColumns(Source, {"CategoryID", "CategoryName"}, "Month", "SalesValue")
```

#### Episode 41 Code Reference:

```powerquery
Table.Pivot(Source, List.Distinct(Source[Metric]), "Metric", "Value", List.Sum)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Unpivot & Pivot Columns.xlsx`** (`31.1 KB (31,842 bytes)`) — Excel practice dataset
- 📊 **`unpivot.pbix`** (`100.1 KB (102,480 bytes)`) — Power BI Desktop solution model

> 💡 **How to use:** Open `.pbix` files in **Microsoft Power BI Desktop**; and Open `.xlsx` files in **Microsoft Excel** to inspect source tables, verify data types, and follow along with the transformations.
---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep39-Invoke-Custom-Function](../../05-Data-Transformation/Ep39-Invoke-Custom-Function/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep42-Double-Headers-Issue ➡️](../../05-Data-Transformation/Ep42-Double-Headers-Issue/README.md)
