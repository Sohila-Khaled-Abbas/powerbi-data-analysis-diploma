# Episode 78: Worksheets Name | Ep. 78 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 78** | Worksheets Name | Ep. 78 | Microsoft Power BI Data Analysis Diploma | `11m 46s` | [Watch on YouTube](https://www.youtube.com/watch?v=uyA9C7m0UYY) | [Download Sample Data](https://drive.google.com/drive/folders/1Z7sVUu5XuWCWP-gEJujWYs8q7GYHd5sa?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Dynamic Excel Worksheets Extraction. Demonstrates dynamically discovering sheet names in an Excel file, filtering out archive or hidden sheets, and consolidating all target sheets automatically.

**Key Skills & Concepts Covered:**
- ✅ **Filtering Excel.Workbook Schema Dynamically**
- ✅ **Selecting Sheets with Dynamic Pattern Matching**
- ✅ **Consolidating Sheets with Divergent Structures**
- ✅ **Automating Monthly Workbook Reports**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = Excel.Workbook(File.Contents("data.xlsx")),
ValidSheets = Table.SelectRows(Source, each [Kind] = "Sheet" and not Text.StartsWith([Item], "Old_")),
Combined = Table.Combine(ValidSheets[Data])
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`HRDatabase.xlsx`** (`14,971` bytes)
- 📄 **`HRDatabase2.xlsx`** (`9,468` bytes)

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

[⬅️ Previous: Ep77-The-Logic-of-Thinking](../../07-Power-Query-Engine-and-M-Language/Ep77-The-Logic-of-Thinking/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep79-Transform-All-Columns ➡️](../../07-Power-Query-Engine-and-M-Language/Ep79-Transform-All-Columns/README.md)
