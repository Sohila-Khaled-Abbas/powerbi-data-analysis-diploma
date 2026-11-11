# Episode 81: Try & Otherwise

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `07-Power-Query-Engine-and-M-Language`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 81** | Try & Otherwise | `12m 17s` | [Watch on YouTube](https://www.youtube.com/watch?v=YTZEzXVY8IA) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1MCI_gLq5mbBFYjSXrsDS-Vq0ih8FF8jP/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Defensive Programming with Try & Otherwise in Power Query. Teaches catching run-time evaluation exceptions gracefully, substituting fallbacks, and extracting structured error records.

**Key Skills & Concepts Covered:**
- ✅ **Try ... Otherwise Syntax**
- ✅ **Catching Exceptions Gracefully**
- ✅ **Inspecting Error Records (Reason, Message, Detail)**
- ✅ **Zero-Downtime Production ETL**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
try Number.FromText([TextVal]) otherwise 0

// Inspecting detailed error metadata:
Result = try [Calculation],
Status = if Result[HasError] then Result[Error][Message] else Result[Value]
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Try and Otherwise.xlsx`** (`14.9 KB (15,219 bytes)`) — Excel practice dataset

> 💡 **How to use:** Open `.xlsx` files in **Microsoft Excel** to inspect source tables, verify data types, and follow along with the transformations.
---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep80-Null-Coalescing-Operator](../../07-Power-Query-Engine-and-M-Language/Ep80-Null-Coalescing-Operator/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md)
