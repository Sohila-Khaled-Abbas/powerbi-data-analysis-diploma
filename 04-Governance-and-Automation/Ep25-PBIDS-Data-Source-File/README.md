# Episode 25: PBIDS (Power BI Data Source File)

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `04-Governance-and-Automation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 25** | PBIDS (Power BI Data Source File) | `21m 2s` | [Watch on YouTube](https://www.youtube.com/watch?v=QG_omh_AMu8) | [Download Sample Data](https://drive.google.com/drive/folders/1MHSgZ5UkhB1iov0vcunu_lCxgdJFg1fV?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Creating and distributing PBIDS (Power BI Data Source) files. Explains how enterprise BI administrators pre-configure connection strings, database credentials, and catalogs for business users.

**Key Skills & Concepts Covered:**
- ✅ **PBIDS JSON Specification**
- ✅ **Standardizing Enterprise Connections**
- ✅ **One-Click Data Onboarding for Analysts**
- ✅ **Deploying Pre-configured Sources**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
{
  "version": "0.1",
  "connections": [
    {
      "details": {
        "protocol": "sql",
        "address": {"server": "db.corp.net", "database": "Analytics"}
      },
      "connectionType": "Sql"
    }
  ]
}
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

[⬅️ Previous: Ep24-Permissions-Credential-Encryption-Privacy](../../04-Governance-and-Automation/Ep24-Permissions-Credential-Encryption-Privacy/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep26-Endorsement-and-Discovery ➡️](../../04-Governance-and-Automation/Ep26-Endorsement-and-Discovery/README.md)
