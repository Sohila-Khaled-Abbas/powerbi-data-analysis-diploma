# Episode 21: Get Data From X (Twitter) | Ep. 21 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `03-Advanced-Data-Extraction`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 21** | Get Data From X (Twitter) | Ep. 21 | Microsoft Power BI Data Analysis Diploma | `9m 32s` | [Watch on YouTube](https://www.youtube.com/watch?v=6vDArBejQe0) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

Extracting and analyzing X (Twitter) data. Covers API endpoints, tweet metrics, engagement analysis, and processing social feed streams in Power BI.

**Key Skills & Concepts Covered:**
- ✅ **X (Twitter) API Integration**
- ✅ **Sentiment & Engagement Analysis**
- ✅ **Parsing Nested Tweet JSON Objects**
- ✅ **Social Media Reporting**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = Json.Document(Web.Contents("https://api.twitter.com/2/tweets", [Headers=[#"Authorization"="Bearer TOKEN"]]))
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

[⬅️ Previous: Ep20-Get-Data-From-LinkedIn](../../03-Advanced-Data-Extraction/Ep20-Get-Data-From-LinkedIn/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep22-Get-Data-From-Dataverse ➡️](../../03-Advanced-Data-Extraction/Ep22-Get-Data-From-Dataverse/README.md)
