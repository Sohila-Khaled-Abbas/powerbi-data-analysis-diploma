# Episode 60: Locale (Dates vs. Numbers)

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 60** | Locale (Dates vs. Numbers) | `12m 31s` | [Watch on YouTube](https://www.youtube.com/watch?v=NwneSCZVndk) | [Download Sample Data](https://drive.google.com/file/d/188cd3l6tXUVKO9Ese2Zs2Av3G_uYhSzq/view?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Real-World Case Study: Locale (Dates vs Numbers) Edge Cases. Deep troubleshooting of corrupt imports where dates and monetary figures use opposing regional conventions in the same file.

**Key Skills & Concepts Covered:**
- ✅ **Isolating Column-Specific Locales**
- ✅ **Handling Mixed Regional Formats**
- ✅ **Culture Tags ('en-US', 'en-GB', 'fr-FR')**
- ✅ **Data Sanitization Before Type Casting**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.TransformColumnTypes(Source, {{"US_Date", type date}}, "en-US"),
Table.TransformColumnTypes(Source, {{"EU_Amount", type number}}, "de-DE")
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📋 **`DatesCSV 23Aug26.csv`** (`46.0 KB (47,091 bytes)`) — CSV data file
- 📊 **`Locale (Dates vs. Numbers).pbix`** (`56.0 KB (57,303 bytes)`) — Power BI Desktop solution model

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

[⬅️ Previous: Ep59-Context-vs-Logic](../../06-Case-Studies/Ep59-Context-vs-Logic/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep61-Vertical-Headers-Structure ➡️](../../06-Case-Studies/Ep61-Vertical-Headers-Structure/README.md)
