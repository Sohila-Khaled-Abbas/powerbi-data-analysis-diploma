# Episode 51: Fragmented, Duplicate & Merge

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 51** | Fragmented, Duplicate & Merge | `9m 54s` | [Watch on YouTube](https://www.youtube.com/watch?v=FecDKZfggWg) | [Download Sample Data](https://docs.google.com/spreadsheets/d/15QhhgIBUsmb-57FZKiKgxDZgUk-hfim9/edit?usp=sharing&ouid=107970738919672012073&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Real-World Case Study: Fragmented, Duplicate & Merge. Advanced end-to-end challenge reconciling fragmented records, deduplicating complex keys, and merging lookup dimensions.

**Key Skills & Concepts Covered:**
- ✅ **Multi-column Deduplication Logic**
- ✅ **Resolving Conflicting Duplicate Records**
- ✅ **Cascading Merge Operations**
- ✅ **Validating Clean Relational Tables**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.Distinct(Source, {"TransactionID", "Date"})
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📊 **`Fragmented Duplicate & Merge.pbix`** (`21.6 KB (22,111 bytes)`) — Power BI Desktop solution model
- 📄 **`Fragmented Duplicate & Merge.xlsx`** (`9.4 KB (9,671 bytes)`) — Excel practice dataset

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

[⬅️ Previous: Ep50-GDP-Database](../../06-Case-Studies/Ep50-GDP-Database/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep52-Monthly-Sales-Actual-vs-Budget ➡️](../../06-Case-Studies/Ep52-Monthly-Sales-Actual-vs-Budget/README.md)
