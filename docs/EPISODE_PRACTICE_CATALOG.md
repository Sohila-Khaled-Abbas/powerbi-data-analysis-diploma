# Episode-by-Episode Learning Resources

> A practical companion for all 83 lessons. Each episode below is written as a small learning lab: start from its actual tracked source files, rebuild the Power Query work, use an existing PBIX/PBIT only as a reference, and validate the result.

## Important note about the source files

The binary lesson assets are tracked with Git LFS (`.xlsx`, `.pbix`, `.pbit`, and `.pdf`). A normal GitHub text preview may show only a short LFS pointer; it does **not** expose worksheet contents, Power Query steps, model tables, measures, or report visuals. The guidance below uses the repository's real file inventory, the lesson README, and the stated episode objective. It does not invent sheet names, field names, DAX measures, query names, or visual titles.

After cloning the repository, run `git lfs install` once and `git lfs pull` to download the actual binary assets. If an episode lists no local workbook or PBIX, use the official sample-data link or connector/service linked in that episode's README. Do not mistake an LFS pointer stub for the real workbook.

## How to study each episode

1. **Preview the lesson page.** Read the objective and open the official video/sample-data links in the episode README.
2. **Inspect the source in Excel first.** Record the actual sheet/table names, headers, grain (what one row represents), key columns, data types, nulls, duplicates, and irregularities.
3. **Rebuild in Power Query.** Import the source into a new PBIX or a separate query. Reproduce the lesson's transformation without changing the original file.
4. **Use the reference PBIX after attempting the task.** Trace `Source` and `Applied Steps`, note why each step exists, and compare your output. Inspect Model view/report pages only when the episode actually includes a modeling/reporting outcome.
5. **Test the checkpoint and one extra edge case.** Examples include a new row, missing field, duplicate key, null, unexpected type, new worksheet, or a different locale.
6. **Save evidence.** Keep the M code or query screenshot, a small before/after sample, validation result, and a short explanation of the decision.

---

## Episode learning labs

### Ep. 01 · دبلومة تحليل البيانات - المحاضرة (١) - مقدمة

**Lesson notes:** [Open the episode README](<../01-Data-Foundations/Ep01-Introduction/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Sketch the BI workflow from source data to a decision; identify where Power Query and the semantic model fit.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Explain the purpose of each stage without describing only button clicks.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 02 · Proper Raw Data Structure

**Lesson notes:** [Open the episode README](<../01-Data-Foundations/Ep02-Proper-Raw-Data-Structure/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Inspect a raw table and state its grain, one-row meaning, identifier columns, and observation columns.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Flag repeated headers, totals mixed with records, merged cells, and multiple values in one field.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 03 · Get Data From Microsoft Excel

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep03-Get-Data-From-Excel/README.md>)

**Actual files tracked in this lesson folder:**

- [`3. Countries Database.xlsx`](<../02-Data-Acquisition/Ep03-Get-Data-From-Excel/3.%20Countries%20Database.xlsx>) — Excel workbook
- [`4. Employees Datebase/Administration.xlsx`](<../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Administration.xlsx>) — Excel workbook
- [`4. Employees Datebase/Business Development.xlsx`](<../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Business%20Development.xlsx>) — Excel workbook
- [`4. Employees Datebase/Customer Service.xlsx`](<../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Customer%20Service.xlsx>) — Excel workbook
- [`4. Employees Datebase/Finance.xlsx`](<../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Finance.xlsx>) — Excel workbook
- [`4. Employees Datebase/Human Resources.xlsx`](<../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Human%20Resources.xlsx>) — Excel workbook
- [`4. Employees Datebase/IT.xlsx`](<../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/IT.xlsx>) — Excel workbook
- [`4. Employees Datebase/Legal.xlsx`](<../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Legal.xlsx>) — Excel workbook

**Excel workbook study**

Open the 8 Excel workbook(s) listed above. Inspect each file independently before combining anything. Compare sheet/table names, column names, data types, row grain, and overlapping fields. Decide whether these are separate source partitions, different entities, or alternative layouts; only combine files after confirming their structure is compatible.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Open the workbook navigator; compare a structured Excel Table with a worksheet object and select the intended source.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Add a row to the table and refresh; confirm the new record is included and unrelated objects are excluded.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 04 · Get Data From CSV Files

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/README.md>)

**Actual files tracked in this lesson folder:**

- [`1. csv Employees.csv`](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/1.%20csv%20Employees.csv>) — CSV source
- [`2. txt Customers.txt`](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/2.%20txt%20Customers.txt>) — text source
- [`3. csv Employees With Summary Header.csv`](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/3.%20csv%20Employees%20With%20Summary%20Header.csv>) — CSV source
- [`4. csv Employees With Quotes.csv`](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/4.%20csv%20Employees%20With%20Quotes.csv>) — CSV source
- [`5. CSV Extract From Example.csv`](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/5.%20CSV%20Extract%20From%20Example.csv>) — CSV source

**Other source-file study**

For `1. csv Employees.csv`, `3. csv Employees With Summary Header.csv`, `4. csv Employees With Quotes.csv`, `5. CSV Extract From Example.csv`, inspect delimiter, encoding, quoting, header rows, line breaks, and locale before loading. Compare the parsed row and column counts with the raw file.
For `2. txt Customers.txt`, inspect the raw text layout, delimiters, headers, and record boundaries. Decide how the file should be parsed before promoting headers or assigning types.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Import the CSV and test delimiter, encoding, quote style, and header handling.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Compare row/column counts with the raw file and inspect values containing embedded delimiters.

**Evidence to keep**

Save a reproducible query, small output sample, and assumptions/edge-case notes. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 05 · Fixing CSV Import Issues

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/README.md>)

**Actual files tracked in this lesson folder:**

- [`1. csv Employees.csv`](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/1.%20csv%20Employees.csv>) — CSV source
- [`2. txt Customers.txt`](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/2.%20txt%20Customers.txt>) — text source
- [`3. csv Employees With Summary Header.csv`](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/3.%20csv%20Employees%20With%20Summary%20Header.csv>) — CSV source
- [`4. csv Employees With Quotes.csv`](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/4.%20csv%20Employees%20With%20Quotes.csv>) — CSV source
- [`5. CSV Extract From Example.csv`](<../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/5.%20CSV%20Extract%20From%20Example.csv>) — CSV source

**Other source-file study**

For `1. csv Employees.csv`, `3. csv Employees With Summary Header.csv`, `4. csv Employees With Quotes.csv`, `5. CSV Extract From Example.csv`, inspect delimiter, encoding, quoting, header rows, line breaks, and locale before loading. Compare the parsed row and column counts with the raw file.
For `2. txt Customers.txt`, inspect the raw text layout, delimiters, headers, and record boundaries. Decide how the file should be parsed before promoting headers or assigning types.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Reproduce a malformed CSV import using the supplied variants; adjust parsing options rather than manually editing the source.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Confirm quoted fields, summary lines, and headers are parsed as intended.

**Evidence to keep**

Save a reproducible query, small output sample, and assumptions/edge-case notes. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 06 · Get Data From PDFs

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/README.md>)

**Actual files tracked in this lesson folder:**

