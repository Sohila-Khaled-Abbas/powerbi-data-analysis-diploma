# Episode 74: Frequency vs. Sequence Analysis

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 74** | Frequency vs. Sequence Analysis | `15m 23s` | [Watch on YouTube](https://www.youtube.com/watch?v=CfpKqBiO8Kg) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1RG09LGg3W60frQHKlZycLTfGzvJ0kp_c/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Frequency vs Sequence Analysis in Power Query. Analyzes event logs, transaction order, customer journeys, and calculating duration between consecutive events.

**Key Skills & Concepts Covered:**
- ✅ **Sorting & Sequential Row Analysis**
- ✅ **Adding Offset Indices to Compare Row N with Row N-1**
- ✅ **Calculating Inter-Event Durations**
- ✅ **Frequency Distribution Analytics**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
#"Indexed" = Table.AddIndexColumn(Source, "Idx", 0, 1),
#"Shifted" = Table.AddIndexColumn(#"Indexed", "IdxNext", 1, 1),
#"SelfJoined" = Table.NestedJoin(#"Indexed", {"IdxNext"}, #"Indexed", {"Idx"}, "PrevRow", JoinKind.LeftOuter)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Frequency vs Sequence Analysis.xlsx`** (`26,482` bytes)

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

[⬅️ Previous: Ep73-Build-Custom-Functions](../../07-Power-Query-Engine-and-M-Language/Ep73-Build-Custom-Functions/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep75-Missing-Fields ➡️](../../07-Power-Query-Engine-and-M-Language/Ep75-Missing-Fields/README.md)
