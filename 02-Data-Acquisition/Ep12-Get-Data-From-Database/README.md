# Episode 12: Get Data From Database (SQL | Oracle | SAP) | Ep. 12 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 12** | Get Data From Database (SQL | Oracle | SAP) | Ep. 12 | Microsoft Power BI Data Analysis Diploma | `46m 21s` | [Watch on YouTube](https://www.youtube.com/watch?v=VQsinzZ4ERY) | [Download Sample Data](https://drive.google.com/file/d/1AOYbAyLbbsSYuvJe3uCpiPCiU4fATSRS/view?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Querying Enterprise Relational Databases including Microsoft SQL Server, Oracle, and SAP HANA. Covers database authentication, server/database addressing, and Query Folding pushdown to the SQL engine.

**Key Skills & Concepts Covered:**
- ✅ **Sql.Database & Oracle.Database Connectors**
- ✅ **Query Folding (Pushing compute to SQL)**
- ✅ **Writing Native SQL Queries in Power Query**
- ✅ **Database Permissions & Credentials**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = Sql.Database("server_name", "db_name", [Query="SELECT * FROM Sales WHERE OrderDate >= '2023-01-01'"])
```

---

## 📁 Practice Files in this Repository

No local binary dataset files are stored in this folder. You can use the official sample data link from the video description above, or practice directly inside Power BI Desktop following the video walkthrough.

---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep11-Get-Data-From-Google-Drive](../../02-Data-Acquisition/Ep11-Get-Data-From-Google-Drive/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep13-Get-Data-From-Semantic-Models ➡️](../../02-Data-Acquisition/Ep13-Get-Data-From-Semantic-Models/README.md)
