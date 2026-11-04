# Episode 34: Local Interpretation | Ep. 34 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 34** | Local Interpretation | Ep. 34 | Microsoft Power BI Data Analysis Diploma | `17m 36s` | [Watch on YouTube](https://www.youtube.com/watch?v=NR93ZmJplk0) | [Download Sample Data](https://drive.google.com/drive/folders/1kXySoG8OwEKlbwOU4dIOR0P5Crt2qPTH?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Mastering Local Interpretation and Culture-sensitive data parsing. Explains resolving international format conflicts (US MM/DD/YYYY vs UK/EU DD/MM/YYYY, comma vs period decimal separators).

**Key Skills & Concepts Covered:**
- ✅ **Culture-Specific Type Casting**
- ✅ **Resolving Date Inversion (MM/DD vs DD/MM)**
- ✅ **Decimal & Thousand Separator Discrepancies**
- ✅ **Using 'Using Locale...' in Power Query**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Table.TransformColumnTypes(Source, {{"Date", type date}}, "en-GB"),
Table.TransformColumnTypes(Source, {{"Price", type number}}, "de-DE")
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Local Interpretation Essam Elsdayad.pbix`** (`257,083,764` bytes)
- 📄 **`WideWorldImporters_2021-23.xlsx`** (`23,408,295` bytes)
- 📄 **`csv_wideworldimporters.csv`** (`20,836,447` bytes)
- 📄 **`datatypes.xlsx`** (`32,267` bytes)

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

[⬅️ Previous: Ep32-33-Different-Data-Types](../../05-Data-Transformation/Ep32-33-Different-Data-Types/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep35-Custom-Columns ➡️](../../05-Data-Transformation/Ep35-Custom-Columns/README.md)
