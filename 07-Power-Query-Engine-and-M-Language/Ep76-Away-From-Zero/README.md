# Episode 76: Away From Zero | Ep. 76 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 76** | Away From Zero | Ep. 76 | Microsoft Power BI Data Analysis Diploma | `10m 4s` | [Watch on YouTube](https://www.youtube.com/watch?v=o2uAwvLCRmY) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1oLnk44t2QSLCh6qFQWdLrK2xlFoLx8YH/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

'Away From Zero' & Custom Analytical Logic Patterns. Explains IEEE floating-point arithmetic quirks, rounding strategies (Round AwayFromZero vs Round ToEven), and business rounding compliance.

**Key Skills & Concepts Covered:**
- ✅ **Number.Round with RoundingMode.AwayFromZero**
- ✅ **Banker's Rounding (RoundingMode.ToEven) vs Commercial Rounding**
- ✅ **Financial Compliance in Metric Calculations**
- ✅ **Precision & Floating-point Gotchas**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Number.Round(2.5, 0, RoundingMode.AwayFromZero) // Returns 3
Number.Round(2.5, 0, RoundingMode.ToEven)       // Returns 2 (Banker's Rounding)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Away From Zero.xlsx`** (`10,600` bytes)

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

[⬅️ Previous: Ep75-Missing-Fields](../../07-Power-Query-Engine-and-M-Language/Ep75-Missing-Fields/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep77-The-Logic-of-Thinking ➡️](../../07-Power-Query-Engine-and-M-Language/Ep77-The-Logic-of-Thinking/README.md)
