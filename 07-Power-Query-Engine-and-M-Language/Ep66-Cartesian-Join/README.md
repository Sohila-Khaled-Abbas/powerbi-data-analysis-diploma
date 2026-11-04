# Episode 66: Cartesian Join | Ep. 66 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 66** | Cartesian Join | Ep. 66 | Microsoft Power BI Data Analysis Diploma | `12m 1s` | [Watch on YouTube](https://www.youtube.com/watch?v=RFDEx47xQa0) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1sB34uqMVhycmQ1xb7NlFuTUajHVR0Zje/edit?gid=1957227644#gid=1957227644) |

---

## 🎯 Lesson Overview & Objectives

Mastering Cartesian Joins (Cross Joins). Explains when cartesian products are useful (e.g. generating complete scenario matrices) and how to avoid accidental memory crashes.

**Key Skills & Concepts Covered:**
- ✅ **Cartesian Product Concepts**
- ✅ **Table.AddColumn with Table Reference**
- ✅ **Generating Matrix Combinations (All Dates x All Products)**
- ✅ **Preventing Accidental Row Explosions**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.AddColumn(TableA, "Custom", each TableB),
#"Expanded" = Table.ExpandTableColumn(#"Added", "Custom", Table.ColumnNames(TableB))
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Cartesian Join.pbix`** (`27,906` bytes)
- 📄 **`Cartesian Join.xlsx`** (`16,069` bytes)

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

[⬅️ Previous: Ep65-Null-vs-Blank](../../07-Power-Query-Engine-and-M-Language/Ep65-Null-vs-Blank/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep67-Safe-vs-Breaking-Changes ➡️](../../07-Power-Query-Engine-and-M-Language/Ep67-Safe-vs-Breaking-Changes/README.md)
