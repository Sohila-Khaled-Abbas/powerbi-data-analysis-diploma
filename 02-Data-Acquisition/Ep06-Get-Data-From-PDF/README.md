# Episode 6: Get Data From PDFs | Ep. 6 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 06** | Get Data From PDFs | Ep. 6 | Microsoft Power BI Data Analysis Diploma | `26m 50s` | [Watch on YouTube](https://www.youtube.com/watch?v=FoofsFoj6ik) | [Download Sample Data](https://drive.google.com/drive/folders/15XsLUpRll4QUF5hiQv-sI7Z33N43uzgq?usp=sharing) |

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

- 📄 **`1. Sales Database.pdf`** (`4,762,386` bytes)
- 📂 **`2. Employees Database/`** (Directory containing 12 dataset files)

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

[⬅️ Previous: Ep04-05-Get-Data-From-CSV](../../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep07-On-Premises-Data-Gateway ➡️](../../02-Data-Acquisition/Ep07-On-Premises-Data-Gateway/README.md)
