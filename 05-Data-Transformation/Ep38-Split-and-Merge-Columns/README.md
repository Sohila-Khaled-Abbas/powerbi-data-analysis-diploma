# Episode 38: Split and Merge Columns

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 38** | Split and Merge Columns | `33m 42s` | [Watch on YouTube](https://www.youtube.com/watch?v=2OR9JHAcxEM) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

Splitting and Merging Columns in Power Query. Explains splitting by delimiter, number of characters, positions, lowercase-to-uppercase transitions, and merging multiple fields.

**Key Skills & Concepts Covered:**
- ✅ **Table.SplitColumn by Delimiter & Position**
- ✅ **Splitting into Rows vs Splitting into Columns**
- ✅ **Text.Combine & Table.CombineColumns**
- ✅ **Handling Variable Delimiter Counts**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.SplitColumn(Source, "FullName", Splitter.SplitTextByDelimiter(" ", ExtraValues.Ignore), {"FirstName", "LastName"})
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

[⬅️ Previous: Ep37-Columns-From-Examples](../../05-Data-Transformation/Ep37-Columns-From-Examples/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep39-Invoke-Custom-Function ➡️](../../05-Data-Transformation/Ep39-Invoke-Custom-Function/README.md)
