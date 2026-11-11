# Episodes 32 - 33: Different Data Types (Theory)

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `05-Data-Transformation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 32** | Different Data Types (Theory) | `25m 59s` | [Watch on YouTube](https://www.youtube.com/watch?v=KeuW9GhCIbY) | Included in repo / Follow lecture |
| **Ep. 33** | Different Data Types | `45m 18s` | [Watch on YouTube](https://www.youtube.com/watch?v=p8wStMCEIbc) | [Download Sample Data](https://drive.google.com/drive/folders/1mCgtHkBd8rtNE89wM-fRmZpJWZzDtCcD?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

### Part 32: Different Data Types (Theory) | Ep. 32 | Microsoft Power BI Data Analysis Diploma

Theoretical foundation of Power Query Data Types. Explains how the VertiPaq tabular storage engine encodes data, dictionary compression, type hierarchies, and storage impact.

**Key Skills & Concepts Covered:**
- ✅ **Power Query Data Type Architecture**
- ✅ **VertiPaq Dictionary & Run-Length Encoding**
- ✅ **Impact of Data Types on Memory & Compression**
- ✅ **Type Compatibility & Implicit Casting**

### Part 33: Different Data Types | Ep. 33 | Microsoft Power BI Data Analysis Diploma

Practical handling and conversion of Data Types in Power Query. Demonstrates resolving type mismatches, datetime conversions, fixed decimals (Currency), and type inspection.

**Key Skills & Concepts Covered:**
- ✅ **Table.TransformColumnTypes Function**
- ✅ **Fixed Decimal (Int64.Type vs Currency.Type)**
- ✅ **Date & Time Conversions**
- ✅ **Preventing Automatic Type Inference Errors**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

#### Episode 32 Code Reference:

```powerquery
// Primitive M Types: text, number, logical, date, time, datetime, datetimezone, duration, binary, list, record, table, function, type
```

#### Episode 33 Code Reference:

```powerquery
Table.TransformColumnTypes(Source, {{"ID", Int64.Type}, {"Date", type date}, {"Amount", Currency.Type}})
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📊 **`Essam Elsayad.pbix`** (`128.0 MB (134,174,599 bytes)`) — Power BI Desktop solution model
- 📄 **`Essam Elsayad.xlsx`** (`22.3 MB (23,408,032 bytes)`) — Excel practice dataset
- 📄 **`WideWorldImporters_2021-23.xlsx`** (`21.7 MB (22,800,736 bytes)`) — Excel practice dataset
- 📄 **`datatypes.xlsx`** (`31.5 KB (32,254 bytes)`) — Excel practice dataset
- 📄 **`datatypes_info.xlsx`** (`29.8 KB (30,512 bytes)`) — Excel practice dataset

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

[⬅️ Previous: Ep30-31-Parameters-and-Templates](../../04-Governance-and-Automation/Ep30-31-Parameters-and-Templates/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep34-Local-Interpretation ➡️](../../05-Data-Transformation/Ep34-Local-Interpretation/README.md)
