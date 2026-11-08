# Module 07: Power Query Engine Internals & Advanced M Language

### محرك باور كويري ولغة إم (M Language) المتقدمة

> **Diploma:** Microsoft Power BI Data Analysis Diploma  
> **Instructor:** Essam Elsayed (عصام الصياد) - Microsoft Certified Trainer  
> **Total Lectures in Module:** `17`

---

## 📖 Module Overview

Become an elite Power Query architect by mastering M Language code and engine internals. Understand Null vs Blank semantics, Cartesian join scenarios, preserving Query Folding, step vs cell error isolation, functional M language foundations, custom functions, modular helper query architectures, missing field resilience, floating-point rounding compliance, dynamic worksheet ingestion, bulk column transformations, null coalescing (??), and defensive try...otherwise exception handling.

### 🎯 Key Competencies Acquired:

- 🌟 **Engine Deep-Dive: Null vs Blank vs DAX BLANK() Semantics**
- 🌟 **Query Folding Preservation & Safe vs Breaking Changes**
- 🌟 **Step Errors vs Cell Errors (Auditing & Repairing Pipeline Exceptions)**
- 🌟 **M Language Fundamentals (Lists, Records, Tables, Lambda Functions)**
- 🌟 **Architecting Modular Helper Queries & Decoupled Pipelines**
- 🌟 **Writing Typed Reusable M Functions with Metadata**
- 🌟 **MissingField Enumeration & Resilient Dynamic Ingestion**
- 🌟 **Bulk Column Processing with Table.TransformColumns**
- 🌟 **Null Coalescing Operator (??) & Try ... Otherwise Defensive Programming**

---

## 📚 Lessons in this Module

