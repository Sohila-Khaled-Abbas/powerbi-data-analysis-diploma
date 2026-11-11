# Episode 6: Get Data From PDFs

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 06** | Get Data From PDFs | `26m 50s` | [Watch on YouTube](https://www.youtube.com/watch?v=FoofsFoj6ik) | [Download Sample Data](https://drive.google.com/drive/folders/15XsLUpRll4QUF5hiQv-sI7Z33N43uzgq?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Extracting tabular data from PDF files. Demonstrates how Power Query detects tabular bounding boxes, extracts multi-page tables, and handles irregular layout boundaries in PDF documents.

**Key Skills & Concepts Covered:**
- ✅ **Pdf.Tables connector**
- ✅ **Automatic Table Detection in PDF**
- ✅ **Multi-page PDF Table Extraction**
- ✅ **Cleaning Non-standard PDF Header Artifacts**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = Pdf.Tables(File.Contents("report.pdf")),
Table1 = Source{[Id="Table001"]}[Data]
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📑 **`1. Sales Database.pdf`** (`4.5 MB (4,762,386 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Abdullah Alomary.pdf`** (`132.9 KB (136,128 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Abeer Mohamed.pdf`** (`127.8 KB (130,820 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Ahmed Ezzat.pdf`** (`127.5 KB (130,546 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Ahmed Yousef.pdf`** (`133.2 KB (136,414 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Amal Abdelfatah.pdf`** (`125.2 KB (128,178 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Amal Mohamed.pdf`** (`131.7 KB (134,884 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Azza Abdelrahman.pdf`** (`132.5 KB (135,675 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Berry Hassan.pdf`** (`129.4 KB (132,498 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Essam Elsayad.pdf`** (`126.9 KB (129,956 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Hala Ahmed.pdf`** (`128.8 KB (131,918 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Hassan Abdelrahman.pdf`** (`535.1 KB (547,991 bytes)`) — PDF source document / statement
- 📑 **`2. Employees Database/Mahmoud Hamouda.pdf`** (`128.2 KB (131,274 bytes)`) — PDF source document / statement
---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep04-05-Get-Data-From-CSV](../../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep07-On-Premises-Data-Gateway ➡️](../../02-Data-Acquisition/Ep07-On-Premises-Data-Gateway/README.md)
