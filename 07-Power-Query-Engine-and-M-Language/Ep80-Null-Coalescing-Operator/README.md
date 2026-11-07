# Episode 80: Null Coalescing Operator

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 80** | Null Coalescing Operator | `9m 17s` | [Watch on YouTube](https://www.youtube.com/watch?v=Tf7yCfw9TeA) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1h9TgU98uAohxtM3oss8usbNg2oL09F7z/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Mastering the Null Coalescing Operator (??). Teaches concise fallback logic to replace null values with default expressions in M expressions.

**Key Skills & Concepts Covered:**
- ✅ **Null Coalescing Operator (??) Syntax**
- ✅ **Chaining Fallback Defaults (a ?? b ?? c)**
- ✅ **Simplifying Nested If-Then-Else Null Checks**
- ✅ **Writing Clean, Readable M Code**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
// Cleaner than: if [Discount] <> null then [Discount] else 0
[Discount] ?? 0
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Null Coalescing Operator.xlsx`** (`11,888` bytes)

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

[⬅️ Previous: Ep79-Transform-All-Columns](../../07-Power-Query-Engine-and-M-Language/Ep79-Transform-All-Columns/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep81-Try-and-Otherwise ➡️](../../07-Power-Query-Engine-and-M-Language/Ep81-Try-and-Otherwise/README.md)
