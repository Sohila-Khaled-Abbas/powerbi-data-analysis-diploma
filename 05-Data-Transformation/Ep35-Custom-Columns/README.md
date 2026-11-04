# Episode 35: Custom Columns | Ep. 35 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 35** | Custom Columns | Ep. 35 | Microsoft Power BI Data Analysis Diploma | `29m 15s` | [Watch on YouTube](https://www.youtube.com/watch?v=wzDHUwIVT_I) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1b7VSsw7VT5YYqML7oA_hgG1IbR1RZT7Z/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Creating Custom Columns in Power Query using M Language expressions. Covers arithmetic calculations, string formatting, date differences, and conditional evaluation.

**Key Skills & Concepts Covered:**
- ✅ **Table.AddColumn Architecture**
- ✅ **Syntax of Custom Column Expressions**
- ✅ **Working with Record Context (each keyword)**
- ✅ **Optimizing Custom Column Calculations**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.AddColumn(Source, "Profit", each [Revenue] - [Cost], Currency.Type)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Custom CL.pbix`** (`6,491,035` bytes)

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

[⬅️ Previous: Ep34-Local-Interpretation](../../05-Data-Transformation/Ep34-Local-Interpretation/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep36-Conditional-Columns ➡️](../../05-Data-Transformation/Ep36-Conditional-Columns/README.md)
