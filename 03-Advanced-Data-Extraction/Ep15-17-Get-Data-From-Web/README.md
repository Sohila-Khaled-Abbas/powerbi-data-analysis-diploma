# Episodes 15 - 17: Get Data From Web

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `03-Advanced-Data-Extraction`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 15** | Get Data From Web | `34m 43s` | [Watch on YouTube](https://www.youtube.com/watch?v=97jpUL-FJIY) | Included in repo / Follow lecture |
| **Ep. 16** | Get Data From Web (Invoke) | `22m 13s` | [Watch on YouTube](https://www.youtube.com/watch?v=QrIstR9ZyaA) | Included in repo / Follow lecture |
| **Ep. 17** | Get Data From Web (List) | `30m 41s` | [Watch on YouTube](https://www.youtube.com/watch?v=NLzEOoYmh1s) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

### Part 15: Get Data From Web | Ep. 15 | Microsoft Power BI Data Analysis Diploma

Web Scraping fundamentals in Power BI. Explains Web.BrowserContents, HTML table detection, extracting unstructured HTML tables, and automated web data ingestion.

**Key Skills & Concepts Covered:**
- ✅ **Web.BrowserContents & Web.Page**
- ✅ **Scraping HTML Tables**
- ✅ **CSS Selectors & Table Parsing**
- ✅ **Handling Dynamic JavaScript Rendered Pages**

### Part 16: Get Data From Web (Invoke) | Ep. 16 | Microsoft Power BI Data Analysis Diploma

Advanced Web Scraping using Custom Functions and Invocation. Demonstrates building a reusable M function that scrapes web pages parameterized by page numbers or category IDs.

**Key Skills & Concepts Covered:**
- ✅ **Parameterized Web Scraping**
- ✅ **Creating Custom Scraping M Functions**
- ✅ **Table.AddColumn with Function Invocation**
- ✅ **Batch Scraping Multiple URLs**

### Part 17: Get Data From Web (List) | Ep. 17 | Microsoft Power BI Data Analysis Diploma

Web Scraping with List operations and pagination. Demonstrates generating pagination lists in M, iterating through dynamic web queries, and combining results into a single dataset.

**Key Skills & Concepts Covered:**
- ✅ **Generating Dynamic URL Lists**
- ✅ **List.Transform for Multi-Page Scraping**
- ✅ **Handling Pagination Limits**
- ✅ **Combining Paginated Tables (Table.Combine)**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

#### Episode 15 Code Reference:

```powerquery
Source = Web.Page(Web.Contents("https://example.com/data")),
Data0 = Source{0}[Data]
```

#### Episode 16 Code Reference:

```powerquery
(pageNumber as number) =>
let
    Source = Web.Page(Web.Contents("https://example.com/products?page=" & Text.From(pageNumber)))
in
    Source{0}[Data]
```

#### Episode 17 Code Reference:

```powerquery
Pages = {1..10},
Tables = List.Transform(Pages, each GetPageData(_)),
Combined = Table.Combine(Tables)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`get data from web.pbix`** (`79,272` bytes)

> 💡 **How to use:** Open `.pbix` files in **Microsoft Power BI Desktop**, or open `.xlsx` files in **Microsoft Excel** to inspect the source schemas and practice the transformations step-by-step.

---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep14-Get-Data-From-Microsoft-Exchange](../../02-Data-Acquisition/Ep14-Get-Data-From-Microsoft-Exchange/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep18-19-Get-Data-From-API ➡️](../../03-Advanced-Data-Extraction/Ep18-19-Get-Data-From-API/README.md)
