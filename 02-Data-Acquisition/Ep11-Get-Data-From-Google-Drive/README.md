# Episode 11: Get Data From Google Drive | Ep. 11 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 11** | Get Data From Google Drive | Ep. 11 | Microsoft Power BI Data Analysis Diploma | `17m 6s` | [Watch on YouTube](https://www.youtube.com/watch?v=JYGhyETA9yc) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1hWUanCD3IanMbBAW_mDcXPHKs5UjPrUm/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Extracting datasets stored in Google Drive. Explains how to extract direct download URLs for public or shared drive files and connect seamlessly without third-party plugins.

**Key Skills & Concepts Covered:**
- ✅ **Google Drive Direct Download Links**
- ✅ **Web.Contents Connector for Drive Assets**
- ✅ **Extracting CSV/Excel from Drive**
- ✅ **Handling Permissions & Shared Drives**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = Web.Contents("https://drive.google.com/uc?export=download&id=FILE_ID")
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

[⬅️ Previous: Ep10-Get-Data-From-Google-Sheets](../../02-Data-Acquisition/Ep10-Get-Data-From-Google-Sheets/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep12-Get-Data-From-Database ➡️](../../02-Data-Acquisition/Ep12-Get-Data-From-Database/README.md)
