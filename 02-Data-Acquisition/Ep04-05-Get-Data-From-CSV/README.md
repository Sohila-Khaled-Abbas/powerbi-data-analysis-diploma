# Episodes 4 - 5: Get Data From CSV Files

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 04** | Get Data From CSV Files | `33m 35s` | [Watch on YouTube](https://www.youtube.com/watch?v=2I00ZCmG204) | [Download Sample Data](https://drive.google.com/drive/folders/1kd63LXUQ8qZ21yU54xNTX1_PwLT_MXAm?usp=sharing) |
| **Ep. 05** | Fixing CSV Import Issues | `6m 46s` | [Watch on YouTube](https://www.youtube.com/watch?v=TbyiWFP9IYE) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

### Part 4: Get Data From CSV Files | Ep. 4 | Microsoft Power BI Data Analysis Diploma

Extracting flat data from CSV and TXT files. Examines delimiters (comma, tab, semicolon), encoding standards (UTF-8 vs ANSI), line breaks, and how the Power Query engine previews and splits columns.

**Key Skills & Concepts Covered:**
- ✅ **Csv.Document connector**
- ✅ **Custom & Standard Delimiters**
- ✅ **Text Encoding (UTF-8, Arabic Windows 1256)**
- ✅ **Quote Handling & Line Breaks**

### Part 5: Fixing CSV Import Issues | Ep. 5 | Microsoft Power BI Data Analysis Diploma

Troubleshooting common CSV import failures: misaligned columns, embedded commas inside quoted fields, trailing summary headers, and extra blank rows.

**Key Skills & Concepts Covered:**
- ✅ **QuoteStyle.Csv vs QuoteStyle.None**
- ✅ **Skipping Unwanted Top Header Rows**
- ✅ **Handling Jagged Rows & Column Count Mismatches**
- ✅ **Data Quality Pre-filtering**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

#### Episode 4 Code Reference:

```powerquery
Source = Csv.Document(File.Contents("path/to/file.csv"), [Delimiter=",", Columns=10, Encoding=65001, QuoteStyle=QuoteStyle.None])
```

#### Episode 5 Code Reference:

```powerquery
Source = Csv.Document(File.Contents("data.csv"), [Delimiter=",", QuoteStyle=QuoteStyle.Csv]),
#"Promoted Headers" = Table.PromoteHeaders(Source, [PromoteAllScalars=true])
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`1. csv Employees.csv`** (`1,167` bytes)
- 📄 **`2. txt Customers.txt`** (`106` bytes)
- 📄 **`3. csv Employees With Summary Header.csv`** (`1,237` bytes)
- 📄 **`4. csv Employees With Quotes.csv`** (`1,622` bytes)
- 📄 **`5. CSV Extract From Example.csv`** (`3,088` bytes)

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

[⬅️ Previous: Ep03-Get-Data-From-Excel](../../02-Data-Acquisition/Ep03-Get-Data-From-Excel/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep06-Get-Data-From-PDF ➡️](../../02-Data-Acquisition/Ep06-Get-Data-From-PDF/README.md)
