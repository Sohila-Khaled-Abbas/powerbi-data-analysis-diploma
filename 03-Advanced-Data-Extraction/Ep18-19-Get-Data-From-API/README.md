# Episodes 18 - 19: Get Data From API

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `03-Advanced-Data-Extraction`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 18** | Get Data From API | `23m 20s` | [Watch on YouTube](https://www.youtube.com/watch?v=VejauRwSb8A) | Included in repo / Follow lecture |
| **Ep. 19** | Get Data From API (List. Generate) | `34m 40s` | [Watch on YouTube](https://www.youtube.com/watch?v=Jrr34uXL7sk) | [Download Sample Data](https://drive.google.com/file/d/1eKPGO9RTRI2_ES3W-SkqLlj_1aGBGD7B/view?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

### Part 18: Get Data From API | Ep. 18 | Microsoft Power BI Data Analysis Diploma

Connecting to REST APIs from Power BI. Covers HTTP GET requests, API endpoints, request headers, API keys, and handling raw JSON response payloads.

**Key Skills & Concepts Covered:**
- ✅ **REST API Architecture & HTTP Methods**
- ✅ **Passing Headers & API Tokens in Web.Contents**
- ✅ **Json.Document Parsing**
- ✅ **API Authentication Best Practices**

### Part 19: Get Data From API (List. Generate) | Ep. 19 | Microsoft Power BI Data Analysis Diploma

Advanced API pagination using List.Generate. Solves real-world API limits by generating stateful pagination loops until the API returns no further records.

**Key Skills & Concepts Covered:**
- ✅ **List.Generate Stateful Loops**
- ✅ **API Cursor & Offset Pagination**
- ✅ **Dynamic Stop Conditions**
- ✅ **Deep M Language Looping Strategy**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

#### Episode 18 Code Reference:

```powerquery
Source = Json.Document(Web.Contents("https://api.example.com/v1/data", [Headers=[#"Authorization"="Bearer YOUR_TOKEN"]]))
```

#### Episode 19 Code Reference:

```powerquery
PaginatedData = List.Generate(
    () => [Page = 1, Data = FetchApi(1)],
    each not List.IsEmpty([Data]),
    each [Page = [Page] + 1, Data = FetchApi([Page] + 1)],
    each [Data]
)
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

[⬅️ Previous: Ep15-17-Get-Data-From-Web](../../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep20-Get-Data-From-LinkedIn ➡️](../../03-Advanced-Data-Extraction/Ep20-Get-Data-From-LinkedIn/README.md)
