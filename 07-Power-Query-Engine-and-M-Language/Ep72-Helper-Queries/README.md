# Episode 72: Helper Queries

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 72** | Helper Queries | `16m 32s` | [Watch on YouTube](https://www.youtube.com/watch?v=ESZie6P1VxA) | [Download Sample Data](https://drive.google.com/drive/folders/1OPwJ6BQ2JjcR9KWb5-eqOiLiXLcDBqn1?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Architecting Helper Queries in Power Query. Demonstrates decomposing monolithic queries into modular helper queries, staging tables, parameters, and shared lookups.

**Key Skills & Concepts Covered:**
- ✅ **Modular ETL Pipeline Architecture**
- ✅ **Decoupling Ingestion from Transformation**
- ✅ **Disabling 'Enable Load' for Intermediate Helper Queries**
- ✅ **Improving Maintainability and Debugging Speed**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
// Query Organization:
// - Parameters
// - Staging / Helper Queries (Enable Load = False)
// - Production Fact & Dimension Queries (Enable Load = True)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📂 **`Department Folder/`** (Directory containing 7 dataset files)
- 📂 **`Helper Queries/`** (Directory containing 7 dataset files)
- 📄 **`Helper Queries.pbix`** (`71,100` bytes)

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

[⬅️ Previous: Ep71-Practical-Exercise-3](../../07-Power-Query-Engine-and-M-Language/Ep71-Practical-Exercise-3/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep73-Build-Custom-Functions ➡️](../../07-Power-Query-Engine-and-M-Language/Ep73-Build-Custom-Functions/README.md)
