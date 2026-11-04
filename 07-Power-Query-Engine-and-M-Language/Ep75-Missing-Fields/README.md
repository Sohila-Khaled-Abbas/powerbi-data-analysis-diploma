# Episode 75: Missing Fields | Ep. 75 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 75** | Missing Fields | Ep. 75 | Microsoft Power BI Data Analysis Diploma | `11m 35s` | [Watch on YouTube](https://www.youtube.com/watch?v=Yc8WkhRb60U) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1Mbg4Q5f3dsaGUzJk_yv-7gWaFcSp469J/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Handling Missing Fields dynamically with MissingField enumeration. Prevents pipeline failure when optional fields are absent in incoming payloads.

**Key Skills & Concepts Covered:**
- ✅ **MissingField.Error vs MissingField.Ignore vs MissingField.UseNull**
- ✅ **Dynamic Record Field Extraction**
- ✅ **Handling Schema Evolution Without Pipeline Failure**
- ✅ **Resilient API & JSON Ingestion**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Record.FieldOrDefault(rec, "OptionalField", null),
Table.SelectColumns(Source, {"ColA", "ColB"}, MissingField.Ignore)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Missing Fields.xlsx`** (`9,625` bytes)

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

[⬅️ Previous: Ep74-Frequency-vs-Sequence-Analysis](../../07-Power-Query-Engine-and-M-Language/Ep74-Frequency-vs-Sequence-Analysis/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep76-Away-From-Zero ➡️](../../07-Power-Query-Engine-and-M-Language/Ep76-Away-From-Zero/README.md)
