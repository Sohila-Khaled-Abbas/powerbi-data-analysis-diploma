# Episode 48: Horizontal Date Matrix

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 48** | Horizontal Date Matrix | `17m 56s` | [Watch on YouTube](https://www.youtube.com/watch?v=DFCk5VfYmf0) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1pPrz3pW14yRopHyD3YdOvjExma3i2pBD/edit?usp=sharing&ouid=107970738919672012073&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Real-World Case Study: Transforming a Horizontal Date Matrix. Solves a classic enterprise data challenge where dates are spread horizontally across 100+ columns with blank gaps.

**Key Skills & Concepts Covered:**
- ✅ **Extracting Date Headers from Rows**
- ✅ **Unpivoting Large Dynamic Date Matrices**
- ✅ **Handling Irregular Date Headers**
- ✅ **Creating Standard Fact Tables**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
#"Unpivoted Dates" = Table.UnpivotOtherColumns(Source, {"Account", "CostCenter"}, "DateString", "Amount")
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Horizontal Date Matrix Case.xlsx`** (`24.1 KB (24,698 bytes)`) — Excel practice dataset
- 📊 **`Horizontal Date Matrix.pbix`** (`23.0 KB (23,540 bytes)`) — Power BI Desktop solution model

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

[⬅️ Previous: Ep45-47-Merge-and-Fuzzy-Match](../../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep49-Fragmented-Rows ➡️](../../06-Case-Studies/Ep49-Fragmented-Rows/README.md)
