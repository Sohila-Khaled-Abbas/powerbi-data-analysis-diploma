# Episode 9: Get Data From SharePoint |Ep. 9 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 09** | Get Data From SharePoint |Ep. 9 | Microsoft Power BI Data Analysis Diploma | `49m 31s` | [Watch on YouTube](https://www.youtube.com/watch?v=JAe7n3Fo1uU) | [Download Sample Data](https://drive.google.com/drive/folders/1HHCYLuq97qB9OQ5FIN0hAPf_HaAfUX6l?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Connecting to SharePoint Document Libraries and SharePoint Lists. Shows how to query the SharePoint Folder API, extract nested binary files, and filter dynamic team folders.

**Key Skills & Concepts Covered:**
- ✅ **SharePoint.Files vs SharePoint.Contents**
- ✅ **SharePoint List Connector**
- ✅ **Extracting Binaries from SharePoint Folders**
- ✅ **Team Site Security & RBAC**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = SharePoint.Files("https://myorg.sharepoint.com/sites/TeamSite", [ApiVersion = 15])
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

[⬅️ Previous: Ep08-Get-Data-From-OneDrive](../../02-Data-Acquisition/Ep08-Get-Data-From-OneDrive/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep10-Get-Data-From-Google-Sheets ➡️](../../02-Data-Acquisition/Ep10-Get-Data-From-Google-Sheets/README.md)
