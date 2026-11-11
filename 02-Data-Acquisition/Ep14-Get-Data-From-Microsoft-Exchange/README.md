# Episode 14: Get Data From Microsoft Exchange

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `02-Data-Acquisition`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 14** | Get Data From Microsoft Exchange | `23m 18s` | [Watch on YouTube](https://www.youtube.com/watch?v=U9rl2ygQSRs) | [Download Sample Data](https://drive.google.com/drive/folders/1pVWf-i4SiGqHtpdgYTIuBsFXagPSboxa?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Connecting Power BI directly to Microsoft Exchange / Outlook mailboxes. Demonstrates extracting emails, calendar appointments, task lists, and email attachments for operational analysis.

**Key Skills & Concepts Covered:**
- ✅ **Exchange.Contents Connector**
- ✅ **Extracting Email Headers & Subject Analytics**
- ✅ **Parsing Email Attachments into Data Tables**
- ✅ **Mailbox Analytics & Activity Tracking**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = Exchange.Contents("user@domain.com"),
Mail = Source{[Name="Mail"]}[Data]
```

---

## 📁 Practice Files in this Repository

- *Included with the lecture instructions / no local dataset required.*
---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep13-Get-Data-From-Semantic-Models](../../02-Data-Acquisition/Ep13-Get-Data-From-Semantic-Models/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep15-17-Get-Data-From-Web ➡️](../../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/README.md)
