# Episode 50: GDP Database | Case Study | Ep. 50 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 50** | GDP Database | Case Study | Ep. 50 | Microsoft Power BI Data Analysis Diploma | `11m 5s` | [Watch on YouTube](https://www.youtube.com/watch?v=eb4cz-Z6BMA) | [Download Sample Data](https://drive.google.com/file/d/1pSWxQ0x_6w5z_N0iibXn99ND3dfrUXrZ/view?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Real-World Case Study: GDP Database Normalization. Cleans an international tabular database of global economic indicators spanning 50+ years across 200+ nations.

**Key Skills & Concepts Covered:**
- ✅ **Filtering Metadata Text & Notes**
- ✅ **Normalizing Multi-Year Time Series Data**
- ✅ **Handling Missing & 'no data' Strings**
- ✅ **Structuring Global Macroeconomic Datasets**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.SelectRows(Source, each [Country] <> "" and [Country] <> "Notes")
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`GDP Database.txt`** (`67,555` bytes)

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

[⬅️ Previous: Ep49-Fragmented-Rows](../../06-Case-Studies/Ep49-Fragmented-Rows/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep51-Fragmented-Duplicate-and-Merge ➡️](../../06-Case-Studies/Ep51-Fragmented-Duplicate-and-Merge/README.md)
