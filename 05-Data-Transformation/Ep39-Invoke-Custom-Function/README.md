# Episode 39: Invoke Custom Function

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 39** | Invoke Custom Function | `26m 54s` | [Watch on YouTube](https://www.youtube.com/watch?v=8uAhgo19hxQ) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

Invoking Custom Functions across table rows. Explains creating parameterized M functions and applying them iteratively to each record in a dataset.

**Key Skills & Concepts Covered:**
- ✅ **Table.AddColumn with Custom Function Calls**
- ✅ **Creating Reusable Transformation Functions**
- ✅ **Passing Multiple Column Arguments**
- ✅ **Performance Optimization for Row Functions**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.AddColumn(Source, "CleanedPhone", each FormatPhone([RawPhone]))
```

---

## 📁 Practice Files in this Repository

- *Included with the lecture instructions / no local dataset required.*
---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep38-Split-and-Merge-Columns](../../05-Data-Transformation/Ep38-Split-and-Merge-Columns/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep40-41-Unpivot-and-Pivot-Columns ➡️](../../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/README.md)
