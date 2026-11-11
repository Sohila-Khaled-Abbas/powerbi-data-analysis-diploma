# Episode 64: Multi-Bank PDF Consolidation

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 64** | Multi-Bank PDF Consolidation | `37m 42s` | [Watch on YouTube](https://www.youtube.com/watch?v=QDId2DLl7EY) | [Download Sample Data](https://drive.google.com/drive/folders/1pd3LJW4AgqME4h5tp1Qzf7WadEmuJWvA) |

---

## 🎯 Lesson Overview & Objectives

Enterprise Case Study: Multi-Bank PDF Consolidation. Consolidates monthly bank statements from multiple financial institutions (Alrajhi, SNB) with completely different layouts into a single ledger.

**Key Skills & Concepts Covered:**
- ✅ **Multi-Layout PDF Statement Parsing**
- ✅ **Reconciling Disparate Bank Column Structures**
- ✅ **Handling Debit/Credit Discrepancies**
- ✅ **Automating Unified Financial Cashflow Statements**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
// Unified Bank Schema:
// Date, BankName, Description, ReferenceNo, Debit, Credit, Balance
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📊 **`Multi-Bank PDF Consolidation.pbix`** (`35.9 KB (36,810 bytes)`) — Power BI Desktop solution model
- 📑 **`Alrajhi/Alrajhi Bank.pdf`** (`212.2 KB (217,283 bytes)`) — PDF source document / statement
- 📑 **`SNB/SNB Bank.pdf`** (`41.2 KB (42,188 bytes)`) — PDF source document / statement

> 💡 **How to use:** Open `.pbix` files in **Microsoft Power BI Desktop**.
---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep63-Practical-Exercise-2](../../06-Case-Studies/Ep63-Practical-Exercise-2/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep65-Null-vs-Blank ➡️](../../07-Power-Query-Engine-and-M-Language/Ep65-Null-vs-Blank/README.md)