- [`2. Employees Database/Abdullah Alomary.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Abdullah%20Alomary.pdf>) — PDF source
- [`2. Employees Database/Abeer Mohamed.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Abeer%20Mohamed.pdf>) — PDF source
- [`2. Employees Database/Ahmed Ezzat.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Ahmed%20Ezzat.pdf>) — PDF source
- [`2. Employees Database/Ahmed Yousef.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Ahmed%20Yousef.pdf>) — PDF source
- [`2. Employees Database/Amal Abdelfatah.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Amal%20Abdelfatah.pdf>) — PDF source
- [`2. Employees Database/Amal Mohamed.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Amal%20Mohamed.pdf>) — PDF source
- [`2. Employees Database/Azza Abdelrahman.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Azza%20Abdelrahman.pdf>) — PDF source
- [`2. Employees Database/Berry Hassan.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Berry%20Hassan.pdf>) — PDF source
- [`2. Employees Database/Essam Elsayad.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Essam%20Elsayad.pdf>) — PDF source
- [`2. Employees Database/Hala Ahmed.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Hala%20Ahmed.pdf>) — PDF source
- [`2. Employees Database/Hassan Abdelrahman.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Hassan%20Abdelrahman.pdf>) — PDF source
- [`2. Employees Database/Mahmoud Hamouda.pdf`](<../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Mahmoud%20Hamouda.pdf>) — PDF source

**Other source-file study**

For `2. Employees Database/Abdullah Alomary.pdf`, `2. Employees Database/Abeer Mohamed.pdf`, `2. Employees Database/Ahmed Ezzat.pdf`, `2. Employees Database/Ahmed Yousef.pdf`, `2. Employees Database/Amal Abdelfatah.pdf`, `2. Employees Database/Amal Mohamed.pdf`, `2. Employees Database/Azza Abdelrahman.pdf`, `2. Employees Database/Berry Hassan.pdf`, `2. Employees Database/Essam Elsayad.pdf`, `2. Employees Database/Hala Ahmed.pdf`, `2. Employees Database/Hassan Abdelrahman.pdf`, `2. Employees Database/Mahmoud Hamouda.pdf`, inspect the PDF pages and table layouts. Identify repeated page headers, columns that shift between pages/files, and values that need reconciliation after extraction.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Extract a tabular section from the employee PDFs and inspect repeated headers and page boundaries.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Compare extracted records with source pages; check missing/duplicated rows.

**Evidence to keep**

Save a reproducible query, small output sample, and assumptions/edge-case notes. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 07 · On-Premises Data Gateway

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep07-On-Premises-Data-Gateway/README.md>)

**Actual files tracked in this lesson folder:**

- [`Essam Elsayad Gateway.xlsx`](<../02-Data-Acquisition/Ep07-On-Premises-Data-Gateway/Essam%20Elsayad%20Gateway.xlsx>) — Excel workbook

**Excel workbook study**

Open `Essam Elsayad Gateway.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Map the on-premises gateway path from data source to Power BI Service refresh.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Document gateway dependency, credentials, source reachability, and a safe refresh test.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 08 · Get Data From OneDrive

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep08-Get-Data-From-OneDrive/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Connect to a OneDrive-hosted file and distinguish the cloud path from a local synced path.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Change the source file and verify refresh behavior without hardcoding a machine-specific path.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 09 · Get Data From SharePoint

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep09-Get-Data-From-SharePoint/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Connect to a SharePoint document library and filter to the intended file.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Verify site/library/file identity and test a refresh after a file update.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 10 · Get Data From Google Sheets

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep10-Get-Data-From-Google-Sheets/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Connect to a Google Sheet and inspect its tabular structure and access requirements.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Verify header row, column types, and whether the connector returns the expected worksheet.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 11 · Get Data From Google Drive

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep11-Get-Data-From-Google-Drive/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Connect to a Google Drive file and compare the selected object with the intended source.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Record authentication and refresh constraints; confirm file identity.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 12 · Get Data From Database (SQL / Oracle / SAP)

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep12-Get-Data-From-Database/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Connect to a relational source and inspect native query/folding indicators where supported by the connector.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Validate row counts and key filters; distinguish source-side operations from local transformations.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 13 · Get Data From Semantic Models

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep13-Get-Data-From-Semantic-Models/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Connect to a published semantic model and identify what is reusable versus what cannot be transformed locally.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Explain the difference between consuming a governed model and importing raw source tables.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 14 · Get Data From Microsoft Exchange

**Lesson notes:** [Open the episode README](<../02-Data-Acquisition/Ep14-Get-Data-From-Microsoft-Exchange/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Inspect the mailbox/attachment ingestion pattern and identify which messages or attachments should be included.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test duplicate attachments, unexpected file types, and privacy/credential boundaries.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 15 · Get Data From Web

**Lesson notes:** [Open the episode README](<../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/README.md>)

**Actual files tracked in this lesson folder:**

- [`get data from web.pbix`](<../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/get%20data%20from%20web.pbix>) — Power BI Desktop project

**Power BI reference project study**

Open `get data from web.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Extract a web table and inspect how page structure maps to rows and columns.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check row count, repeated headings, and whether a website layout change breaks the query.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 16 · Get Data From Web (Invoke)

**Lesson notes:** [Open the episode README](<../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/README.md>)

**Actual files tracked in this lesson folder:**

- [`get data from web.pbix`](<../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/get%20data%20from%20web.pbix>) — Power BI Desktop project

**Power BI reference project study**

Open `get data from web.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Turn a repeated web extraction into a parameterized function and invoke it for multiple inputs.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Compare outputs across inputs and confirm consistent schemas.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 17 · Get Data From Web (List)

**Lesson notes:** [Open the episode README](<../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/README.md>)

**Actual files tracked in this lesson folder:**

- [`get data from web.pbix`](<../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/get%20data%20from%20web.pbix>) — Power BI Desktop project

**Power BI reference project study**

Open `get data from web.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Iterate over multiple web pages or result sets and combine the returned tables.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check termination, duplicate pages, missing pages, and consistent columns.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 18 · Get Data From API

**Lesson notes:** [Open the episode README](<../03-Advanced-Data-Extraction/Ep18-19-Get-Data-From-API/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Build a request to an API endpoint and inspect status, headers, and response shape.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test a failed response and verify the parsed record/list structure.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 19 · Get Data From API (List. Generate)

**Lesson notes:** [Open the episode README](<../03-Advanced-Data-Extraction/Ep18-19-Get-Data-From-API/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Use List.Generate or an equivalent controlled loop to retrieve pages until the stop condition is met.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check page termination, repeated cursors, rate limits, and duplicate records.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 20 · Get Data From LinkedIn

**Lesson notes:** [Open the episode README](<../03-Advanced-Data-Extraction/Ep20-Get-Data-From-LinkedIn/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Review the LinkedIn source approach and identify current API/access limitations before attempting a live connection.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Separate reproducible query logic from credentials, permissions, and platform policy.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 21 · Get Data From X (Twitter)

**Lesson notes:** [Open the episode README](<../03-Advanced-Data-Extraction/Ep21-Get-Data-From-X-Twitter/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Review the X/Twitter source approach and identify current API/access limitations before attempting a live connection.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Separate reproducible query logic from credentials, permissions, and platform policy.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 22 · Get Data From Dataverse

**Lesson notes:** [Open the episode README](<../03-Advanced-Data-Extraction/Ep22-Get-Data-From-Dataverse/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Explore Dataverse entities and identify the table relationships and columns required for the scenario.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check entity selection, key fields, and permission boundaries.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 23 · Get Data From JSON - Facebook - Instagram

**Lesson notes:** [Open the episode README](<../03-Advanced-Data-Extraction/Ep23-Get-Data-From-JSON/README.md>)

**Actual files tracked in this lesson folder:**

- [`Essam Elsayad.json`](<../03-Advanced-Data-Extraction/Ep23-Get-Data-From-JSON/Essam%20Elsayad.json>) — JSON source

**Other source-file study**

For `Essam Elsayad.json`, inspect the JSON hierarchy first: identify records, lists, nested objects, repeated arrays, and optional fields. Expand one level at a time and preserve identifiers when normalizing the structure.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Expand the supplied JSON from its outer record/list into a tabular shape while preserving identifiers.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test optional/missing fields and verify nested list expansion does not multiply rows unexpectedly.

**Evidence to keep**

Save a reproducible query, small output sample, and assumptions/edge-case notes. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 24 · Permissions (Credential - Encryption - Privacy)

**Lesson notes:** [Open the episode README](<../04-Governance-and-Automation/Ep24-Permissions-Credential-Encryption-Privacy/README.md>)

**Actual files tracked in this lesson folder:**

- [`Permissions (Credential, Encryption & Privacy).pdf`](<../04-Governance-and-Automation/Ep24-Permissions-Credential-Encryption-Privacy/Permissions%20(Credential%2C%20Encryption%20%26%20Privacy).pdf>) — PDF source
- [`csv_employees.csv`](<../04-Governance-and-Automation/Ep24-Permissions-Credential-Encryption-Privacy/csv_employees.csv>) — CSV source

**Other source-file study**

For `Permissions (Credential, Encryption & Privacy).pdf`, inspect the PDF pages and table layouts. Identify repeated page headers, columns that shift between pages/files, and values that need reconciliation after extraction.
For `csv_employees.csv`, inspect delimiter, encoding, quoting, header rows, line breaks, and locale before loading. Compare the parsed row and column counts with the raw file.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Inspect privacy levels, credentials, and encryption settings for the supplied source scenario.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Explain why privacy/firewall behavior changes across source combinations; never commit credentials.

**Evidence to keep**

Save a reproducible query, small output sample, and assumptions/edge-case notes. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 25 · PBIDS (Power BI Data Source File)

**Lesson notes:** [Open the episode README](<../04-Governance-and-Automation/Ep25-PBIDS-Data-Source-File/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Inspect the PBIDS concept and build a minimal source-definition file for a safe sample connection.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Validate file syntax and confirm it identifies the intended source without embedding secrets.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 26 · Endorsement & Discovery

**Lesson notes:** [Open the episode README](<../04-Governance-and-Automation/Ep26-Endorsement-and-Discovery/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Compare promoted and certified endorsement and identify how discovery metadata supports governed reuse.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Explain who can endorse content and what evidence a consumer should expect.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 27 · Power Platform (Data Flows)

**Lesson notes:** [Open the episode README](<../04-Governance-and-Automation/Ep27-Power-Platform-Dataflows/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Map the dataflow as a reusable cloud ETL layer and identify ownership/refresh boundaries.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Document source credentials, refresh dependencies, and downstream consumers.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 28 · Data Source Connections (Import, Direct & Live)

**Lesson notes:** [Open the episode README](<../04-Governance-and-Automation/Ep28-29-Data-Source-Connections-Storage-Modes/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Compare Import, DirectQuery, and Live Connection for the same analytical requirement.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Explain storage, latency, transformation, and model-authoring trade-offs.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 29 · Dual Mode Connection

**Lesson notes:** [Open the episode README](<../04-Governance-and-Automation/Ep28-29-Data-Source-Connections-Storage-Modes/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Inspect Dual storage mode and identify when a table can participate in composite model behavior.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Explain expected query behavior and validate the model's storage-mode settings.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 30 · Parameters

**Lesson notes:** [Open the episode README](<../04-Governance-and-Automation/Ep30-31-Parameters-and-Templates/README.md>)

**Actual files tracked in this lesson folder:**

- [`New Template.pbit`](<../04-Governance-and-Automation/Ep30-31-Parameters-and-Templates/New%20Template.pbit>) — Power BI template

**Power BI template study**

Open `New Template.pbit` as a template. Inspect its parameter prompts and source configuration, instantiate a copy with safe test values, and verify the resulting connection. Keep the original template unchanged.

**Episode-specific task**

Create a parameter for a source value or file path and replace a hardcoded literal.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Change the parameter and verify the query points to the intended source.

**Evidence to keep**

Save a reproducible query, small output sample, and assumptions/edge-case notes. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 31 · Templates & Parameters

**Lesson notes:** [Open the episode README](<../04-Governance-and-Automation/Ep30-31-Parameters-and-Templates/README.md>)

**Actual files tracked in this lesson folder:**

- [`New Template.pbit`](<../04-Governance-and-Automation/Ep30-31-Parameters-and-Templates/New%20Template.pbit>) — Power BI template

**Power BI template study**

Open `New Template.pbit` as a template. Inspect its parameter prompts and source configuration, instantiate a copy with safe test values, and verify the resulting connection. Keep the original template unchanged.

**Episode-specific task**

Open the PBIT template and inspect its parameters and source prompts.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Instantiate the template with safe test values and verify no credentials are embedded.

**Evidence to keep**

Save a reproducible query, small output sample, and assumptions/edge-case notes. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 32 · Different Data Types (Theory)

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep32-33-Different-Data-Types/README.md>)

**Actual files tracked in this lesson folder:**

- [`datatypes.xlsx`](<../05-Data-Transformation/Ep32-33-Different-Data-Types/datatypes.xlsx>) — Excel workbook
- [`datatypes_info.xlsx`](<../05-Data-Transformation/Ep32-33-Different-Data-Types/datatypes_info.xlsx>) — Excel workbook

**Excel workbook study**

Open the 2 Excel workbook(s) listed above. Inspect each file independently before combining anything. Compare sheet/table names, column names, data types, row grain, and overlapping fields. Decide whether these are separate source partitions, different entities, or alternative layouts; only combine files after confirming their structure is compatible.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Inspect the supplied type examples and classify identifiers, dates, numbers, logical values, and text.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Identify conversions that can lose precision or change meaning.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 33 · Different Data Types

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep32-33-Different-Data-Types/README.md>)

**Actual files tracked in this lesson folder:**

- [`datatypes.xlsx`](<../05-Data-Transformation/Ep32-33-Different-Data-Types/datatypes.xlsx>) — Excel workbook
- [`datatypes_info.xlsx`](<../05-Data-Transformation/Ep32-33-Different-Data-Types/datatypes_info.xlsx>) — Excel workbook

**Excel workbook study**

Open the 2 Excel workbook(s) listed above. Inspect each file independently before combining anything. Compare sheet/table names, column names, data types, row grain, and overlapping fields. Decide whether these are separate source partitions, different entities, or alternative layouts; only combine files after confirming their structure is compatible.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Apply explicit data types and compare results before and after conversion.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check conversion errors, leading zeros in identifiers, and numeric/date interpretation.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 34 · Local Interpretation

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep34-Local-Interpretation/README.md>)

**Actual files tracked in this lesson folder:**

- [`csv_wideworldimporters.csv`](<../05-Data-Transformation/Ep34-Local-Interpretation/csv_wideworldimporters.csv>) — CSV source
- [`datatypes.xlsx`](<../05-Data-Transformation/Ep34-Local-Interpretation/datatypes.xlsx>) — Excel workbook

**Excel workbook study**

Open `datatypes.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Other source-file study**

For `csv_wideworldimporters.csv`, inspect delimiter, encoding, quoting, header rows, line breaks, and locale before loading. Compare the parsed row and column counts with the raw file.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Parse the supplied dates/numbers using the correct locale rather than relying on machine defaults.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test ambiguous dates and decimal/thousands separators; record the locale assumption.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 35 · Custom Columns

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep35-Custom-Columns/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Create a custom column from existing fields and document the expression's input/output types.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test nulls and unexpected values in the source columns.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 36 · Conditional Columns

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep36-Conditional-Columns/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Create conditional logic for mutually exclusive business rules and test boundary values.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check rule order, uncovered values, and overlapping conditions.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 37 · Columns from Examples

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep37-Columns-From-Examples/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Use Column From Examples on representative rows, then inspect the generated transformation logic.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test unseen patterns and edge cases; do not assume the inferred rule generalizes.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 38 · Split and Merge Columns

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep38-Split-and-Merge-Columns/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Split and merge fields using explicit delimiters and preserve original identifiers where needed.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test missing delimiters, repeated delimiters, and null values.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 39 · Invoke Custom Function

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep39-Invoke-Custom-Function/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Invoke a custom function over a table column and inspect row-level results.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check parameter types, error handling, and whether each input produces one expected output.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 40 · UnPivot Columns

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/README.md>)

**Actual files tracked in this lesson folder:**

- [`Unpivot & Pivot Columns.xlsx`](<../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/Unpivot%20%26%20Pivot%20Columns.xlsx>) — Excel workbook
- [`unpivot.pbix`](<../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/unpivot.pbix>) — Power BI Desktop project

**Excel workbook study**

Open `Unpivot & Pivot Columns.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `unpivot.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Unpivot the wide sample while retaining the correct identifier columns.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Confirm each output row represents one entity-period-value combination.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 41 · Pivot Columns

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/README.md>)

