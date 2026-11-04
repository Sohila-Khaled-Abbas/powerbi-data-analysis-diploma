# Episode 68: Step Error vs. Cell Error | Ep. 68 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 68** | Step Error vs. Cell Error | Ep. 68 | Microsoft Power BI Data Analysis Diploma | `8m 18s` | [Watch on YouTube](https://www.youtube.com/watch?v=NdSx5_WQcz8) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1CcnHY9sxUNkobYEX_GL2RMbIKtKhGqrK/edit?gid=1998078071#gid=1998078071) |

---

## 🎯 Lesson Overview & Objectives

Step Errors vs Cell Errors in Power Query. Teaches the difference between step-level execution failure (stops query) and cell-level evaluation error (single cell error), and how to audit and fix them.

**Key Skills & Concepts Covered:**
- ✅ **Step-level Exceptions vs Cell-level Errors**
- ✅ **Auditing Errors with Table.SelectRowsWithErrors**
- ✅ **Removing or Replacing Cell Errors**
- ✅ **Building Resilient Production Pipelines**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
#"Audited Errors" = Table.SelectRowsWithErrors(Source),
#"Cleaned Errors" = Table.ReplaceErrorValues(Source, {{"Price", 0}})
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Eps 68 - Step Error vs. Cell Error.xlsx`** (`14,425` bytes)
- 📄 **`Step Error vs. Cell Error.pbix`** (`23,450` bytes)

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

[⬅️ Previous: Ep67-Safe-vs-Breaking-Changes](../../07-Power-Query-Engine-and-M-Language/Ep67-Safe-vs-Breaking-Changes/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep69-70-M-Language-Fundamentals ➡️](../../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/README.md)
