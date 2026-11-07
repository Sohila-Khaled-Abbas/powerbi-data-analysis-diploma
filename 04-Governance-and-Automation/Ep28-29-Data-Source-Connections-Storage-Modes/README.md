# Episodes 28 - 29: Data Source Connections (Import, Direct & Live)

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `04-Governance-and-Automation`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 28** | Data Source Connections (Import, Direct & Live) | `21m 30s` | [Watch on YouTube](https://www.youtube.com/watch?v=bVJ7fH16a3M) | Included in repo / Follow lecture |
| **Ep. 29** | Dual Mode Connection | `12m 41s` | [Watch on YouTube](https://www.youtube.com/watch?v=Ygw7a4RRQ-I) | Included in repo / Follow lecture |

---

## 🎯 Lesson Overview & Objectives

### Part 28: Data Source Connections (Import, Direct & Live) | Ep. 28 | Microsoft Power BI Data Analysis Diploma

Deep dive into Power BI Storage Modes: Import Mode, DirectQuery Mode, and Live Connection. Explains performance trade-offs, caching, refresh limits, and DAX/Power Query restrictions.

**Key Skills & Concepts Covered:**
- ✅ **Import vs DirectQuery vs Live Connection**
- ✅ **VertiPaq In-Memory Compression**
- ✅ **Real-Time Querying with DirectQuery**
- ✅ **Storage Mode Selection Matrix**

### Part 29: Dual Mode Connection | Ep. 29 | Microsoft Power BI Data Analysis Diploma

Dual Mode Connections and Composite Models. Explains how tables can act as both DirectQuery and Import to optimize query performance and enable aggregation tables.

**Key Skills & Concepts Covered:**
- ✅ **Dual Storage Mode Configuration**
- ✅ **Composite Models Architecture**
- ✅ **Aggregation Tables Optimization**
- ✅ **Avoiding DirectQuery Performance Pitfalls**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

#### Episode 28 Code Reference:

```powerquery
// Import Mode: High speed in-memory VertiPaq engine
// DirectQuery: Pushes queries to source, no cache
// Live Connection: Direct connection to SSAS or Semantic Model
```

#### Episode 29 Code Reference:

```powerquery
// Dual Mode: Caches data for visual aggregations,
// falls back to DirectQuery for detail drills
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

[⬅️ Previous: Ep27-Power-Platform-Dataflows](../../04-Governance-and-Automation/Ep27-Power-Platform-Dataflows/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep30-31-Parameters-and-Templates ➡️](../../04-Governance-and-Automation/Ep30-31-Parameters-and-Templates/README.md)
