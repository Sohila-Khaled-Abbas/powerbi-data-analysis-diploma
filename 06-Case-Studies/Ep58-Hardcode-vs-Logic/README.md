# Episode 58: Hardcode vs Logic

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 58** | Hardcode vs Logic | `16m 57s` | [Watch on YouTube](https://www.youtube.com/watch?v=xus1508g4Pw) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1R3wJ3G4olGDGQI1k3vsrZN6xa0iTsmDq/edit?gid=39706116#gid=39706116) |

---

## 🎯 Lesson Overview & Objectives

Real-World Case Study: Hardcode vs Logic. Demonstrates replacing brittle hardcoded values and column names with dynamic M logic that adapts to schema evolution.

**Key Skills & Concepts Covered:**
- ✅ **Dynamic Column Name Referencing**
- ✅ **Table.ColumnNames Inspection**
- ✅ **Eliminating Brittle Hardcoded Constants**
- ✅ **Writing Future-Proof Power Query Scripts**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
ColumnList = Table.ColumnNames(Source),
DynamicColumns = List.Select(ColumnList, each Text.StartsWith(_, "20"))
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Hardcode vs Logic.xlsx`** (`14,581` bytes)

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

[⬅️ Previous: Ep57-Inconsistent-Data-Sources](../../06-Case-Studies/Ep57-Inconsistent-Data-Sources/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep59-Context-vs-Logic ➡️](../../06-Case-Studies/Ep59-Context-vs-Logic/README.md)