**Actual files tracked in this lesson folder:**

- [`Unpivot & Pivot Columns.xlsx`](<../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/Unpivot%20%26%20Pivot%20Columns.xlsx>) — Excel workbook
- [`unpivot.pbix`](<../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/unpivot.pbix>) — Power BI Desktop project

**Excel workbook study**

Open `Unpivot & Pivot Columns.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `unpivot.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Pivot the long result back to columns and choose an aggregation only when duplicate keys require it.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Reconcile values with the original wide table and explain any aggregation.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 42 · Double Headers Issue

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep42-Double-Headers-Issue/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Promote/repair multi-row headers and fill down grouping labels where appropriate.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check that every output column has a unique meaningful name and records retain their intended grain.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 43 · Append (Theory)

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep43-44-Append-Queries/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Compare source schemas before appending and identify missing/extra columns.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Explain how column names and data types affect the combined table.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 44 · Append

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep43-44-Append-Queries/README.md>)

**Local files:** No non-empty practice workbook or Power BI project is tracked in this episode folder. Use the official dataset or connector/service referenced by the lesson README.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Append the supplied compatible tables and inspect the combined schema.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Reconcile input/output row counts and inspect nulls introduced by missing columns.

**Evidence to keep**

Save connection/configuration notes or a small independent reproduction; never include credentials. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 45 · Merge & Join Kind (Theory)

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/README.md>)

