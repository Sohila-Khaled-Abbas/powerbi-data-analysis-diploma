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

- 📊 **`Helper Queries.pbix`** (`69.4 KB (71,100 bytes)`) — Power BI Desktop solution model
- 📄 **`Department Folder/Administration.xlsx`** (`19.8 KB (20,266 bytes)`) — Excel practice dataset
- 📄 **`Department Folder/Business Development.xlsx`** (`21.1 KB (21,589 bytes)`) — Excel practice dataset
- 📄 **`Department Folder/Customer Service.xlsx`** (`22.2 KB (22,725 bytes)`) — Excel practice dataset
- 📄 **`Department Folder/Finance.xlsx`** (`22.9 KB (23,479 bytes)`) — Excel practice dataset
- 📄 **`Department Folder/Human Resources.xlsx`** (`21.1 KB (21,571 bytes)`) — Excel practice dataset
- 📄 **`Department Folder/IT.xlsx`** (`21.7 KB (22,187 bytes)`) — Excel practice dataset
- 📄 **`Department Folder/Legal.xlsx`** (`21.1 KB (21,599 bytes)`) — Excel practice dataset
- 📄 **`Helper Queries/Administration.xlsx`** (`14.7 KB (15,061 bytes)`) — Excel practice dataset
- 📄 **`Helper Queries/Business Development.xlsx`** (`21.1 KB (21,589 bytes)`) — Excel practice dataset
- 📄 **`Helper Queries/Customer Service.xlsx`** (`17.2 KB (17,599 bytes)`) — Excel practice dataset
- 📄 **`Helper Queries/Finance.xlsx`** (`22.9 KB (23,479 bytes)`) — Excel practice dataset
- 📄 **`Helper Queries/Human Resources.xlsx`** (`21.1 KB (21,571 bytes)`) — Excel practice dataset
- 📄 **`Helper Queries/IT.xlsx`** (`21.7 KB (22,187 bytes)`) — Excel practice dataset
- 📄 **`Helper Queries/Legal.xlsx`** (`16.1 KB (16,436 bytes)`) — Excel practice dataset

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

[⬅️ Previous: Ep71-Practical-Exercise-3](../../07-Power-Query-Engine-and-M-Language/Ep71-Practical-Exercise-3/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep73-Build-Custom-Functions ➡️](../../07-Power-Query-Engine-and-M-Language/Ep73-Build-Custom-Functions/README.md)
