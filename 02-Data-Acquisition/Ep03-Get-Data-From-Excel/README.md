# Episode 3: Get Data From Microsoft Excel

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 03** | Get Data From Microsoft Excel | `44m 33s` | [Watch on YouTube](https://www.youtube.com/watch?v=BO6xDtaNLpA) | [Download Sample Data](https://drive.google.com/drive/folders/1UWs2R2CIeGZlS4hl0n0V6jr8Hb0_Cplu?usp=sharing) |

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

- 📄 **`1. Sales Dastabase.xlsx`** (`5.2 MB (5,452,231 bytes)`) — Excel practice dataset
- 📄 **`2. Sales Dastabase.xlsx`** (`5.2 MB (5,455,308 bytes)`) — Excel practice dataset
- 📄 **`3. Countries Database.xlsx`** (`341.1 KB (349,310 bytes)`) — Excel practice dataset
- 📊 **`Excel Data.pbix`** (`2.4 MB (2,495,695 bytes)`) — Power BI Desktop solution model
- 📄 **`4. Employees Datebase/Administration.xlsx`** (`19.8 KB (20,266 bytes)`) — Excel practice dataset
- 📄 **`4. Employees Datebase/Business Development.xlsx`** (`21.1 KB (21,589 bytes)`) — Excel practice dataset
- 📄 **`4. Employees Datebase/Customer Service.xlsx`** (`22.2 KB (22,725 bytes)`) — Excel practice dataset
- 📄 **`4. Employees Datebase/Finance.xlsx`** (`22.9 KB (23,479 bytes)`) — Excel practice dataset
- 📄 **`4. Employees Datebase/Human Resources.xlsx`** (`21.1 KB (21,571 bytes)`) — Excel practice dataset
- 📄 **`4. Employees Datebase/IT.xlsx`** (`21.7 KB (22,187 bytes)`) — Excel practice dataset
- 📄 **`4. Employees Datebase/Legal.xlsx`** (`21.1 KB (21,599 bytes)`) — Excel practice dataset

> 💡 **How to use:** Open `.pbix` files in **Microsoft Power BI Desktop**; and Open `.xlsx` files in **Microsoft Excel** to inspect source tables, verify data types, and follow along with the transformations.
---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🔬 Independent Practice Extension

The snippet below is a navigation pattern. Replace the path, object name, and object kind with values visible in your own workbook's navigation table.

~~~powerquery
let
    FilePath = "C:\\Data\\Sales.xlsx",
    WorkbookObjects = Excel.Workbook(File.Contents(FilePath), null, true),
    SelectedTable = WorkbookObjects{[Item = "Sales", Kind = "Table"]}[Data]
in
    SelectedTable
~~~

**Compare workbook objects:** Excel Tables, worksheets, and defined names can appear as different objects. Prefer a structured Excel Table when the source is maintained as a table; verify the actual `Item` and `Kind` values instead of assuming them.

**Practice task:** add a row inside the source Excel Table, refresh Power BI, then add an unrelated worksheet and refresh again.

**Validation:** confirm the added table row is included, unrelated objects are excluded, and output columns/types remain correct. A worksheet-based source may behave differently, so test the source you actually use.

## 🧭 Navigation

[⬅️ Previous: Ep02-Proper-Raw-Data-Structure](../../01-Data-Foundations/Ep02-Proper-Raw-Data-Structure/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep04-05-Get-Data-From-CSV ➡️](../../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/README.md)
