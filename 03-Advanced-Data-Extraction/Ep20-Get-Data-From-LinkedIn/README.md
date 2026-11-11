# Episode 20: Get Data From LinkedIn

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `03-Advanced-Data-Extraction`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 20** | Get Data From LinkedIn | `17m 20s` | [Watch on YouTube](https://www.youtube.com/watch?v=7VdsxREKcwo) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

Connecting to LinkedIn data and extracting professional network metrics, campaign performance, and profile analytics using API connectors and exported datasets.

**Key Skills & Concepts Covered:**
- ✅ **LinkedIn Data Ingestion**
- ✅ **Campaign & Ad Metrics Extraction**
- ✅ **Authentication Tokens & Permissions**
- ✅ **Modeling Social Performance Data**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
// Ingesting exported campaign metrics or API endpoints
Source = Json.Document(Web.Contents("https://api.linkedin.com/v2/..."))
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

[⬅️ Previous: Ep18-19-Get-Data-From-API](../../03-Advanced-Data-Extraction/Ep18-19-Get-Data-From-API/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep21-Get-Data-From-X-Twitter ➡️](../../03-Advanced-Data-Extraction/Ep21-Get-Data-From-X-Twitter/README.md)
