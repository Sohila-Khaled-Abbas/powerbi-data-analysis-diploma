# Episode 10: Get Data From Google Sheets

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 10** | Get Data From Google Sheets | `32m 6s` | [Watch on YouTube](https://www.youtube.com/watch?v=Jil1SSWVFeU) | [Download Sample Data](https://drive.google.com/drive/folders/1jJ0wn1nepvgLh1Tiq2V59TZbuzthQFGd?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Connecting directly to Google Sheets from Power BI. Covers using the native Google Sheets connector, authenticating with Google accounts, and live synchronizing cloud spreadsheets.

**Key Skills & Concepts Covered:**
- ✅ **Native Google Sheets Connector**
- ✅ **OAuth2 Google Authentication**
- ✅ **Maintaining Spreadsheet Structure in BI**
- ✅ **Syncing Cloud Updates**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = GoogleSheets.Contents("https://docs.google.com/spreadsheets/d/...")
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

[⬅️ Previous: Ep09-Get-Data-From-SharePoint](../../02-Data-Acquisition/Ep09-Get-Data-From-SharePoint/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep11-Get-Data-From-Google-Drive ➡️](../../02-Data-Acquisition/Ep11-Get-Data-From-Google-Drive/README.md)