**Actual files tracked in this lesson folder:**

- [`Merge.xlsx`](<../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/Merge.xlsx>) — Excel workbook

**Excel workbook study**

Open `Merge.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Choose a join kind for a concrete business question and predict which keys survive.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check uniqueness on the lookup side and count unmatched keys.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 46 · Merge & Join Kind

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/README.md>)

**Actual files tracked in this lesson folder:**

- [`Merge.xlsx`](<../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/Merge.xlsx>) — Excel workbook

**Excel workbook study**

Open `Merge.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Merge the supplied tables and expand only the required fields.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Validate row counts before/after expansion and detect duplicate-key row multiplication.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 47 · Fuzzy Match

**Lesson notes:** [Open the episode README](<../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/README.md>)

**Actual files tracked in this lesson folder:**

- [`Merge.xlsx`](<../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/Merge.xlsx>) — Excel workbook

**Excel workbook study**

Open `Merge.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Apply fuzzy matching to inconsistent text keys and inspect match confidence/threshold behavior.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Manually review false positives and unmatched records; do not treat fuzzy matches as verified identity.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 48 · Horizontal Date Matrix

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep48-Horizontal-Date-Matrix/README.md>)

**Actual files tracked in this lesson folder:**

- [`Horizontal Date Matrix Case.xlsx`](<../06-Case-Studies/Ep48-Horizontal-Date-Matrix/Horizontal%20Date%20Matrix%20Case.xlsx>) — Excel workbook
- [`Horizontal Date Matrix.pbix`](<../06-Case-Studies/Ep48-Horizontal-Date-Matrix/Horizontal%20Date%20Matrix.pbix>) — Power BI Desktop project

**Excel workbook study**

Open `Horizontal Date Matrix Case.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Horizontal Date Matrix.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Normalize the horizontal date matrix into a row-based fact-like structure.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check that each entity-date observation is represented once and totals reconcile.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 49 · Fragmented Rows

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep49-Fragmented-Rows/README.md>)

**Actual files tracked in this lesson folder:**

- [`Fragmented Rows Case.xlsx`](<../06-Case-Studies/Ep49-Fragmented-Rows/Fragmented%20Rows%20Case.xlsx>) — Excel workbook
- [`Fragmented Rows.pbix`](<../06-Case-Studies/Ep49-Fragmented-Rows/Fragmented%20Rows.pbix>) — Power BI Desktop project

**Excel workbook study**

Open `Fragmented Rows Case.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Fragmented Rows.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Reconstruct fragmented records using grouping/ordering logic and explicit fill rules.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Compare record counts before/after and inspect boundary rows where fragments begin/end.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 50 · GDP Database

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep50-GDP-Database/README.md>)

**Actual files tracked in this lesson folder:**

- [`GDP Database.txt`](<../06-Case-Studies/Ep50-GDP-Database/GDP%20Database.txt>) — text source

**Other source-file study**

For `GDP Database.txt`, inspect the raw text layout, delimiters, headers, and record boundaries. Decide how the file should be parsed before promoting headers or assigning types.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Import the GDP text source and normalize country/year/value fields.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check numeric parsing, country identifiers, missing values, and year coverage.

**Evidence to keep**

Save a reproducible query, small output sample, and assumptions/edge-case notes. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 51 · Fragmented, Duplicate & Merge

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep51-Fragmented-Duplicate-and-Merge/README.md>)

**Actual files tracked in this lesson folder:**

- [`Fragmented Duplicate & Merge.pbix`](<../06-Case-Studies/Ep51-Fragmented-Duplicate-and-Merge/Fragmented%20Duplicate%20%26%20Merge.pbix>) — Power BI Desktop project
- [`Fragmented Duplicate & Merge.xlsx`](<../06-Case-Studies/Ep51-Fragmented-Duplicate-and-Merge/Fragmented%20Duplicate%20%26%20Merge.xlsx>) — Excel workbook

**Excel workbook study**

Open `Fragmented Duplicate & Merge.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Fragmented Duplicate & Merge.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Resolve fragmented rows and duplicates before merging related tables.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Document the deduplication key and prove the merge does not multiply facts unexpectedly.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 52 · Monthly Sales (Actual vs Budget)

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep52-Monthly-Sales-Actual-vs-Budget/README.md>)

