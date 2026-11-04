# Episode 61: Vertical Headers Structure | Case Study | Ep. 61 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 61** | Vertical Headers Structure | Case Study | Ep. 61 | Microsoft Power BI Data Analysis Diploma | `20m 37s` | [Watch on YouTube](https://www.youtube.com/watch?v=c5Ja8xUZmEY) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1iIbqiFkiWTfUcoH4nS4URRRLG7vNFNTE/edit?gid=1207873951#gid=1207873951) |

---

## 🎯 Lesson Overview & Objectives

Real-World Case Study: Vertical Headers Structure. Solves datasets where metrics and metadata are presented vertically down rows rather than across columns.

**Key Skills & Concepts Covered:**
- ✅ **Vertical to Horizontal Reshaping**
- ✅ **Record Construction from Vertical Pairs**
- ✅ **Table.FromRows and Table.FromRecords**
- ✅ **Normalizing Vertical Financial Statements**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.Pivot(Source, List.Distinct(Source[Attribute]), "Attribute", "Value")
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Vertical Header Structure.xlsx`** (`12,699` bytes)
- 📄 **`Vertical Headers Structure.pbix`** (`23,224` bytes)

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

[⬅️ Previous: Ep60-Locale-Dates-vs-Numbers](../../06-Case-Studies/Ep60-Locale-Dates-vs-Numbers/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep62-Practical-Exercise-1 ➡️](../../06-Case-Studies/Ep62-Practical-Exercise-1/README.md)
