# Episode 23: Get Data From JSON - Facebook - Instagram

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `03-Advanced-Data-Extraction`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 23** | Get Data From JSON - Facebook - Instagram | `25m 20s` | [Watch on YouTube](https://www.youtube.com/watch?v=pQ-ZAmkhXzM) | [Download Sample Data](https://drive.google.com/file/d/178IbhuDlsTxMJr9VPaYBlQM2VROSlGuw/view?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Parsing deeply nested JSON datasets from Facebook, Instagram, and web platforms. Demonstrates expanding records, converting lists to tables, and handling jagged JSON hierarchies.

**Key Skills & Concepts Covered:**
- ✅ **Json.Document Parser**
- ✅ **Expanding Nested Records & Lists**
- ✅ **Normalizing Hierarchical JSON into Tables**
- ✅ **Social Media Export Analytics**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = Json.Document(File.Contents("data.json")),
#"Converted to Table" = Record.ToTable(Source),
#"Expanded Column" = Table.ExpandRecordColumn(...) 
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📦 **`Essam Elsayad.json`** (`2.4 MB (2,541,993 bytes)`) — JSON data payload
- 📊 **`JSON.pbix`** (`1.1 MB (1,200,515 bytes)`) — Power BI Desktop solution model

> 💡 **How to use:** Open `.pbix` files in **Microsoft Power BI Desktop**.
---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Navigation

[⬅️ Previous: Ep22-Get-Data-From-Dataverse](../../03-Advanced-Data-Extraction/Ep22-Get-Data-From-Dataverse/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep24-Permissions-Credential-Encryption-Privacy ➡️](../../04-Governance-and-Automation/Ep24-Permissions-Credential-Encryption-Privacy/README.md)