**Actual files tracked in this lesson folder:**

- [`Monthly Sales (Actual vs Budget).pbix`](<../06-Case-Studies/Ep52-Monthly-Sales-Actual-vs-Budget/Monthly%20Sales%20(Actual%20vs%20Budget).pbix>) — Power BI Desktop project
- [`Monthly Sales (Actual vs Budget).xlsx`](<../06-Case-Studies/Ep52-Monthly-Sales-Actual-vs-Budget/Monthly%20Sales%20(Actual%20vs%20Budget).xlsx>) — Excel workbook

**Excel workbook study**

Open `Monthly Sales (Actual vs Budget).xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Monthly Sales (Actual vs Budget).pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Align monthly budget values with daily actuals using a clearly defined date grain.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Validate monthly totals and explain how budget values are allocated or compared.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 53 · Group By (Actual vs Forecast)

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep53-Group-By-Actual-vs-Forecast/README.md>)

**Actual files tracked in this lesson folder:**

- [`Group By (Actual vs Forecast).pbix`](<../06-Case-Studies/Ep53-Group-By-Actual-vs-Forecast/Group%20By%20(Actual%20vs%20Forecast).pbix>) — Power BI Desktop project
- [`SalesRep Actual VS Forecast.xlsx`](<../06-Case-Studies/Ep53-Group-By-Actual-vs-Forecast/SalesRep%20Actual%20VS%20Forecast.xlsx>) — Excel workbook

**Excel workbook study**

Open `SalesRep Actual VS Forecast.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Group By (Actual vs Forecast).pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Group sales records and compare actual versus forecast at a consistent grain.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Reconcile grouped totals with the source and verify grouping keys.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 54 · Complex Header Structure

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep54-Complex-Header-Structure/README.md>)

**Actual files tracked in this lesson folder:**

- [`Complex Header Structure Case.xlsx`](<../06-Case-Studies/Ep54-Complex-Header-Structure/Complex%20Header%20Structure%20Case.xlsx>) — Excel workbook
- [`Complex Header Structure.pbix`](<../06-Case-Studies/Ep54-Complex-Header-Structure/Complex%20Header%20Structure.pbix>) — Power BI Desktop project

**Excel workbook study**

Open `Complex Header Structure Case.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Complex Header Structure.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Flatten the complex header structure into a stable column schema.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check header uniqueness, nulls introduced by fill operations, and record grain.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 55 · Full Project from Multiple Data Sources

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep55-Full-Project-Multiple-Sources/README.md>)

**Actual files tracked in this lesson folder:**

- [`Customer Database.xlsx`](<../06-Case-Studies/Ep55-Full-Project-Multiple-Sources/Customer%20Database.xlsx>) — Excel workbook
- [`Product Database.xlsx`](<../06-Case-Studies/Ep55-Full-Project-Multiple-Sources/Product%20Database.xlsx>) — Excel workbook
- [`SalesFullProject.pbix`](<../06-Case-Studies/Ep55-Full-Project-Multiple-Sources/SalesFullProject.pbix>) — Power BI Desktop project

**Excel workbook study**

Open the 2 Excel workbook(s) listed above. Inspect each file independently before combining anything. Compare sheet/table names, column names, data types, row grain, and overlapping fields. Decide whether these are separate source partitions, different entities, or alternative layouts; only combine files after confirming their structure is compatible.

**Power BI reference project study**

Open `SalesFullProject.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Integrate customer and product sources with the sales PBIX project; identify the sales grain before modeling.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Validate dimension key uniqueness, fact foreign-key coverage, and source-to-model totals.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 56 · Multi-Source Data Integration & Modeling

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep56-Multi-Source-Integration-and-Modeling/README.md>)

**Actual files tracked in this lesson folder:**

- [`Category Database.xlsx`](<../06-Case-Studies/Ep56-Multi-Source-Integration-and-Modeling/Category%20Database.xlsx>) — Excel workbook
- [`Customer Database.txt`](<../06-Case-Studies/Ep56-Multi-Source-Integration-and-Modeling/Customer%20Database.txt>) — text source
- [`Product Database.pdf`](<../06-Case-Studies/Ep56-Multi-Source-Integration-and-Modeling/Product%20Database.pdf>) — PDF source

**Excel workbook study**

Open `Category Database.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Other source-file study**

For `Customer Database.txt`, inspect the raw text layout, delimiters, headers, and record boundaries. Decide how the file should be parsed before promoting headers or assigning types.
For `Product Database.pdf`, inspect the PDF pages and table layouts. Identify repeated page headers, columns that shift between pages/files, and values that need reconciliation after extraction.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Combine the category, customer, and product sources while documenting source-specific transformations.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check key consistency across formats and document the intended model relationships.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 57 · Inconsistent Data Sources

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep57-Inconsistent-Data-Sources/README.md>)

**Actual files tracked in this lesson folder:**

- [`Case study.pbix`](<../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Case%20study.pbix>) — Power BI Desktop project
- [`New Microsoft Excel Worksheet.xlsx`](<../06-Case-Studies/Ep57-Inconsistent-Data-Sources/New%20Microsoft%20Excel%20Worksheet.xlsx>) — Excel workbook
- [`Year - 2005.xlsx`](<../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Year%20-%202005.xlsx>) — Excel workbook
- [`Year - 2006.xlsx`](<../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Year%20-%202006.xlsx>) — Excel workbook
- [`Year - 2007.xlsx`](<../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Year%20-%202007.xlsx>) — Excel workbook
- [`Year - 2008.xlsx`](<../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Year%20-%202008.xlsx>) — Excel workbook
- [`Year - 2009.xlsx`](<../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Year%20-%202009.xlsx>) — Excel workbook

**Excel workbook study**

Open the 6 Excel workbook(s) listed above. Inspect each file independently before combining anything. Compare sheet/table names, column names, data types, row grain, and overlapping fields. Decide whether these are separate source partitions, different entities, or alternative layouts; only combine files after confirming their structure is compatible.

**Power BI reference project study**

Open `Case study.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Build a folder-ingestion approach that filters inconsistent and irrelevant files before combining.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test a new year file, a lock file, and a malformed/unexpected file; confirm refresh resilience.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 58 · Hardcode vs Logic

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep58-Hardcode-vs-Logic/README.md>)

**Actual files tracked in this lesson folder:**

- [`Hardcode vs Logic.xlsx`](<../06-Case-Studies/Ep58-Hardcode-vs-Logic/Hardcode%20vs%20Logic.xlsx>) — Excel workbook

**Excel workbook study**

