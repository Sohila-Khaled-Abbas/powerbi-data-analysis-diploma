# Episode 3: Get Data From Microsoft Excel | Ep. 3 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 03** | Get Data From Microsoft Excel | Ep. 3 | Microsoft Power BI Data Analysis Diploma | `44m 33s` | [Watch on YouTube](https://www.youtube.com/watch?v=BO6xDtaNLpA) | [Download Sample Data](https://drive.google.com/drive/folders/1UWs2R2CIeGZlS4hl0n0V6jr8Hb0_Cplu?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Connecting to and ingesting data from Microsoft Excel workbooks into Power BI. Explains selecting worksheets, named ranges, and Excel Tables, understanding sheet navigation preview, and handling schema modifications.

**Key Skills & Concepts Covered:**
- ✅ **Excel Connector (Excel.Workbook)**
- ✅ **Worksheets vs Named Tables vs Defined Names**
- ✅ **Handling Multi-sheet Workbooks**
- ✅ **Folder-level vs File-level Loading**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = Excel.Workbook(File.Contents("path/to/file.xlsx"), null, true),
Sheet1 = Source{[Item="Sheet1",Kind="Sheet"]}[Data]
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`1. Sales Dastabase.xlsx`** (`5,452,231` bytes)
- 📄 **`2. Sales Dastabase.xlsx`** (`5,455,308` bytes)
- 📄 **`3. Countries Database.xlsx`** (`349,310` bytes)
- 📂 **`4. Employees Datebase/`** (Directory containing 7 dataset files)
- 📄 **`Excel Data.pbix`** (`2,495,695` bytes)

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

[⬅️ Previous: Ep02-Proper-Raw-Data-Structure](../../01-Data-Foundations/Ep02-Proper-Raw-Data-Structure/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep04-05-Get-Data-From-CSV ➡️](../../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/README.md)
