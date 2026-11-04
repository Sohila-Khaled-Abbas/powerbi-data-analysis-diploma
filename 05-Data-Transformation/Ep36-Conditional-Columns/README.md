# Episode 36: Conditional Columns | Ep. 36 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 36** | Conditional Columns | Ep. 36 | Microsoft Power BI Data Analysis Diploma | `24m 7s` | [Watch on YouTube](https://www.youtube.com/watch?v=s97vRdiyEdE) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

Building Conditional Columns in Power Query. Explains multi-branch IF-THEN-ELSE logic, nested conditions, boundary evaluation, and categorizing metrics.

**Key Skills & Concepts Covered:**
- ✅ **Power Query Conditional Column Builder**
- ✅ **Multi-condition Logic (if ... then ... else)**
- ✅ **Handling Boundary Values & Nulls**
- ✅ **Creating Analytical Buckets & Bands**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.AddColumn(Source, "Tier", each if [Sales] > 100000 then "Platinum" else if [Sales] > 50000 then "Gold" else "Silver")
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

[⬅️ Previous: Ep35-Custom-Columns](../../05-Data-Transformation/Ep35-Custom-Columns/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep37-Columns-From-Examples ➡️](../../05-Data-Transformation/Ep37-Columns-From-Examples/README.md)
