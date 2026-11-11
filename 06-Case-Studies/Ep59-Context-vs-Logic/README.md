# Episode 59: Context vs Logic

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 59** | Context vs Logic | `14m 2s` | [Watch on YouTube](https://www.youtube.com/watch?v=WOkfAwiBwLY) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1R3wJ3G4olGDGQI1k3vsrZN6xa0iTsmDq/edit?gid=39706116#gid=39706116) |

---

## 🎯 Lesson Overview & Objectives

Real-World Case Study: Context vs Logic. Explains evaluating calculations within the proper evaluation context, understanding row context vs query context in Power Query.

**Key Skills & Concepts Covered:**
- ✅ **Evaluation Context in M Language**
- ✅ **Row-by-Row Evaluation vs Table-level Evaluation**
- ✅ **Passing Contextual Variables in Nested Expressions**
- ✅ **Avoiding Ambiguous Column References**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.AddColumn(Source, "RelativePercent", (r) => r[Sales] / Table.Column(Source, "TotalSales"){0})
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📊 **`Context vs Logic (Case Study).pbix`** (`43.9 KB (44,984 bytes)`) — Power BI Desktop solution model

> 💡 **How to use:** Open `.pbix` files in **Microsoft Power BI Desktop**.
---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep58-Hardcode-vs-Logic](../../06-Case-Studies/Ep58-Hardcode-vs-Logic/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep60-Locale-Dates-vs-Numbers ➡️](../../06-Case-Studies/Ep60-Locale-Dates-vs-Numbers/README.md)
