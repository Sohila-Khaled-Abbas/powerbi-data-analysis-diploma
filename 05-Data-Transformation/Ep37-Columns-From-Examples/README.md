# Episode 37: Columns from Examples | Ep. 37 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 37** | Columns from Examples | Ep. 37 | Microsoft Power BI Data Analysis Diploma | `16m 1s` | [Watch on YouTube](https://www.youtube.com/watch?v=t6JwFr04Aj4) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

Generating Columns from Examples. Explains how Power Query's AI pattern matching infers transformation rules from user examples and generates underlying M expressions.

**Key Skills & Concepts Covered:**
- ✅ **Column From Examples Feature**
- ✅ **Pattern Inference Engine**
- ✅ **Text Extraction & Concatenation Patterns**
- ✅ **Inspecting Auto-generated M Expressions**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
// Auto-generated example:
Table.AddColumn(Source, "Initials", each Text.Combine(List.Transform(Text.Split([Name], " "), each Text.Start(_, 1))))
```

---

## 📁 Practice Files in this Repository

No local binary dataset files are stored in this folder. You can use the official sample data link from the video description above, or practice directly inside Power BI Desktop following the video walkthrough.

---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep36-Conditional-Columns](../../05-Data-Transformation/Ep36-Conditional-Columns/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep38-Split-and-Merge-Columns ➡️](../../05-Data-Transformation/Ep38-Split-and-Merge-Columns/README.md)
