# Episode 55: Full Project from Multiple Data Sources

> **Course:** Microsoft Power BI Data Analysis Diploma (دبلومة تحليل البيانات)  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Module:** `06-Case-Studies`

---

## 📺 Video Information

| Episode | Title | Duration | YouTube Link | Official Sample Data |
|:-------:|:------|:--------:|:------------:|:--------------------:|
| **Ep. 55** | Full Project from Multiple Data Sources | `54m 33s` | [Watch on YouTube](https://www.youtube.com/watch?v=AcT5yK_oLMc) | [Download Sample Data](https://drive.google.com/drive/folders/1EO16UVQNId0DdowPc_8HTCl7FvEvae49?usp=sharing) |

---

## 🎯 Lesson Overview & Objectives

Comprehensive Capstone Project: Full BI Pipeline from Multiple Data Sources. Integrates Customer database, Product catalog, and regional Sales databases into an end-to-end model.

**Key Skills & Concepts Covered:**
- ✅ **Multi-Source Ingestion Architecture**
- ✅ **Building Star Schema Fact & Dimension Tables**
- ✅ **Establishing 1:Many Relationships in Power BI**
- ✅ **End-to-End Analytical Reporting**

---

## 💡 Key Technical Notes & Formulas / M Language Snippets

```powerquery
// End-to-end model with DimCustomer, DimProduct, and FctSales
```

---

## 📁 Practice Files in this Repository

This episode folder contains the following hands-on practice assets:

- 📄 **`Customer Database.xlsx`** (`16.8 KB (17,155 bytes)`) — Excel practice dataset
- 📄 **`Product Database.xlsx`** (`35.1 KB (35,992 bytes)`) — Excel practice dataset
- 📄 **`Sales Database.xlsx`** (`2.5 MB (2,600,046 bytes)`) — Excel practice dataset
- 📊 **`SalesFullProject.pbix`** (`687.4 KB (703,944 bytes)`) — Power BI Desktop solution model

> 💡 **How to use:** Open `.pbix` files in **Microsoft Power BI Desktop**; and Open `.xlsx` files in **Microsoft Excel** to inspect source tables, verify data types, and follow along with the transformations.
---

## 📝 Self-Study & Hands-On Practice Checklist

- [ ] Watch the lecture video carefully and take notes.
- [ ] Replicate the Power Query transformations step-by-step.
- [ ] Verify the column data types and ensure no errors in the Applied Steps window.
- [ ] Check Query Folding status (right-click final step -> *View Native Query* where applicable).
- [ ] Apply and close into the Data Model and verify table relationships.

---

## 🧭 Independent Practice: Validate the Model Before Building Reports

The course project integrates customer, product, and sales sources. Use this exercise to test the model design rather than assuming similarly named columns guarantee correct relationships.

~~~mermaid
flowchart LR
    C["Customer source"] --> DC["DimCustomer"]
    P["Product source"] --> DP["DimProduct"]
    S["Sales source"] --> F["FactSales"]
    DC --> F
    DP --> F
    D["Date dimension<br/>(if required by analysis)"] --> F
~~~

**Practice sequence**

1. Profile each workbook independently.
2. Write a grain statement for each table. For sales, determine whether a row is an order, order line, or another level.
3. Identify candidate keys and test nulls and duplicates.
4. Check dimension-key uniqueness before creating one-to-many relationships.
5. Reconcile a business total from source sales to the transformed fact table.
6. Record rejected rows, unmatched keys, and assumptions.

**Model validation checklist**

- [ ] Fact-table grain is documented.
- [ ] Dimension keys are unique on the one-side.
- [ ] Fact foreign keys have been checked for unmatched values.
- [ ] Relationships do not create unexpected many-to-many behavior.
- [ ] Source and model totals reconcile at the same grain.
- [ ] A date dimension is included only when the source and analysis require it.

> This is an independent modeling exercise. Determine exact field names, granularity, and relationships from the supplied source files; the illustrative names above are not a claim about every field in the lecture data.

## 🧭 Navigation

[⬅️ Previous: Ep54-Complex-Header-Structure](../../06-Case-Studies/Ep54-Complex-Header-Structure/README.md) | [📂 Module Overview](../README.md) | [🏠 Main Course Catalog](../../README.md) | [Next: Ep56-Multi-Source-Integration-and-Modeling ➡️](../../06-Case-Studies/Ep56-Multi-Source-Integration-and-Modeling/README.md)
