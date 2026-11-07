# Episode 27: Power Platform (Data Flows)

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `04-Governance-and-Automation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 27** | Power Platform (Data Flows) | `30m 20s` | [Watch on YouTube](https://www.youtube.com/watch?v=7JjoYsJgWUE) | [Download Sample Data](https://docs.google.com/spreadsheets/d/16Uw12kENYL8EpVsSrruz5FjdoqOdiWfG/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |

---

## 🎯 Lesson Overview & Objectives

Building reusable ETL pipelines with Power Platform Dataflows. Explains creating cloud-based Power Query transformations in Power BI Service and sharing unified tables across reports.

**Key Skills & Concepts Covered:**
- ✅ **Cloud Dataflows in Power BI Service**
- ✅ **Reusing ETL Across Multiple Reports**
- ✅ **Incremental Refresh in Dataflows**
- ✅ **Decoupling ETL from Report Development**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
Source = PowerBI.Dataflows(),
Workspace = Source{[workspaceId="..."]}[Data]
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

[⬅️ Previous: Ep26-Endorsement-and-Discovery](../../04-Governance-and-Automation/Ep26-Endorsement-and-Discovery/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep28-29-Data-Source-Connections-Storage-Modes ➡️](../../04-Governance-and-Automation/Ep28-29-Data-Source-Connections-Storage-Modes/README.md)