Open `Hardcode vs Logic.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Replace a hardcoded rule with a rule derived from source values or parameters.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Add a new category/value and verify the logic adapts without editing the query.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 59 · Context vs Logic

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep59-Context-vs-Logic/README.md>)

**Actual files tracked in this lesson folder:**

- [`Context vs Logic (Case Study).pbix`](<../06-Case-Studies/Ep59-Context-vs-Logic/Context%20vs%20Logic%20(Case%20Study).pbix>) — Power BI Desktop project

**Power BI reference project study**

Open `Context vs Logic (Case Study).pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Separate evaluation context from the intended analytical rule in the case study.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Use a small counterexample to explain why the original logic does or does not generalize.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 60 · Locale (Dates vs. Numbers)

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep60-Locale-Dates-vs-Numbers/README.md>)

**Actual files tracked in this lesson folder:**

- [`DatesCSV 23Aug26.csv`](<../06-Case-Studies/Ep60-Locale-Dates-vs-Numbers/DatesCSV%2023Aug26.csv>) — CSV source
- [`Locale (Dates vs. Numbers).pbix`](<../06-Case-Studies/Ep60-Locale-Dates-vs-Numbers/Locale%20(Dates%20vs.%20Numbers).pbix>) — Power BI Desktop project

**Other source-file study**

For `DatesCSV 23Aug26.csv`, inspect delimiter, encoding, quoting, header rows, line breaks, and locale before loading. Compare the parsed row and column counts with the raw file.

**Power BI reference project study**

Open `Locale (Dates vs. Numbers).pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Parse dates and numbers using explicit regional interpretation for mixed-locale data.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test ambiguous day/month values and decimal separators against known examples.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 61 · Vertical Headers Structure

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep61-Vertical-Headers-Structure/README.md>)

**Actual files tracked in this lesson folder:**

- [`Vertical Header Structure.xlsx`](<../06-Case-Studies/Ep61-Vertical-Headers-Structure/Vertical%20Header%20Structure.xlsx>) — Excel workbook
- [`Vertical Headers Structure.pbix`](<../06-Case-Studies/Ep61-Vertical-Headers-Structure/Vertical%20Headers%20Structure.pbix>) — Power BI Desktop project

**Excel workbook study**

Open `Vertical Header Structure.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Vertical Headers Structure.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Transform vertical header/value pairs into a structured table with meaningful columns.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check that labels and values remain aligned after fill/transpose/reshape operations.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 62 · Practical Exercise - 1

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep62-Practical-Exercise-1/README.md>)

**Actual files tracked in this lesson folder:**

- [`Practical Exercise (1).pbix`](<../06-Case-Studies/Ep62-Practical-Exercise-1/Practical%20Exercise%20(1).pbix>) — Power BI Desktop project
- [`Practical Exercise -1 30Aug26.xlsx`](<../06-Case-Studies/Ep62-Practical-Exercise-1/Practical%20Exercise%20-1%2030Aug26.xlsx>) — Excel workbook

**Excel workbook study**

Open `Practical Exercise -1 30Aug26.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Practical Exercise (1).pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Attempt the first practical exercise before inspecting the supplied PBIX solution.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Record the approach, compare the output, and explain one difference or improvement.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 63 · Practical Exercise - 2

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep63-Practical-Exercise-2/README.md>)

**Actual files tracked in this lesson folder:**

- [`Practical Exercise (2).pbix`](<../06-Case-Studies/Ep63-Practical-Exercise-2/Practical%20Exercise%20(2).pbix>) — Power BI Desktop project
- [`Practical Exercise -2 2Sep26.xlsx`](<../06-Case-Studies/Ep63-Practical-Exercise-2/Practical%20Exercise%20-2%202Sep26.xlsx>) — Excel workbook

**Excel workbook study**

Open `Practical Exercise -2 2Sep26.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Practical Exercise (2).pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Attempt the second practical exercise independently and use the PBIX as a comparison reference.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Validate row counts, key fields, output types, and totals.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 64 · Multi-Bank PDF Consolidation

**Lesson notes:** [Open the episode README](<../06-Case-Studies/Ep64-Multi-Bank-PDF-Consolidation/README.md>)

**Actual files tracked in this lesson folder:**

- [`Alrajhi/Alrajhi Bank.pdf`](<../06-Case-Studies/Ep64-Multi-Bank-PDF-Consolidation/Alrajhi/Alrajhi%20Bank.pdf>) — PDF source
- [`Multi-Bank PDF Consolidation.pbix`](<../06-Case-Studies/Ep64-Multi-Bank-PDF-Consolidation/Multi-Bank%20PDF%20Consolidation.pbix>) — Power BI Desktop project
- [`SNB/SNB Bank.pdf`](<../06-Case-Studies/Ep64-Multi-Bank-PDF-Consolidation/SNB/SNB%20Bank.pdf>) — PDF source

**Other source-file study**

For `Alrajhi/Alrajhi Bank.pdf`, `SNB/SNB Bank.pdf`, inspect the PDF pages and table layouts. Identify repeated page headers, columns that shift between pages/files, and values that need reconciliation after extraction.

**Power BI reference project study**

Open `Multi-Bank PDF Consolidation.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Consolidate the Alrajhi and SNB PDF statements using a repeatable extraction pattern.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Compare extracted transactions/totals with each source statement and preserve bank/source identity.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 65 · Null vs. Blank – Full Explanation

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep65-Null-vs-Blank/README.md>)

**Actual files tracked in this lesson folder:**

- [`Null vs Blank.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep65-Null-vs-Blank/Null%20vs%20Blank.pbix>) — Power BI Desktop project
- [`Test.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep65-Null-vs-Blank/Test.xlsx>) — Excel workbook

**Excel workbook study**

Open `Test.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Null vs Blank.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Compare null, blank text, and empty values in the supplied test data.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Check how each behaves in filters, type conversion, and downstream expressions.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 66 · Cartesian Join

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep66-Cartesian-Join/README.md>)

**Actual files tracked in this lesson folder:**

- [`Cartesian Join.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep66-Cartesian-Join/Cartesian%20Join.pbix>) — Power BI Desktop project
- [`Cartesian Join.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep66-Cartesian-Join/Cartesian%20Join.xlsx>) — Excel workbook

**Excel workbook study**

