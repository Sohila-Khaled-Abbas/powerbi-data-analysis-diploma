# Episodes 69 - 70: M Language (Theory) | Ep. 69 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 69** | M Language (Theory) | Ep. 69 | Microsoft Power BI Data Analysis Diploma | `1h 16m 20s` | [Watch on YouTube](https://www.youtube.com/watch?v=DeJi6omk5Dk) | [Download Sample Data](https://drive.google.com/file/d/15EEPsaZEM5xnlh3uwgLZ7Avb-k5D8keg/view?usp=sharing) |
| **Ep. 70** | M Language | Ep. 70 | Microsoft Power BI Data Analysis Diploma | `33m 6s` | [Watch on YouTube](https://www.youtube.com/watch?v=KNfHFcJUQOs) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1mGOJ_w5ZzEraxZR_CvoYwuK682ZBqzt_/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

### Part 69: M Language (Theory) | Ep. 69 | Microsoft Power BI Data Analysis Diploma

Theoretical foundations of Power Query M Language. Covers functional language principles, the 'let ... in' block structure, lazy evaluation, immutability, and scoping environments.

**Key Skills & Concepts Covered:**
- ✅ **Functional Programming Concepts in M**
- ✅ **Let ... In Syntax & Step Dependencies**
- ✅ **Lazy Evaluation (Steps evaluated only when required)**
- ✅ **Immutability & Variables as Step Aliases**

### Part 70: M Language | Ep. 70 | Microsoft Power BI Data Analysis Diploma

Deep Dive into M Language Data Structures. Detailed study of Lists ({}), Records ([]), Tables (#table), and Functions (() =>), and how to manipulate them programmatically.

**Key Skills & Concepts Covered:**
- ✅ **M List Construction & Functions (List.*)**
- ✅ **M Record Construction & Access (Record.*)**
- ✅ **M Table Functions (Table.*)**
- ✅ **Custom Lambda Functions in M**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

#### Episode 69 Code Reference:

```powerquery
let
    Source = Excel.Workbook(...),
    Step1 = Table.SelectRows(Source, ...),
    Step2 = Table.TransformColumnTypes(Step1, ...)
in
    Step2
```

#### Episode 70 Code Reference:

```powerquery
MyList = {1, 2, 3},
MyRecord = [ID = 101, Name = "Essam"],
MyTable = #table({"ID", "Name"}, {{1, "Essam"}, {2, "Mai"}})
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`M Language Theory.pdf`** (`4,685,560` bytes)
- 📄 **`M Language.pbix`** (`20,969` bytes)
- 📄 **`M Language.xlsx`** (`10,124` bytes)

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

[⬅️ Previous: Ep68-Step-Error-vs-Cell-Error](../../07-Power-Query-Engine-and-M-Language/Ep68-Step-Error-vs-Cell-Error/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep71-Practical-Exercise-3 ➡️](../../07-Power-Query-Engine-and-M-Language/Ep71-Practical-Exercise-3/README.md)
