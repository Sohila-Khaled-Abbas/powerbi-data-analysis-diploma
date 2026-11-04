# Episodes 30 - 31: Parameters | Ep. 30 | Microsoft Power BI Data Analysis Diploma

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `04-Governance-and-Automation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 30** | Parameters | Ep. 30 | Microsoft Power BI Data Analysis Diploma | `14m 52s` | [Watch on YouTube](https://www.youtube.com/watch?v=OyhTs6jhBcM) | [Download Sample Data](https://drive.google.com/drive/folders/1v0-vZc1s-knXknWIxtitUEUBnNPL2jXO?usp=sharing) |
| **Ep. 31** | Templates & Parameters | Ep. 31 | Microsoft Power BI Data Analysis Diploma | `21m 18s` | [Watch on YouTube](https://www.youtube.com/watch?v=xmFHUOsRBmI) | [Download Sample Data](https://docs.google.com/spreadsheets/d/1XiQ0E58f1yB_Ib6l8uJrZKp29m5gNRx8/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

### Part 30: Parameters | Ep. 30 | Microsoft Power BI Data Analysis Diploma

Creating and managing Power Query Parameters. Demonstrates dynamic filtering, parameterizing file paths, server names, database names, and threshold values.

**Key Skills & Concepts Covered:**
- ✅ **Creating Parameters in Power Query**
- ✅ **Dynamic File Path Configuration**
- ✅ **List & Query-based Parameter Suggestions**
- ✅ **Enabling Self-Service Parameter Updates**

### Part 31: Templates & Parameters | Ep. 31 | Microsoft Power BI Data Analysis Diploma

Building Power BI Templates (.pbit) combined with dynamic parameters. Shows how to distribute lightweight report definitions without data, prompting users for parameters upon launch.

**Key Skills & Concepts Covered:**
- ✅ **Exporting .pbit Template Files**
- ✅ **Template Deployment Workflows**
- ✅ **Runtime Parameter Prompting**
- ✅ **Securing Proprietary Data in Templates**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

#### Episode 30 Code Reference:

```powerquery
Source = Excel.Workbook(File.Contents(FilePathParameter), null, true)
```

#### Episode 31 Code Reference:

```powerquery
// .pbit saves report schema, visuals, and queries without data
// When opened, prompts for parameters (e.g., Year, ClientID, Path)
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📂 **`Change DataSource/`** (Directory containing 3 dataset files)
- 📄 **`Essam Elsayad 13May26.xlsx`** (`17,524,657` bytes)
- 📄 **`New Template.pbit`** (`24,776` bytes)

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

[⬅️ Previous: Ep28-29-Data-Source-Connections-Storage-Modes](../../04-Governance-and-Automation/Ep28-29-Data-Source-Connections-Storage-Modes/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep32-33-Different-Data-Types ➡️](../../05-Data-Transformation/Ep32-33-Different-Data-Types/README.md)