Open `Cartesian Join.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Cartesian Join.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Create a Cartesian product and calculate expected row multiplication before execution.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Validate output row count equals the product of input row counts for non-empty inputs.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 67 · Safe vs. Breaking Changes

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep67-Safe-vs-Breaking-Changes/README.md>)

**Actual files tracked in this lesson folder:**

- [`Safe vs. Breaking Changes.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep67-Safe-vs-Breaking-Changes/Safe%20vs.%20Breaking%20Changes.pbix>) — Power BI Desktop project
- [`Safe vs. Breaking Changes.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep67-Safe-vs-Breaking-Changes/Safe%20vs.%20Breaking%20Changes.xlsx>) — Excel workbook
- [`Very Important Notes.pdf`](<../07-Power-Query-Engine-and-M-Language/Ep67-Safe-vs-Breaking-Changes/Very%20Important%20Notes.pdf>) — PDF source

**Excel workbook study**

Open `Safe vs. Breaking Changes.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Other source-file study**

For `Very Important Notes.pdf`, inspect the PDF pages and table layouts. Identify repeated page headers, columns that shift between pages/files, and values that need reconciliation after extraction.

**Power BI reference project study**

Open `Safe vs. Breaking Changes.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Classify query edits as safe or breaking and inspect downstream dependencies.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test a rename/type/schema change and identify affected steps and consumers.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 68 · Step Error vs. Cell Error

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep68-Step-Error-vs-Cell-Error/README.md>)

**Actual files tracked in this lesson folder:**

- [`Eps 68 - Step Error vs. Cell Error.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep68-Step-Error-vs-Cell-Error/Eps%2068%20-%20Step%20Error%20vs.%20Cell%20Error.xlsx>) — Excel workbook
- [`Step Error vs. Cell Error.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep68-Step-Error-vs-Cell-Error/Step%20Error%20vs.%20Cell%20Error.pbix>) — Power BI Desktop project

**Excel workbook study**

Open `Eps 68 - Step Error vs. Cell Error.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Step Error vs. Cell Error.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Create or inspect both step-level and cell-level errors and compare their impact.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Record whether the query refreshes and how errors can be isolated without silently discarding data.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 69 · M Language (Theory)

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/README.md>)

**Actual files tracked in this lesson folder:**

- [`M Language.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/M%20Language.pbix>) — Power BI Desktop project
- [`M Language.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/M%20Language.xlsx>) — Excel workbook

**Excel workbook study**

Open `M Language.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `M Language.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Read M expressions as values and functions; inspect let/in scope, lists, records, and tables.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Explain evaluation dependencies and test a small expression in a blank query.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 70 · M Language

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/README.md>)

**Actual files tracked in this lesson folder:**

- [`M Language.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/M%20Language.pbix>) — Power BI Desktop project
- [`M Language.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/M%20Language.xlsx>) — Excel workbook

**Excel workbook study**

Open `M Language.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `M Language.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Rebuild a compact M query using explicit let bindings, functions, and table/list operations.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Change one input and explain how the expression evaluates.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 71 · Practical Exercise - 3

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep71-Practical-Exercise-3/README.md>)

**Actual files tracked in this lesson folder:**

- [`Ep. 71.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep71-Practical-Exercise-3/Ep.%2071.xlsx>) — Excel workbook
- [`Practical Exercise - 3.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep71-Practical-Exercise-3/Practical%20Exercise%20-%203.pbix>) — Power BI Desktop project

**Excel workbook study**

Open `Ep. 71.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Practical Exercise - 3.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Complete the practical M exercise without copying the PBIX query steps.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Save your solution, compare with the reference, and record correctness and alternatives.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 72 · Helper Queries

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/README.md>)

**Actual files tracked in this lesson folder:**

- [`Department Folder/Administration.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Administration.xlsx>) — Excel workbook
- [`Department Folder/Business Development.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Business%20Development.xlsx>) — Excel workbook
- [`Department Folder/Customer Service.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Customer%20Service.xlsx>) — Excel workbook
- [`Department Folder/Finance.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Finance.xlsx>) — Excel workbook
- [`Department Folder/Human Resources.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Human%20Resources.xlsx>) — Excel workbook
- [`Department Folder/IT.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/IT.xlsx>) — Excel workbook
- [`Department Folder/Legal.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Legal.xlsx>) — Excel workbook
- [`Helper Queries.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries.pbix>) — Power BI Desktop project
- [`Helper Queries/Administration.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Administration.xlsx>) — Excel workbook
- [`Helper Queries/Business Development.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Business%20Development.xlsx>) — Excel workbook
- [`Helper Queries/Customer Service.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Customer%20Service.xlsx>) — Excel workbook
- [`Helper Queries/Finance.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Finance.xlsx>) — Excel workbook
- [`Helper Queries/Human Resources.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Human%20Resources.xlsx>) — Excel workbook
- [`Helper Queries/IT.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/IT.xlsx>) — Excel workbook
- [`Helper Queries/Legal.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Legal.xlsx>) — Excel workbook

**Excel workbook study**

Open the 14 Excel workbook(s) listed above. Inspect each file independently before combining anything. Compare sheet/table names, column names, data types, row grain, and overlapping fields. Decide whether these are separate source partitions, different entities, or alternative layouts; only combine files after confirming their structure is compatible.

**Power BI reference project study**

Open `Helper Queries.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Inspect the helper-query PBIX and the two department-folder layouts; distinguish staging/helper queries from final outputs.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Verify folder filters, function invocation, and combined row counts.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 73 · Build Custom Functions

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep73-Build-Custom-Functions/README.md>)

**Actual files tracked in this lesson folder:**

- [`Build Custom Functions.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep73-Build-Custom-Functions/Build%20Custom%20Functions.pbix>) — Power BI Desktop project
- [`Ep. 73.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep73-Build-Custom-Functions/Ep.%2073.xlsx>) — Excel workbook

**Excel workbook study**

Open `Ep. 73.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Build Custom Functions.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Build a typed custom function and invoke it against the supplied workbook.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test valid, null, and invalid parameter values and document the function contract.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 74 · Frequency vs. Sequence Analysis

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep74-Frequency-vs-Sequence-Analysis/README.md>)

**Actual files tracked in this lesson folder:**

- [`Frequency vs Sequence Analysis.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep74-Frequency-vs-Sequence-Analysis/Frequency%20vs%20Sequence%20Analysis.xlsx>) — Excel workbook
- [`Frequency vs. Sequence Analysis.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep74-Frequency-vs-Sequence-Analysis/Frequency%20vs.%20Sequence%20Analysis.pbix>) — Power BI Desktop project

**Excel workbook study**

Open `Frequency vs Sequence Analysis.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Frequency vs. Sequence Analysis.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Calculate frequency and sequence metrics using stable sort/index logic.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test ties, repeated events, missing dates, and sequence boundaries.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 75 · Missing Fields

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep75-Missing-Fields/README.md>)

**Actual files tracked in this lesson folder:**

- [`Missing Fields.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep75-Missing-Fields/Missing%20Fields.pbix>) — Power BI Desktop project
- [`Missing Fields.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep75-Missing-Fields/Missing%20Fields.xlsx>) — Excel workbook

**Excel workbook study**

Open `Missing Fields.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Missing Fields.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Handle fields that may be absent from a record/table using an explicit missing-field policy.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test both present and absent columns and ensure the fallback is intentional.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 76 · Away From Zero

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep76-Away-From-Zero/README.md>)

**Actual files tracked in this lesson folder:**

- [`Away From Zero.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep76-Away-From-Zero/Away%20From%20Zero.pbix>) — Power BI Desktop project
- [`Away From Zero.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep76-Away-From-Zero/Away%20From%20Zero.xlsx>) — Excel workbook

**Excel workbook study**

