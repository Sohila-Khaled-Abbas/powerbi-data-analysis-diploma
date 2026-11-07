# Episode 42: Double Headers Issue

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 42** | Double Headers Issue | `15m 7s` | [Watch on YouTube](https://www.youtube.com/watch?v=218KtXG4GVY) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

Resolving Double Headers and Multi-tier Column Headers. Demonstrates transposing, filling down, combining rows, and promoting clean composite headers.

**Key Skills & Concepts Covered:**
- ✅ **Transposing Tables (Table.Transpose)**
- ✅ **Fill Down Logic across Multi-level Headers**
- ✅ **Merging Header Rows with Delimiters**
- ✅ **Promoting Headers (Table.PromoteHeaders)**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
#"Transposed" = Table.Transpose(Source),
#"Filled Down" = Table.FillDown(#"Transposed", {"Column1"}),
#"Merged" = Table.CombineColumns(#"Filled Down", {"Column1", "Column2"}, Combiner.CombineTextByDelimiter("_"), "Header"),
#"Clean" = Table.PromoteHeaders(Table.Transpose(#"Merged"))
```

---

## 📁 Practice Files in this Repository

No local binary dataset files are stored in this folder. You can use the official sample data link from the video description above, or practice directly inside Power BI Desktop following the video walkthrough.

---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep40-41-Unpivot-and-Pivot-Columns](../../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep43-44-Append-Queries ➡️](../../05-Data-Transformation/Ep43-44-Append-Queries/README.md)
