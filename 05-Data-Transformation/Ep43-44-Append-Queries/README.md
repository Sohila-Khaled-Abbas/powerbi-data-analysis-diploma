# Episodes 43 - 44: Append (Theory) | Ep. 43 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 43** | Append (Theory) | Ep. 43 | Microsoft Power BI Data Analysis Diploma | `10m 26s` | [Watch on YouTube](https://www.youtube.com/watch?v=TGqI6xxEO28) | Included in repo / Follow lecture |
| **Ep. 44** | Append | Ep. 44 | Microsoft Power BI Data Analysis Diploma | `27m 45s` | [Watch on YouTube](https://www.youtube.com/watch?v=kqTcg-j5bk4) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1_hWdLDXrnIIEjyUfiFntNA9LQhuJPZyi/edit?usp=sharing&ouid=107970738919672012073&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

### Part 43: Append (Theory) | Ep. 43 | Microsoft Power BI Data Analysis Diploma

Theoretical foundation of Append Queries. Explains vertical table stacking, column matching by name (case-sensitive), handling missing columns, and schema unification.

**Key Skills & Concepts Covered:**
- ✅ **Table.Combine Theory**
- ✅ **Case Sensitivity in Column Names**
- ✅ **Handling Column Position Independence**
- ✅ **Schema Drift in Appended Tables**

### Part 44: Append | Ep. 44 | Microsoft Power BI Data Analysis Diploma

Practical execution of Append Queries. Demonstrates consolidating multiple operational tables, reconciling disparate schemas, and optimizing refresh times.

**Key Skills & Concepts Covered:**
- ✅ **Appending 2 or More Tables**
- ✅ **Resolving Schema Discrepancies**
- ✅ **Disabling 'Enable Load' for Intermediate Staging Tables**
- ✅ **Verifying Combined Row Counts**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

#### Episode 43 Code Reference:

```powerquery
// Table.Combine stacks tables vertically by matching exact column names
```

#### Episode 44 Code Reference:

```powerquery
Table.Combine({Sales2021, Sales2022, Sales2023})
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Append Eps44.xlsx`** (`17,342,011` bytes)
- 📄 **`append.pbix`** (`5,162,335` bytes)

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

[⬅️ Previous: Ep42-Double-Headers-Issue](../../05-Data-Transformation/Ep42-Double-Headers-Issue/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep45-47-Merge-and-Fuzzy-Match ➡️](../../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/README.md)
