# Episode 49: Fragmented Rows

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 49** | Fragmented Rows | `12m 41s` | [Watch on YouTube](https://www.youtube.com/watch?v=j2lfBaQoe-w) | [Download Sample Data](https://docs.google.com/spreadsheets/d/11EH1eoy1tlAoqxJ1JARN40OW9xWtJiwA/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Real-World Case Study: Restructuring Fragmented Rows. Demonstrates repairing corrupted exports where single transactions are broken across multiple alternating rows.

**Key Skills & Concepts Covered:**
- ✅ **Identifying Row Alternation Patterns**
- ✅ **Index Columns (Modulo & Integer-Divide)**
- ✅ **Splitting and Re-joining Fragmented Records**
- ✅ **Table Reconstruction Workflows**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.AddColumn(Source, "GroupIndex", each Number.IntegerDivide([Index], 2))
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Fragmented Rows Case.xlsx`** (`12.5 KB (12,796 bytes)`) — Excel practice dataset
- 📊 **`Fragmented Rows.pbix`** (`20.9 KB (21,399 bytes)`) — Power BI Desktop solution model

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

[⬅️ Previous: Ep48-Horizontal-Date-Matrix](../../06-Case-Studies/Ep48-Horizontal-Date-Matrix/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep50-GDP-Database ➡️](../../06-Case-Studies/Ep50-GDP-Database/README.md)
