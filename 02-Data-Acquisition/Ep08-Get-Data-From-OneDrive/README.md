# Episode 8: Get Data From OneDrive | Ep. 8 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 08** | Get Data From OneDrive | Ep. 8 | Microsoft Power BI Data Analysis Diploma | `14m 56s` | [Watch on YouTube](https://www.youtube.com/watch?v=esTfWYjDWBs) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1lQh89lXIJ5OF3j44NyMkdw-vfJEGti3B/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Ingesting files directly from Microsoft OneDrive. Contrasts syncing via OneDrive desktop sync app vs direct cloud web URL connection using organization credentials for zero-gateway cloud refreshes.

**Key Skills & Concepts Covered:**
- ✅ **OneDrive Web URL Extraction**
- ✅ **Replacing Local Path with Web.Contents**
- ✅ **Automated Cloud Refresh Without Local Machine**
- ✅ **Organizational Account Authentication**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = Excel.Workbook(Web.Contents("https://myorg-my.sharepoint.com/personal/.../file.xlsx?web=0"), null, true)
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

[⬅️ Previous: Ep07-On-Premises-Data-Gateway](../../02-Data-Acquisition/Ep07-On-Premises-Data-Gateway/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep09-Get-Data-From-SharePoint ➡️](../../02-Data-Acquisition/Ep09-Get-Data-From-SharePoint/README.md)
