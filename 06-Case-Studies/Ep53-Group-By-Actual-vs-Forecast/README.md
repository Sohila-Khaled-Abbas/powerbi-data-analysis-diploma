# Episode 53: Group By (Actual vs Forecast)

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 53** | Group By (Actual vs Forecast) | `22m 30s` | [Watch on YouTube](https://www.youtube.com/watch?v=dUu93A6t5gM) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1MuJ9EZnB-zKUMS8No5qQ_oJzcSFFg-tK/edit?usp=sharing&ouid=107970738919672012073&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Real-World Case Study: Group By (Actual vs Forecast). Demonstrates aggregating high-volume operational actuals and joining with forward-looking sales forecasts.

**Key Skills & Concepts Covered:**
- ✅ **Table.Group for Multi-Column Aggregation**
- ✅ **Consolidating Sales Rep Forecasts**
- ✅ **Calculating Weighted Averages in Power Query**
- ✅ **Preparing Executive Variance Tables**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.Group(Source, {"SalesRep", "Region"}, {{"TotalActual", each List.Sum([Sales]), type number}})
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📊 **`Group By (Actual vs Forecast).pbix`** (`24.9 KB (25,469 bytes)`) — Power BI Desktop solution model
- 📄 **`SalesRep Actual VS Forecast.xlsx`** (`30.6 KB (31,366 bytes)`) — Excel practice dataset

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

[⬅️ Previous: Ep52-Monthly-Sales-Actual-vs-Budget](../../06-Case-Studies/Ep52-Monthly-Sales-Actual-vs-Budget/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep54-Complex-Header-Structure ➡️](../../06-Case-Studies/Ep54-Complex-Header-Structure/README.md)
