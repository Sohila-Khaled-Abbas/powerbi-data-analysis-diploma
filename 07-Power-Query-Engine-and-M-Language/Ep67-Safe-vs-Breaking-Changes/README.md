# Episode 67: Safe vs. Breaking Changes | Ep. 67 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 67** | Safe vs. Breaking Changes | Ep. 67 | Microsoft Power BI Data Analysis Diploma | `25m 21s` | [Watch on YouTube](https://www.youtube.com/watch?v=g4b3S3rLQr8) | [Download Sample Data](https://drive.google.com/drive/folders/1IQYx_NGw08X73OkgYzFmhK5EsP5ONvKr) |

---

## 🎯 Lesson Overview & Objectives

Safe vs Breaking Changes in Power Query. Explains Query Folding preservation, preventing schema breakage when upstream source columns change, and writing resilient M code.

**Key Skills & Concepts Covered:**
- ✅ **Safe Transformation Steps vs Breaking Changes**
- ✅ **Maintaining Query Folding to SQL Engines**
- ✅ **Mitigating Schema Drift Impact**
- ✅ **Enterprise Pipeline Maintenance Best Practices**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
// Safe changes preserve Query Folding (Table.SelectRows, Table.Filter)
// Breaking changes force local engine evaluation (Table.Buffer, custom M loops)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Safe vs. Breaking Changes.pbix`** (`58,206` bytes)
- 📄 **`Safe vs. Breaking Changes.xlsx`** (`72,469` bytes)
- 📄 **`Very Important Notes.pdf`** (`56,960` bytes)

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

[⬅️ Previous: Ep66-Cartesian-Join](../../07-Power-Query-Engine-and-M-Language/Ep66-Cartesian-Join/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep68-Step-Error-vs-Cell-Error ➡️](../../07-Power-Query-Engine-and-M-Language/Ep68-Step-Error-vs-Cell-Error/README.md)
