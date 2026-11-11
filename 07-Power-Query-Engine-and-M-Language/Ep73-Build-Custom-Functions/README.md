# Episode 73: Build Custom Functions

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 73** | Build Custom Functions | `19m 1s` | [Watch on YouTube](https://www.youtube.com/watch?v=IpBJqY3zctE) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1iEJblGG-g1TSAq6L9AmCoqYe1i49JTJo/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Building Custom Reusable Functions in M. Teaches writing modular functions with typed parameters, optional arguments, and documentation metadata.

**Key Skills & Concepts Covered:**
- ✅ **Writing Typed M Functions ((x as text, optional y as number) as text =>)**
- ✅ **Parameter Types & Type Checking**
- ✅ **Adding Function Documentation (Type.Function)**
- ✅ **Deploying Functions Across Workspaces**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
(dateVal as date, optional fiscalStartMonth as number) as text =>
let
    fMonth = if fiscalStartMonth = null then 1 else fiscalStartMonth,
    m = Date.Month(dateVal),
    fy = if m >= fMonth then Date.Year(dateVal) + 1 else Date.Year(dateVal)
in
    "FY" & Text.End(Text.From(fy), 2)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📊 **`Build Custom Functions.pbix`** (`37.8 KB (38,722 bytes)`) — Power BI Desktop solution model
- 📄 **`Ep. 73.xlsx`** (`15.4 KB (15,781 bytes)`) — Excel practice dataset

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

[⬅️ Previous: Ep72-Helper-Queries](../../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep74-Frequency-vs-Sequence-Analysis ➡️](../../07-Power-Query-Engine-and-M-Language/Ep74-Frequency-vs-Sequence-Analysis/README.md)