Open `Away From Zero.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Away From Zero.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Compare midpoint rounding modes, including AwayFromZero, with positive and negative values.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test positive/negative halves and document the business rounding rule.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 77 · The Logic of Thinking

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep77-The-Logic-of-Thinking/README.md>)

**Actual files tracked in this lesson folder:**

- [`The Logic of Thinking.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep77-The-Logic-of-Thinking/The%20Logic%20of%20Thinking.pbix>) — Power BI Desktop project
- [`The Logic of Thinking.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep77-The-Logic-of-Thinking/The%20Logic%20of%20Thinking.xlsx>) — Excel workbook

**Excel workbook study**

Open `The Logic of Thinking.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `The Logic of Thinking.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Translate the problem statement into declarative steps before writing M.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Explain why the transformation is correct and identify hidden assumptions.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 78 · Worksheets Name

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/README.md>)

**Actual files tracked in this lesson folder:**

- [`Employees Datebase/Administration.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Administration.xlsx>) — Excel workbook
- [`Employees Datebase/Business Development.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Business%20Development.xlsx>) — Excel workbook
- [`Employees Datebase/Customer Service.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Customer%20Service.xlsx>) — Excel workbook
- [`Employees Datebase/Finance.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Finance.xlsx>) — Excel workbook
- [`Employees Datebase/Human Resources.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Human%20Resources.xlsx>) — Excel workbook
- [`Employees Datebase/IT.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/IT.xlsx>) — Excel workbook
- [`Employees Datebase/Legal.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Legal.xlsx>) — Excel workbook
- [`HRDatabase.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/HRDatabase.xlsx>) — Excel workbook
- [`HRDatabase2.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/HRDatabase2.xlsx>) — Excel workbook
- [`Worksheet Names.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Worksheet%20Names.pbix>) — Power BI Desktop project

**Excel workbook study**

Open the 9 Excel workbook(s) listed above. Inspect each file independently before combining anything. Compare sheet/table names, column names, data types, row grain, and overlapping fields. Decide whether these are separate source partitions, different entities, or alternative layouts; only combine files after confirming their structure is compatible.

**Power BI reference project study**

Open `Worksheet Names.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Combine worksheets across the department workbooks using worksheet names as metadata.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test a new worksheet and a missing worksheet; verify selection and schema handling.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 79 · Transform All Columns

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep79-Transform-All-Columns/README.md>)

**Actual files tracked in this lesson folder:**

- [`Transform All Columns.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep79-Transform-All-Columns/Transform%20All%20Columns.pbix>) — Power BI Desktop project
- [`Transform All Columns.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep79-Transform-All-Columns/Transform%20All%20Columns.xlsx>) — Excel workbook

**Excel workbook study**

Open `Transform All Columns.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Transform All Columns.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Apply a transformation across columns using an explicit column/type policy.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Confirm non-target columns remain unchanged and null/type edge cases are handled.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 80 · Null Coalescing Operator

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep80-Null-Coalescing-Operator/README.md>)

**Actual files tracked in this lesson folder:**

- [`Null Coalescing Operator.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep80-Null-Coalescing-Operator/Null%20Coalescing%20Operator.pbix>) — Power BI Desktop project
- [`Null Coalescing Operator.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep80-Null-Coalescing-Operator/Null%20Coalescing%20Operator.xlsx>) — Excel workbook

**Excel workbook study**

Open `Null Coalescing Operator.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Null Coalescing Operator.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Use the null-coalescing operator for a deliberate fallback expression.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Distinguish null from empty text/zero and test precedence/parentheses.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 81 · Try & Otherwise

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep81-Try-and-Otherwise/README.md>)

**Actual files tracked in this lesson folder:**

- [`Try and Otherwise.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep81-Try-and-Otherwise/Try%20and%20Otherwise.pbix>) — Power BI Desktop project
- [`Try and Otherwise.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep81-Try-and-Otherwise/Try%20and%20Otherwise.xlsx>) — Excel workbook

**Excel workbook study**

Open `Try and Otherwise.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Try and Otherwise.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Use try/otherwise to handle an expected failure while preserving diagnostic information where needed.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test success and failure paths; ensure the fallback does not hide data-quality defects.

**Evidence to keep**

Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 82 · Reference Outside Scope

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep82-Reference-Outside-Scope/README.md>)

**Actual files tracked in this lesson folder:**

- [`Reference_Outside_Scope.pbix`](<../07-Power-Query-Engine-and-M-Language/Ep82-Reference-Outside-Scope/Reference_Outside_Scope.pbix>) — Power BI Desktop project
- [`Reference_Outside_Scope.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep82-Reference-Outside-Scope/Reference_Outside_Scope.xlsx>) — Excel workbook

**Excel workbook study**

Open `Reference_Outside_Scope.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI reference project study**

Open `Reference_Outside_Scope.pbix` in Power BI Desktop after making your own first attempt. In **Transform data**, trace each query from its source through the Applied Steps. For every important step, write: input shape → transformation → output shape → reason. Rebuild the key transformation separately, then compare row counts, columns, types, and key values with the reference.

**Episode-specific task**

Inspect a reference that is outside the current lexical scope and trace the evaluation dependency.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Explain why the identifier is or is not visible at the point of use.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

### Ep. 83 · Complex Date Transformations

**Lesson notes:** [Open the episode README](<../07-Power-Query-Engine-and-M-Language/Ep83-Complex-Date-Transformations/README.md>)

**Actual files tracked in this lesson folder:**

- [`Complex_Date_Transformations.xlsx`](<../07-Power-Query-Engine-and-M-Language/Ep83-Complex-Date-Transformations/Complex_Date_Transformations.xlsx>) — Excel workbook

**Excel workbook study**

Open `Complex_Date_Transformations.xlsx` in Excel. Inspect every worksheet and structured table, then write down the exact object names and the meaning of one row. Identify identifiers, descriptive fields, numeric/date fields, nulls, duplicates, and any presentation formatting that is not part of the real table.

**Power BI build/reference step**

No PBIX/PBIT reference project is tracked in this folder. When the lesson produces a transformed table, create a small PBIX of your own and retain the query and a simple validation view. For service, connector, or governance lessons, a documented connection/refresh test may be more useful than forcing the work into a report.

**Episode-specific task**

Build date transformations for quarters, durations, and custom periods using explicit calendar assumptions.

Turn that focus into a reproducible exercise: write down the source, recreate the key transformation in your own query, and explain why the approach fits this data rather than merely listing UI clicks.

**Validation checkpoint**

Test month/year boundaries, leap days, fiscal boundaries, and null dates.

**Evidence to keep**

Save the query output or a before/after workbook and record row counts, types, and key checks. Include the actual object/field names you observed, a small before/after example, row-count or total reconciliation where relevant, and one edge case. Do not include credentials or restricted personal data.

---

## Final review checklist

- [ ] I recorded the source object, actual field names, and row grain.
- [ ] I rebuilt the main transformation instead of only watching or copying the reference PBIX.
- [ ] I can explain the purpose of the important Applied Steps.
- [ ] I checked types, nulls, errors, duplicates, and key integrity where relevant.
- [ ] I reconciled row counts or business totals against the source.
- [ ] I tested at least one realistic edge case.
- [ ] I saved evidence and added a dated entry to the [learning log](LEARNING_LOG.md).
- [ ] I updated my status and review date in the [progress tracker](../PROGRESS_TRACKER.md).

## Related learning tools

- [Competency-based roadmap](LEARNING_ROADMAP.md)
- [Learning log](LEARNING_LOG.md)
- [Progress tracker](../PROGRESS_TRACKER.md)
- [Documentation standard](DOCUMENTATION_STANDARD.md)
