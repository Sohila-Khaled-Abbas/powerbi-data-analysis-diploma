# Episode 57: Inconsistent Data Sources

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 57** | Inconsistent Data Sources | `37m 56s` | [Watch on YouTube](https://www.youtube.com/watch?v=j_PFG3lIaaM) | [Download Sample Data](https://drive.google.com/drive/folders/1fLH6GoSZyYeUnM7IBxTc2IG-8afFezJY) |

---

## 🎯 Lesson Overview & Objectives

Real-World Case Study: Handling Inconsistent Data Sources. Builds a fault-tolerant folder connector that automatically filters out unwanted file extensions, corrupt files, and temporary Excel locks.

**Key Skills & Concepts Covered:**
- ✅ **Folder Connector Advanced Filtering**
- ✅ **Filtering by Extension (.xlsx only)**
- ✅ **Excluding Hidden & Lock Files (~$*)**
- ✅ **Dynamic Folder Consolidation**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = Folder.Files("C:\Data"),
#"Filtered Files" = Table.SelectRows(Source, each [Extension] = ".xlsx" and not Text.StartsWith([Name], "~$"))
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Case study.pbix`** (`81,924` bytes)
- 📄 **`New Bitmap Image.bmp`** (`0` bytes)
- 📄 **`New Microsoft Excel Worksheet.xlsx`** (`5,739` bytes)
- 📄 **`New Microsoft PowerPoint Presentation.pptx`** (`0` bytes)
- 📄 **`New Microsoft Word Document.docx`** (`0` bytes)
- 📄 **`New Text Document.txt`** (`0` bytes)
- 📄 **`Year - 2005.xlsx`** (`16,521` bytes)
- 📄 **`Year - 2006.xlsx`** (`15,846` bytes)
- 📄 **`Year - 2007.xlsx`** (`17,047` bytes)
- 📄 **`Year - 2008.xlsx`** (`16,384` bytes)
- 📄 **`Year - 2009.xlsx`** (`19,769` bytes)

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

[⬅️ Previous: Ep56-Multi-Source-Integration-and-Modeling](../../06-Case-Studies/Ep56-Multi-Source-Integration-and-Modeling/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep58-Hardcode-vs-Logic ➡️](../../06-Case-Studies/Ep58-Hardcode-vs-Logic/README.md)
