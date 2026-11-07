# Episode 65: Null vs. Blank – Full Explanation

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 65** | Null vs. Blank – Full Explanation | `16m 58s` | [Watch on YouTube](https://www.youtube.com/watch?v=wlSBLPL50rM) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

Engine Deep Dive: Null vs Blank. Comprehensive technical explanation of how Power Query treats 'null' (absence of value) vs blank string ("") vs DAX BLANK() in the engine.

**Key Skills & Concepts Covered:**
- ✅ **Power Query 'null' vs Empty String '""'**
- ✅ **Engine Comparison Semantics (null = null is true)**
- ✅ **DAX BLANK() vs M 'null' Interoperability**
- ✅ **Safe Null Handling Techniques**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
// In M:
// null = absence of any value
// "" = text string of length 0
// To replace: Table.ReplaceValue(Source, "", null, Replacer.ReplaceValue, {"Col"})
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Null vs Blank.pbix`** (`28,747` bytes)
- 📄 **`Test.xlsx`** (`9,429` bytes)

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

[⬅️ Previous: Ep64-Multi-Bank-PDF-Consolidation](../../06-Case-Studies/Ep64-Multi-Bank-PDF-Consolidation/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep66-Cartesian-Join ➡️](../../07-Power-Query-Engine-and-M-Language/Ep66-Cartesian-Join/README.md)