| Ep # | Lesson Title | Duration | Hands-On Folder | Watch Video | Practice Data |
|:----:|:-------------|:--------:|:---------------:|:-----------:|:-------------:|
| **65** | Null vs. Blank – Full Explanation | `16m 58s` | [Ep65-Null-vs-Blank](Ep65-Null-vs-Blank/README.md) | [YouTube](https://www.youtube.com/watch?v=wlSBLPL50rM) | Included |
| **66** | Cartesian Join | `12m 1s` | [Ep66-Cartesian-Join](Ep66-Cartesian-Join/README.md) | [YouTube](https://www.youtube.com/watch?v=RFDEx47xQa0) | [Sample Data](https://docs.google.com/spreadsheets/d/1sB34uqMVhycmQ1xb7NlFuTUajHVR0Zje/edit?gid=1957227644#gid=1957227644) |
| **67** | Safe vs. Breaking Changes | `25m 21s` | [Ep67-Safe-vs-Breaking-Changes](Ep67-Safe-vs-Breaking-Changes/README.md) | [YouTube](https://www.youtube.com/watch?v=g4b3S3rLQr8) | [Sample Data](https://drive.google.com/drive/folders/1IQYx_NGw08X73OkgYzFmhK5EsP5ONvKr) |
| **68** | Step Error vs. Cell Error | `8m 18s` | [Ep68-Step-Error-vs-Cell-Error](Ep68-Step-Error-vs-Cell-Error/README.md) | [YouTube](https://www.youtube.com/watch?v=NdSx5_WQcz8) | [Sample Data](https://docs.google.com/spreadsheets/d/1CcnHY9sxUNkobYEX_GL2RMbIKtKhGqrK/edit?gid=1998078071#gid=1998078071) |
| **69** | M Language (Theory) | `1h 16m 20s` | [Ep69-70-M-Language-Fundamentals](Ep69-70-M-Language-Fundamentals/README.md) | [YouTube](https://www.youtube.com/watch?v=DeJi6omk5Dk) | [Sample Data](https://drive.google.com/file/d/15EEPsaZEM5xnlh3uwgLZ7Avb-k5D8keg/view?usp=sharing) |
| **70** | M Language | `33m 6s` | [Ep69-70-M-Language-Fundamentals](Ep69-70-M-Language-Fundamentals/README.md) | [YouTube](https://www.youtube.com/watch?v=KNfHFcJUQOs) | [Sample Data](https://docs.google.com/spreadsheets/d/1mGOJ_w5ZzEraxZR_CvoYwuK682ZBqzt_/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |
| **71** | Practical Exercise - 3 | `46m 57s` | [Ep71-Practical-Exercise-3](Ep71-Practical-Exercise-3/README.md) | [YouTube](https://www.youtube.com/watch?v=c9XF4QnYAY4) | [Sample Data](https://docs.google.com/spreadsheets/d/1BGjNardWbcEpFkZerwt_hH6K9RW4m1TM/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |
| **72** | Helper Queries | `16m 32s` | [Ep72-Helper-Queries](Ep72-Helper-Queries/README.md) | [YouTube](https://www.youtube.com/watch?v=ESZie6P1VxA) | [Sample Data](https://drive.google.com/drive/folders/1OPwJ6BQ2JjcR9KWb5-eqOiLiXLcDBqn1?usp=sharing) |
| **73** | Build Custom Functions | `19m 1s` | [Ep73-Build-Custom-Functions](Ep73-Build-Custom-Functions/README.md) | [YouTube](https://www.youtube.com/watch?v=IpBJqY3zctE) | [Sample Data](https://docs.google.com/spreadsheets/d/1iEJblGG-g1TSAq6L9AmCoqYe1i49JTJo/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |
| **74** | Frequency vs. Sequence Analysis | `15m 23s` | [Ep74-Frequency-vs-Sequence-Analysis](Ep74-Frequency-vs-Sequence-Analysis/README.md) | [YouTube](https://www.youtube.com/watch?v=CfpKqBiO8Kg) | [Sample Data](https://docs.google.com/spreadsheets/d/1RG09LGg3W60frQHKlZycLTfGzvJ0kp_c/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |
| **75** | Missing Fields | `11m 35s` | [Ep75-Missing-Fields](Ep75-Missing-Fields/README.md) | [YouTube](https://www.youtube.com/watch?v=Yc8WkhRb60U) | [Sample Data](https://docs.google.com/spreadsheets/d/1Mbg4Q5f3dsaGUzJk_yv-7gWaFcSp469J/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |
| **76** | Away From Zero | `10m 4s` | [Ep76-Away-From-Zero](Ep76-Away-From-Zero/README.md) | [YouTube](https://www.youtube.com/watch?v=o2uAwvLCRmY) | [Sample Data](https://docs.google.com/spreadsheets/d/1oLnk44t2QSLCh6qFQWdLrK2xlFoLx8YH/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |
| **77** | The Logic of Thinking | `9m 33s` | [Ep77-The-Logic-of-Thinking](Ep77-The-Logic-of-Thinking/README.md) | [YouTube](https://www.youtube.com/watch?v=XJ2KWWGTujA) | [Sample Data](https://docs.google.com/spreadsheets/d/1xJ602C-K787QzdsqGdMTMuwQNKTvrJ_o/edit?usp=sharing&ouid=114716248435075749833&rtpof=true&sd=true) |
| **78** | Worksheets Name | `11m 46s` | [Ep78-Worksheets-Name](Ep78-Worksheets-Name/README.md) | [YouTube](https://www.youtube.com/watch?v=uyA9C7m0UYY) | [Sample Data](https://drive.google.com/drive/folders/1Z7sVUu5XuWCWP-gEJujWYs8q7GYHd5sa?usp=sharing) |
| **79** | Transform All Columns | `13m 43s` | [Ep79-Transform-All-Columns](Ep79-Transform-All-Columns/README.md) | [YouTube](https://www.youtube.com/watch?v=lNIszvvtH20) | [Sample Data](https://docs.google.com/spreadsheets/d/17x2adhYI77emsOD1O2lXztQ8JPgoqNL6/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |
| **80** | Null Coalescing Operator | `9m 17s` | [Ep80-Null-Coalescing-Operator](Ep80-Null-Coalescing-Operator/README.md) | [YouTube](https://www.youtube.com/watch?v=Tf7yCfw9TeA) | [Sample Data](https://docs.google.com/spreadsheets/d/1h9TgU98uAohxtM3oss8usbNg2oL09F7z/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |
| **81** | Try & Otherwise | `12m 17s` | [Ep81-Try-and-Otherwise](Ep81-Try-and-Otherwise/README.md) | [YouTube](https://www.youtube.com/watch?v=YTZEzXVY8IA) | [Sample Data](https://docs.google.com/spreadsheets/d/1MCI_gLq5mbBFYjSXrsDS-Vq0ih8FF8jP/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |
| **82** | Reference Outside Scope | `8m 11s` | [Ep82-Reference-Outside-Scope](Ep82-Reference-Outside-Scope/README.md) | [YouTube](https://www.youtube.com/watch?v=M4sCUumYySA) | [Sample Data](https://docs.google.com/spreadsheets/d/1WS-2xNo4vVyKoo2OpGcu5sUT80aQNJ0B/edit?usp=sharing&ouid=106512834842891247892&rtpof=true&sd=true) |

---

## 🧭 Navigation

[⬅️ Previous: 06-Case-Studies](../06-Case-Studies/README.md) | [🏠 Course Home Page](../README.md) | [📊 Progress Tracker](../PROGRESS_TRACKER.md) | [⚡ M Language Cheatsheet](../M_LANGUAGE_CHEATSHEET.md)
