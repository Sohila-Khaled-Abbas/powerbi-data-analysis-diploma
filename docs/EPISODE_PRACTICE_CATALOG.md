# Episode-by-Episode Practice Catalog

> Generated from the repository's tracked file tree and the 83-row course tracker. The 83 episodes are grouped into 71 physical lesson folders; shared folders are intentionally linked from each relevant episode. This inventory does not claim that the assets have been independently audited or that any lesson is complete.

## How to use this catalog

1. Read the linked episode notes and watch the official lesson.
2. Identify the source, row grain, expected output, and transformation goal.
3. Rebuild the demonstrated workflow with the listed practice files where available.
4. Complete the independent practice prompt below and test an edge case.
5. Save evidence and update [your learning log](LEARNING_LOG.md) and [progress tracker](../PROGRESS_TRACKER.md).

**File types:** Excel workbooks are source/practice data; PBIX files are Power BI Desktop projects/reports; PBIT files are templates; CSV/TXT/JSON/PDF files are source formats. Confirm the exact role of each asset from the lesson rather than inferring it from its extension.

## Episode inventory

### Ep. 01 · دبلومة تحليل البيانات - المحاضرة (١) - مقدمة

- **Lesson folder:** [Open episode notes](../01-Data-Foundations/Ep01-Introduction/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Sketch the BI workflow from source data to a decision; identify where Power Query and the semantic model fit.
- **Validation checkpoint:** Explain the purpose of each stage without describing only button clicks.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 02 · Proper Raw Data Structure

- **Lesson folder:** [Open episode notes](../01-Data-Foundations/Ep02-Proper-Raw-Data-Structure/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Inspect a raw table and state its grain, one-row meaning, identifier columns, and observation columns.
- **Validation checkpoint:** Flag repeated headers, totals mixed with records, merged cells, and multiple values in one field.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 03 · Get Data From Microsoft Excel

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep03-Get-Data-From-Excel/README.md)
- **Tracked practice assets:** [`3. Countries Database.xlsx`](../02-Data-Acquisition/Ep03-Get-Data-From-Excel/3.%20Countries%20Database.xlsx) · Excel workbook<br>[`Administration.xlsx`](../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Administration.xlsx) · Excel workbook<br>[`Business Development.xlsx`](../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Business%20Development.xlsx) · Excel workbook<br>[`Customer Service.xlsx`](../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Customer%20Service.xlsx) · Excel workbook<br>[`Finance.xlsx`](../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Finance.xlsx) · Excel workbook<br>[`Human Resources.xlsx`](../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Human%20Resources.xlsx) · Excel workbook<br>[`IT.xlsx`](../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/IT.xlsx) · Excel workbook<br>[`Legal.xlsx`](../02-Data-Acquisition/Ep03-Get-Data-From-Excel/4.%20Employees%20Datebase/Legal.xlsx) · Excel workbook
- **Practice focus:** Open the workbook navigator; compare a structured Excel Table with a worksheet object and select the intended source.
- **Validation checkpoint:** Add a row to the table and refresh; confirm the new record is included and unrelated objects are excluded.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 04 · Get Data From CSV Files

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/README.md)
- **Tracked practice assets:** [`1. csv Employees.csv`](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/1.%20csv%20Employees.csv) · CSV<br>[`2. txt Customers.txt`](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/2.%20txt%20Customers.txt) · Text<br>[`3. csv Employees With Summary Header.csv`](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/3.%20csv%20Employees%20With%20Summary%20Header.csv) · CSV<br>[`4. csv Employees With Quotes.csv`](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/4.%20csv%20Employees%20With%20Quotes.csv) · CSV<br>[`5. CSV Extract From Example.csv`](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/5.%20CSV%20Extract%20From%20Example.csv) · CSV
- **Practice focus:** Import the CSV and test delimiter, encoding, quote style, and header handling.
- **Validation checkpoint:** Compare row/column counts with the raw file and inspect values containing embedded delimiters.
- **Evidence to save:** Save a reproducible query, small output sample, and assumptions/edge-case notes.

### Ep. 05 · Fixing CSV Import Issues

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/README.md)
- **Tracked practice assets:** [`1. csv Employees.csv`](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/1.%20csv%20Employees.csv) · CSV<br>[`2. txt Customers.txt`](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/2.%20txt%20Customers.txt) · Text<br>[`3. csv Employees With Summary Header.csv`](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/3.%20csv%20Employees%20With%20Summary%20Header.csv) · CSV<br>[`4. csv Employees With Quotes.csv`](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/4.%20csv%20Employees%20With%20Quotes.csv) · CSV<br>[`5. CSV Extract From Example.csv`](../02-Data-Acquisition/Ep04-05-Get-Data-From-CSV/5.%20CSV%20Extract%20From%20Example.csv) · CSV
- **Practice focus:** Reproduce a malformed CSV import using the supplied variants; adjust parsing options rather than manually editing the source.
- **Validation checkpoint:** Confirm quoted fields, summary lines, and headers are parsed as intended.
- **Evidence to save:** Save a reproducible query, small output sample, and assumptions/edge-case notes.

### Ep. 06 · Get Data From PDFs

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/README.md)
- **Tracked practice assets:** [`Abdullah Alomary.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Abdullah%20Alomary.pdf) · PDF<br>[`Abeer Mohamed.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Abeer%20Mohamed.pdf) · PDF<br>[`Ahmed Ezzat.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Ahmed%20Ezzat.pdf) · PDF<br>[`Ahmed Yousef.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Ahmed%20Yousef.pdf) · PDF<br>[`Amal Abdelfatah.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Amal%20Abdelfatah.pdf) · PDF<br>[`Amal Mohamed.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Amal%20Mohamed.pdf) · PDF<br>[`Azza Abdelrahman.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Azza%20Abdelrahman.pdf) · PDF<br>[`Berry Hassan.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Berry%20Hassan.pdf) · PDF<br>[`Essam Elsayad.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Essam%20Elsayad.pdf) · PDF<br>[`Hala Ahmed.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Hala%20Ahmed.pdf) · PDF<br>[`Hassan Abdelrahman.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Hassan%20Abdelrahman.pdf) · PDF<br>[`Mahmoud Hamouda.pdf`](../02-Data-Acquisition/Ep06-Get-Data-From-PDF/2.%20Employees%20Database/Mahmoud%20Hamouda.pdf) · PDF
- **Practice focus:** Extract a tabular section from the employee PDFs and inspect repeated headers and page boundaries.
- **Validation checkpoint:** Compare extracted records with source pages; check missing/duplicated rows.
- **Evidence to save:** Save a reproducible query, small output sample, and assumptions/edge-case notes.

### Ep. 07 · On-Premises Data Gateway

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep07-On-Premises-Data-Gateway/README.md)
- **Tracked practice assets:** [`Essam Elsayad Gateway.xlsx`](../02-Data-Acquisition/Ep07-On-Premises-Data-Gateway/Essam%20Elsayad%20Gateway.xlsx) · Excel workbook
- **Practice focus:** Map the on-premises gateway path from data source to Power BI Service refresh.
- **Validation checkpoint:** Document gateway dependency, credentials, source reachability, and a safe refresh test.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 08 · Get Data From OneDrive

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep08-Get-Data-From-OneDrive/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Connect to a OneDrive-hosted file and distinguish the cloud path from a local synced path.
- **Validation checkpoint:** Change the source file and verify refresh behavior without hardcoding a machine-specific path.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 09 · Get Data From SharePoint

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep09-Get-Data-From-SharePoint/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Connect to a SharePoint document library and filter to the intended file.
- **Validation checkpoint:** Verify site/library/file identity and test a refresh after a file update.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 10 · Get Data From Google Sheets

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep10-Get-Data-From-Google-Sheets/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Connect to a Google Sheet and inspect its tabular structure and access requirements.
- **Validation checkpoint:** Verify header row, column types, and whether the connector returns the expected worksheet.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 11 · Get Data From Google Drive

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep11-Get-Data-From-Google-Drive/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Connect to a Google Drive file and compare the selected object with the intended source.
- **Validation checkpoint:** Record authentication and refresh constraints; confirm file identity.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 12 · Get Data From Database (SQL / Oracle / SAP)

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep12-Get-Data-From-Database/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Connect to a relational source and inspect native query/folding indicators where supported by the connector.
- **Validation checkpoint:** Validate row counts and key filters; distinguish source-side operations from local transformations.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 13 · Get Data From Semantic Models

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep13-Get-Data-From-Semantic-Models/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Connect to a published semantic model and identify what is reusable versus what cannot be transformed locally.
- **Validation checkpoint:** Explain the difference between consuming a governed model and importing raw source tables.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 14 · Get Data From Microsoft Exchange

- **Lesson folder:** [Open episode notes](../02-Data-Acquisition/Ep14-Get-Data-From-Microsoft-Exchange/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Inspect the mailbox/attachment ingestion pattern and identify which messages or attachments should be included.
- **Validation checkpoint:** Test duplicate attachments, unexpected file types, and privacy/credential boundaries.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 15 · Get Data From Web

- **Lesson folder:** [Open episode notes](../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/README.md)
- **Tracked practice assets:** [`get data from web.pbix`](../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/get%20data%20from%20web.pbix) · Power BI report
- **Practice focus:** Extract a web table and inspect how page structure maps to rows and columns.
- **Validation checkpoint:** Check row count, repeated headings, and whether a website layout change breaks the query.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 16 · Get Data From Web (Invoke)

- **Lesson folder:** [Open episode notes](../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/README.md)
- **Tracked practice assets:** [`get data from web.pbix`](../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/get%20data%20from%20web.pbix) · Power BI report
- **Practice focus:** Turn a repeated web extraction into a parameterized function and invoke it for multiple inputs.
- **Validation checkpoint:** Compare outputs across inputs and confirm consistent schemas.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 17 · Get Data From Web (List)

- **Lesson folder:** [Open episode notes](../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/README.md)
- **Tracked practice assets:** [`get data from web.pbix`](../03-Advanced-Data-Extraction/Ep15-17-Get-Data-From-Web/get%20data%20from%20web.pbix) · Power BI report
- **Practice focus:** Iterate over multiple web pages or result sets and combine the returned tables.
- **Validation checkpoint:** Check termination, duplicate pages, missing pages, and consistent columns.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 18 · Get Data From API

- **Lesson folder:** [Open episode notes](../03-Advanced-Data-Extraction/Ep18-19-Get-Data-From-API/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Build a request to an API endpoint and inspect status, headers, and response shape.
- **Validation checkpoint:** Test a failed response and verify the parsed record/list structure.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 19 · Get Data From API (List. Generate)

- **Lesson folder:** [Open episode notes](../03-Advanced-Data-Extraction/Ep18-19-Get-Data-From-API/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Use List.Generate or an equivalent controlled loop to retrieve pages until the stop condition is met.
- **Validation checkpoint:** Check page termination, repeated cursors, rate limits, and duplicate records.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 20 · Get Data From LinkedIn

- **Lesson folder:** [Open episode notes](../03-Advanced-Data-Extraction/Ep20-Get-Data-From-LinkedIn/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Review the LinkedIn source approach and identify current API/access limitations before attempting a live connection.
- **Validation checkpoint:** Separate reproducible query logic from credentials, permissions, and platform policy.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 21 · Get Data From X (Twitter)

- **Lesson folder:** [Open episode notes](../03-Advanced-Data-Extraction/Ep21-Get-Data-From-X-Twitter/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Review the X/Twitter source approach and identify current API/access limitations before attempting a live connection.
- **Validation checkpoint:** Separate reproducible query logic from credentials, permissions, and platform policy.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 22 · Get Data From Dataverse

- **Lesson folder:** [Open episode notes](../03-Advanced-Data-Extraction/Ep22-Get-Data-From-Dataverse/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Explore Dataverse entities and identify the table relationships and columns required for the scenario.
- **Validation checkpoint:** Check entity selection, key fields, and permission boundaries.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 23 · Get Data From JSON - Facebook - Instagram

- **Lesson folder:** [Open episode notes](../03-Advanced-Data-Extraction/Ep23-Get-Data-From-JSON/README.md)
- **Tracked practice assets:** [`Essam Elsayad.json`](../03-Advanced-Data-Extraction/Ep23-Get-Data-From-JSON/Essam%20Elsayad.json) · JSON
- **Practice focus:** Expand the supplied JSON from its outer record/list into a tabular shape while preserving identifiers.
- **Validation checkpoint:** Test optional/missing fields and verify nested list expansion does not multiply rows unexpectedly.
- **Evidence to save:** Save a reproducible query, small output sample, and assumptions/edge-case notes.

### Ep. 24 · Permissions (Credential - Encryption - Privacy)

- **Lesson folder:** [Open episode notes](../04-Governance-and-Automation/Ep24-Permissions-Credential-Encryption-Privacy/README.md)
- **Tracked practice assets:** [`Permissions (Credential, Encryption & Privacy).pdf`](../04-Governance-and-Automation/Ep24-Permissions-Credential-Encryption-Privacy/Permissions%20%28Credential%2C%20Encryption%20%26%20Privacy%29.pdf) · PDF<br>[`csv_employees.csv`](../04-Governance-and-Automation/Ep24-Permissions-Credential-Encryption-Privacy/csv_employees.csv) · CSV
- **Practice focus:** Inspect privacy levels, credentials, and encryption settings for the supplied source scenario.
- **Validation checkpoint:** Explain why privacy/firewall behavior changes across source combinations; never commit credentials.
- **Evidence to save:** Save a reproducible query, small output sample, and assumptions/edge-case notes.

### Ep. 25 · PBIDS (Power BI Data Source File)

- **Lesson folder:** [Open episode notes](../04-Governance-and-Automation/Ep25-PBIDS-Data-Source-File/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Inspect the PBIDS concept and build a minimal source-definition file for a safe sample connection.
- **Validation checkpoint:** Validate file syntax and confirm it identifies the intended source without embedding secrets.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 26 · Endorsement & Discovery

- **Lesson folder:** [Open episode notes](../04-Governance-and-Automation/Ep26-Endorsement-and-Discovery/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Compare promoted and certified endorsement and identify how discovery metadata supports governed reuse.
- **Validation checkpoint:** Explain who can endorse content and what evidence a consumer should expect.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 27 · Power Platform (Data Flows)

- **Lesson folder:** [Open episode notes](../04-Governance-and-Automation/Ep27-Power-Platform-Dataflows/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Map the dataflow as a reusable cloud ETL layer and identify ownership/refresh boundaries.
- **Validation checkpoint:** Document source credentials, refresh dependencies, and downstream consumers.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 28 · Data Source Connections (Import, Direct & Live)

- **Lesson folder:** [Open episode notes](../04-Governance-and-Automation/Ep28-29-Data-Source-Connections-Storage-Modes/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Compare Import, DirectQuery, and Live Connection for the same analytical requirement.
- **Validation checkpoint:** Explain storage, latency, transformation, and model-authoring trade-offs.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 29 · Dual Mode Connection

- **Lesson folder:** [Open episode notes](../04-Governance-and-Automation/Ep28-29-Data-Source-Connections-Storage-Modes/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Inspect Dual storage mode and identify when a table can participate in composite model behavior.
- **Validation checkpoint:** Explain expected query behavior and validate the model's storage-mode settings.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 30 · Parameters

- **Lesson folder:** [Open episode notes](../04-Governance-and-Automation/Ep30-31-Parameters-and-Templates/README.md)
- **Tracked practice assets:** [`New Template.pbit`](../04-Governance-and-Automation/Ep30-31-Parameters-and-Templates/New%20Template.pbit) · Power BI template
- **Practice focus:** Create a parameter for a source value or file path and replace a hardcoded literal.
- **Validation checkpoint:** Change the parameter and verify the query points to the intended source.
- **Evidence to save:** Save a reproducible query, small output sample, and assumptions/edge-case notes.

### Ep. 31 · Templates & Parameters

- **Lesson folder:** [Open episode notes](../04-Governance-and-Automation/Ep30-31-Parameters-and-Templates/README.md)
- **Tracked practice assets:** [`New Template.pbit`](../04-Governance-and-Automation/Ep30-31-Parameters-and-Templates/New%20Template.pbit) · Power BI template
- **Practice focus:** Open the PBIT template and inspect its parameters and source prompts.
- **Validation checkpoint:** Instantiate the template with safe test values and verify no credentials are embedded.
- **Evidence to save:** Save a reproducible query, small output sample, and assumptions/edge-case notes.

### Ep. 32 · Different Data Types (Theory)

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep32-33-Different-Data-Types/README.md)
- **Tracked practice assets:** [`datatypes.xlsx`](../05-Data-Transformation/Ep32-33-Different-Data-Types/datatypes.xlsx) · Excel workbook<br>[`datatypes_info.xlsx`](../05-Data-Transformation/Ep32-33-Different-Data-Types/datatypes_info.xlsx) · Excel workbook
- **Practice focus:** Inspect the supplied type examples and classify identifiers, dates, numbers, logical values, and text.
- **Validation checkpoint:** Identify conversions that can lose precision or change meaning.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 33 · Different Data Types

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep32-33-Different-Data-Types/README.md)
- **Tracked practice assets:** [`datatypes.xlsx`](../05-Data-Transformation/Ep32-33-Different-Data-Types/datatypes.xlsx) · Excel workbook<br>[`datatypes_info.xlsx`](../05-Data-Transformation/Ep32-33-Different-Data-Types/datatypes_info.xlsx) · Excel workbook
- **Practice focus:** Apply explicit data types and compare results before and after conversion.
- **Validation checkpoint:** Check conversion errors, leading zeros in identifiers, and numeric/date interpretation.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 34 · Local Interpretation

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep34-Local-Interpretation/README.md)
- **Tracked practice assets:** [`csv_wideworldimporters.csv`](../05-Data-Transformation/Ep34-Local-Interpretation/csv_wideworldimporters.csv) · CSV<br>[`datatypes.xlsx`](../05-Data-Transformation/Ep34-Local-Interpretation/datatypes.xlsx) · Excel workbook
- **Practice focus:** Parse the supplied dates/numbers using the correct locale rather than relying on machine defaults.
- **Validation checkpoint:** Test ambiguous dates and decimal/thousands separators; record the locale assumption.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 35 · Custom Columns

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep35-Custom-Columns/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Create a custom column from existing fields and document the expression's input/output types.
- **Validation checkpoint:** Test nulls and unexpected values in the source columns.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 36 · Conditional Columns

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep36-Conditional-Columns/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Create conditional logic for mutually exclusive business rules and test boundary values.
- **Validation checkpoint:** Check rule order, uncovered values, and overlapping conditions.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 37 · Columns from Examples

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep37-Columns-From-Examples/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Use Column From Examples on representative rows, then inspect the generated transformation logic.
- **Validation checkpoint:** Test unseen patterns and edge cases; do not assume the inferred rule generalizes.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 38 · Split and Merge Columns

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep38-Split-and-Merge-Columns/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Split and merge fields using explicit delimiters and preserve original identifiers where needed.
- **Validation checkpoint:** Test missing delimiters, repeated delimiters, and null values.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 39 · Invoke Custom Function

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep39-Invoke-Custom-Function/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Invoke a custom function over a table column and inspect row-level results.
- **Validation checkpoint:** Check parameter types, error handling, and whether each input produces one expected output.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 40 · UnPivot Columns

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/README.md)
- **Tracked practice assets:** [`Unpivot & Pivot Columns.xlsx`](../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/Unpivot%20%26%20Pivot%20Columns.xlsx) · Excel workbook<br>[`unpivot.pbix`](../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/unpivot.pbix) · Power BI report
- **Practice focus:** Unpivot the wide sample while retaining the correct identifier columns.
- **Validation checkpoint:** Confirm each output row represents one entity-period-value combination.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 41 · Pivot Columns

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/README.md)
- **Tracked practice assets:** [`Unpivot & Pivot Columns.xlsx`](../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/Unpivot%20%26%20Pivot%20Columns.xlsx) · Excel workbook<br>[`unpivot.pbix`](../05-Data-Transformation/Ep40-41-Unpivot-and-Pivot-Columns/unpivot.pbix) · Power BI report
- **Practice focus:** Pivot the long result back to columns and choose an aggregation only when duplicate keys require it.
- **Validation checkpoint:** Reconcile values with the original wide table and explain any aggregation.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 42 · Double Headers Issue

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep42-Double-Headers-Issue/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Promote/repair multi-row headers and fill down grouping labels where appropriate.
- **Validation checkpoint:** Check that every output column has a unique meaningful name and records retain their intended grain.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 43 · Append (Theory)

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep43-44-Append-Queries/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Compare source schemas before appending and identify missing/extra columns.
- **Validation checkpoint:** Explain how column names and data types affect the combined table.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 44 · Append

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep43-44-Append-Queries/README.md)
- **Tracked practice assets:** No tracked local binary practice asset detected. Use the official lesson resource or the live connector/service required by the lesson.
- **Practice focus:** Append the supplied compatible tables and inspect the combined schema.
- **Validation checkpoint:** Reconcile input/output row counts and inspect nulls introduced by missing columns.
- **Evidence to save:** Save connection/configuration notes or a small independent reproduction; never include credentials.

### Ep. 45 · Merge & Join Kind (Theory)

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/README.md)
- **Tracked practice assets:** [`Merge.xlsx`](../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/Merge.xlsx) · Excel workbook
- **Practice focus:** Choose a join kind for a concrete business question and predict which keys survive.
- **Validation checkpoint:** Check uniqueness on the lookup side and count unmatched keys.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 46 · Merge & Join Kind

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/README.md)
- **Tracked practice assets:** [`Merge.xlsx`](../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/Merge.xlsx) · Excel workbook
- **Practice focus:** Merge the supplied tables and expand only the required fields.
- **Validation checkpoint:** Validate row counts before/after expansion and detect duplicate-key row multiplication.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 47 · Fuzzy Match

- **Lesson folder:** [Open episode notes](../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/README.md)
- **Tracked practice assets:** [`Merge.xlsx`](../05-Data-Transformation/Ep45-47-Merge-and-Fuzzy-Match/Merge.xlsx) · Excel workbook
- **Practice focus:** Apply fuzzy matching to inconsistent text keys and inspect match confidence/threshold behavior.
- **Validation checkpoint:** Manually review false positives and unmatched records; do not treat fuzzy matches as verified identity.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 48 · Horizontal Date Matrix

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep48-Horizontal-Date-Matrix/README.md)
- **Tracked practice assets:** [`Horizontal Date Matrix Case.xlsx`](../06-Case-Studies/Ep48-Horizontal-Date-Matrix/Horizontal%20Date%20Matrix%20Case.xlsx) · Excel workbook<br>[`Horizontal Date Matrix.pbix`](../06-Case-Studies/Ep48-Horizontal-Date-Matrix/Horizontal%20Date%20Matrix.pbix) · Power BI report
- **Practice focus:** Normalize the horizontal date matrix into a row-based fact-like structure.
- **Validation checkpoint:** Check that each entity-date observation is represented once and totals reconcile.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 49 · Fragmented Rows

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep49-Fragmented-Rows/README.md)
- **Tracked practice assets:** [`Fragmented Rows Case.xlsx`](../06-Case-Studies/Ep49-Fragmented-Rows/Fragmented%20Rows%20Case.xlsx) · Excel workbook<br>[`Fragmented Rows.pbix`](../06-Case-Studies/Ep49-Fragmented-Rows/Fragmented%20Rows.pbix) · Power BI report
- **Practice focus:** Reconstruct fragmented records using grouping/ordering logic and explicit fill rules.
- **Validation checkpoint:** Compare record counts before/after and inspect boundary rows where fragments begin/end.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 50 · GDP Database

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep50-GDP-Database/README.md)
- **Tracked practice assets:** [`GDP Database.txt`](../06-Case-Studies/Ep50-GDP-Database/GDP%20Database.txt) · Text
- **Practice focus:** Import the GDP text source and normalize country/year/value fields.
- **Validation checkpoint:** Check numeric parsing, country identifiers, missing values, and year coverage.
- **Evidence to save:** Save a reproducible query, small output sample, and assumptions/edge-case notes.

### Ep. 51 · Fragmented, Duplicate & Merge

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep51-Fragmented-Duplicate-and-Merge/README.md)
- **Tracked practice assets:** [`Fragmented Duplicate & Merge.pbix`](../06-Case-Studies/Ep51-Fragmented-Duplicate-and-Merge/Fragmented%20Duplicate%20%26%20Merge.pbix) · Power BI report<br>[`Fragmented Duplicate & Merge.xlsx`](../06-Case-Studies/Ep51-Fragmented-Duplicate-and-Merge/Fragmented%20Duplicate%20%26%20Merge.xlsx) · Excel workbook
- **Practice focus:** Resolve fragmented rows and duplicates before merging related tables.
- **Validation checkpoint:** Document the deduplication key and prove the merge does not multiply facts unexpectedly.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 52 · Monthly Sales (Actual vs Budget)

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep52-Monthly-Sales-Actual-vs-Budget/README.md)
- **Tracked practice assets:** [`Monthly Sales (Actual vs Budget).pbix`](../06-Case-Studies/Ep52-Monthly-Sales-Actual-vs-Budget/Monthly%20Sales%20%28Actual%20vs%20Budget%29.pbix) · Power BI report<br>[`Monthly Sales (Actual vs Budget).xlsx`](../06-Case-Studies/Ep52-Monthly-Sales-Actual-vs-Budget/Monthly%20Sales%20%28Actual%20vs%20Budget%29.xlsx) · Excel workbook
- **Practice focus:** Align monthly budget values with daily actuals using a clearly defined date grain.
- **Validation checkpoint:** Validate monthly totals and explain how budget values are allocated or compared.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 53 · Group By (Actual vs Forecast)

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep53-Group-By-Actual-vs-Forecast/README.md)
- **Tracked practice assets:** [`Group By (Actual vs Forecast).pbix`](../06-Case-Studies/Ep53-Group-By-Actual-vs-Forecast/Group%20By%20%28Actual%20vs%20Forecast%29.pbix) · Power BI report<br>[`SalesRep Actual VS Forecast.xlsx`](../06-Case-Studies/Ep53-Group-By-Actual-vs-Forecast/SalesRep%20Actual%20VS%20Forecast.xlsx) · Excel workbook
- **Practice focus:** Group sales records and compare actual versus forecast at a consistent grain.
- **Validation checkpoint:** Reconcile grouped totals with the source and verify grouping keys.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 54 · Complex Header Structure

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep54-Complex-Header-Structure/README.md)
- **Tracked practice assets:** [`Complex Header Structure Case.xlsx`](../06-Case-Studies/Ep54-Complex-Header-Structure/Complex%20Header%20Structure%20Case.xlsx) · Excel workbook<br>[`Complex Header Structure.pbix`](../06-Case-Studies/Ep54-Complex-Header-Structure/Complex%20Header%20Structure.pbix) · Power BI report
- **Practice focus:** Flatten the complex header structure into a stable column schema.
- **Validation checkpoint:** Check header uniqueness, nulls introduced by fill operations, and record grain.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 55 · Full Project from Multiple Data Sources

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep55-Full-Project-Multiple-Sources/README.md)
- **Tracked practice assets:** [`Customer Database.xlsx`](../06-Case-Studies/Ep55-Full-Project-Multiple-Sources/Customer%20Database.xlsx) · Excel workbook<br>[`Product Database.xlsx`](../06-Case-Studies/Ep55-Full-Project-Multiple-Sources/Product%20Database.xlsx) · Excel workbook<br>[`SalesFullProject.pbix`](../06-Case-Studies/Ep55-Full-Project-Multiple-Sources/SalesFullProject.pbix) · Power BI report
- **Practice focus:** Integrate customer and product sources with the sales PBIX project; identify the sales grain before modeling.
- **Validation checkpoint:** Validate dimension key uniqueness, fact foreign-key coverage, and source-to-model totals.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 56 · Multi-Source Data Integration & Modeling

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep56-Multi-Source-Integration-and-Modeling/README.md)
- **Tracked practice assets:** [`Category Database.xlsx`](../06-Case-Studies/Ep56-Multi-Source-Integration-and-Modeling/Category%20Database.xlsx) · Excel workbook<br>[`Customer Database.txt`](../06-Case-Studies/Ep56-Multi-Source-Integration-and-Modeling/Customer%20Database.txt) · Text<br>[`Product Database.pdf`](../06-Case-Studies/Ep56-Multi-Source-Integration-and-Modeling/Product%20Database.pdf) · PDF
- **Practice focus:** Combine the category, customer, and product sources while documenting source-specific transformations.
- **Validation checkpoint:** Check key consistency across formats and document the intended model relationships.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 57 · Inconsistent Data Sources

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep57-Inconsistent-Data-Sources/README.md)
- **Tracked practice assets:** [`Case study.pbix`](../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Case%20study.pbix) · Power BI report<br>[`New Microsoft Excel Worksheet.xlsx`](../06-Case-Studies/Ep57-Inconsistent-Data-Sources/New%20Microsoft%20Excel%20Worksheet.xlsx) · Excel workbook<br>[`New Text Document.txt`](../06-Case-Studies/Ep57-Inconsistent-Data-Sources/New%20Text%20Document.txt) · Text<br>[`Year - 2005.xlsx`](../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Year%20-%202005.xlsx) · Excel workbook<br>[`Year - 2006.xlsx`](../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Year%20-%202006.xlsx) · Excel workbook<br>[`Year - 2007.xlsx`](../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Year%20-%202007.xlsx) · Excel workbook<br>[`Year - 2008.xlsx`](../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Year%20-%202008.xlsx) · Excel workbook<br>[`Year - 2009.xlsx`](../06-Case-Studies/Ep57-Inconsistent-Data-Sources/Year%20-%202009.xlsx) · Excel workbook
- **Practice focus:** Build a folder-ingestion approach that filters inconsistent and irrelevant files before combining.
- **Validation checkpoint:** Test a new year file, a lock file, and a malformed/unexpected file; confirm refresh resilience.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 58 · Hardcode vs Logic

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep58-Hardcode-vs-Logic/README.md)
- **Tracked practice assets:** [`Hardcode vs Logic.xlsx`](../06-Case-Studies/Ep58-Hardcode-vs-Logic/Hardcode%20vs%20Logic.xlsx) · Excel workbook
- **Practice focus:** Replace a hardcoded rule with a rule derived from source values or parameters.
- **Validation checkpoint:** Add a new category/value and verify the logic adapts without editing the query.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 59 · Context vs Logic

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep59-Context-vs-Logic/README.md)
- **Tracked practice assets:** [`Context vs Logic (Case Study).pbix`](../06-Case-Studies/Ep59-Context-vs-Logic/Context%20vs%20Logic%20%28Case%20Study%29.pbix) · Power BI report
- **Practice focus:** Separate evaluation context from the intended analytical rule in the case study.
- **Validation checkpoint:** Use a small counterexample to explain why the original logic does or does not generalize.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 60 · Locale (Dates vs. Numbers)

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep60-Locale-Dates-vs-Numbers/README.md)
- **Tracked practice assets:** [`DatesCSV 23Aug26.csv`](../06-Case-Studies/Ep60-Locale-Dates-vs-Numbers/DatesCSV%2023Aug26.csv) · CSV<br>[`Locale (Dates vs. Numbers).pbix`](../06-Case-Studies/Ep60-Locale-Dates-vs-Numbers/Locale%20%28Dates%20vs.%20Numbers%29.pbix) · Power BI report
- **Practice focus:** Parse dates and numbers using explicit regional interpretation for mixed-locale data.
- **Validation checkpoint:** Test ambiguous day/month values and decimal separators against known examples.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 61 · Vertical Headers Structure

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep61-Vertical-Headers-Structure/README.md)
- **Tracked practice assets:** [`Vertical Header Structure.xlsx`](../06-Case-Studies/Ep61-Vertical-Headers-Structure/Vertical%20Header%20Structure.xlsx) · Excel workbook<br>[`Vertical Headers Structure.pbix`](../06-Case-Studies/Ep61-Vertical-Headers-Structure/Vertical%20Headers%20Structure.pbix) · Power BI report
- **Practice focus:** Transform vertical header/value pairs into a structured table with meaningful columns.
- **Validation checkpoint:** Check that labels and values remain aligned after fill/transpose/reshape operations.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 62 · Practical Exercise - 1

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep62-Practical-Exercise-1/README.md)
- **Tracked practice assets:** [`Practical Exercise (1).pbix`](../06-Case-Studies/Ep62-Practical-Exercise-1/Practical%20Exercise%20%281%29.pbix) · Power BI report<br>[`Practical Exercise -1 30Aug26.xlsx`](../06-Case-Studies/Ep62-Practical-Exercise-1/Practical%20Exercise%20-1%2030Aug26.xlsx) · Excel workbook
- **Practice focus:** Attempt the first practical exercise before inspecting the supplied PBIX solution.
- **Validation checkpoint:** Record the approach, compare the output, and explain one difference or improvement.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 63 · Practical Exercise - 2

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep63-Practical-Exercise-2/README.md)
- **Tracked practice assets:** [`Practical Exercise (2).pbix`](../06-Case-Studies/Ep63-Practical-Exercise-2/Practical%20Exercise%20%282%29.pbix) · Power BI report<br>[`Practical Exercise -2 2Sep26.xlsx`](../06-Case-Studies/Ep63-Practical-Exercise-2/Practical%20Exercise%20-2%202Sep26.xlsx) · Excel workbook
- **Practice focus:** Attempt the second practical exercise independently and use the PBIX as a comparison reference.
- **Validation checkpoint:** Validate row counts, key fields, output types, and totals.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 64 · Multi-Bank PDF Consolidation

- **Lesson folder:** [Open episode notes](../06-Case-Studies/Ep64-Multi-Bank-PDF-Consolidation/README.md)
- **Tracked practice assets:** [`Alrajhi Bank.pdf`](../06-Case-Studies/Ep64-Multi-Bank-PDF-Consolidation/Alrajhi/Alrajhi%20Bank.pdf) · PDF<br>[`Multi-Bank PDF Consolidation.pbix`](../06-Case-Studies/Ep64-Multi-Bank-PDF-Consolidation/Multi-Bank%20PDF%20Consolidation.pbix) · Power BI report<br>[`SNB Bank.pdf`](../06-Case-Studies/Ep64-Multi-Bank-PDF-Consolidation/SNB/SNB%20Bank.pdf) · PDF
- **Practice focus:** Consolidate the Alrajhi and SNB PDF statements using a repeatable extraction pattern.
- **Validation checkpoint:** Compare extracted transactions/totals with each source statement and preserve bank/source identity.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 65 · Null vs. Blank – Full Explanation

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep65-Null-vs-Blank/README.md)
- **Tracked practice assets:** [`Null vs Blank.pbix`](../07-Power-Query-Engine-and-M-Language/Ep65-Null-vs-Blank/Null%20vs%20Blank.pbix) · Power BI report<br>[`Test.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep65-Null-vs-Blank/Test.xlsx) · Excel workbook
- **Practice focus:** Compare null, blank text, and empty values in the supplied test data.
- **Validation checkpoint:** Check how each behaves in filters, type conversion, and downstream expressions.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 66 · Cartesian Join

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep66-Cartesian-Join/README.md)
- **Tracked practice assets:** [`Cartesian Join.pbix`](../07-Power-Query-Engine-and-M-Language/Ep66-Cartesian-Join/Cartesian%20Join.pbix) · Power BI report<br>[`Cartesian Join.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep66-Cartesian-Join/Cartesian%20Join.xlsx) · Excel workbook
- **Practice focus:** Create a Cartesian product and calculate expected row multiplication before execution.
- **Validation checkpoint:** Validate output row count equals the product of input row counts for non-empty inputs.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 67 · Safe vs. Breaking Changes

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep67-Safe-vs-Breaking-Changes/README.md)
- **Tracked practice assets:** [`Safe vs. Breaking Changes.pbix`](../07-Power-Query-Engine-and-M-Language/Ep67-Safe-vs-Breaking-Changes/Safe%20vs.%20Breaking%20Changes.pbix) · Power BI report<br>[`Safe vs. Breaking Changes.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep67-Safe-vs-Breaking-Changes/Safe%20vs.%20Breaking%20Changes.xlsx) · Excel workbook<br>[`Very Important Notes.pdf`](../07-Power-Query-Engine-and-M-Language/Ep67-Safe-vs-Breaking-Changes/Very%20Important%20Notes.pdf) · PDF
- **Practice focus:** Classify query edits as safe or breaking and inspect downstream dependencies.
- **Validation checkpoint:** Test a rename/type/schema change and identify affected steps and consumers.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 68 · Step Error vs. Cell Error

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep68-Step-Error-vs-Cell-Error/README.md)
- **Tracked practice assets:** [`Eps 68 - Step Error vs. Cell Error.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep68-Step-Error-vs-Cell-Error/Eps%2068%20-%20Step%20Error%20vs.%20Cell%20Error.xlsx) · Excel workbook<br>[`Step Error vs. Cell Error.pbix`](../07-Power-Query-Engine-and-M-Language/Ep68-Step-Error-vs-Cell-Error/Step%20Error%20vs.%20Cell%20Error.pbix) · Power BI report
- **Practice focus:** Create or inspect both step-level and cell-level errors and compare their impact.
- **Validation checkpoint:** Record whether the query refreshes and how errors can be isolated without silently discarding data.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 69 · M Language (Theory)

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/README.md)
- **Tracked practice assets:** [`M Language.pbix`](../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/M%20Language.pbix) · Power BI report<br>[`M Language.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/M%20Language.xlsx) · Excel workbook
- **Practice focus:** Read M expressions as values and functions; inspect let/in scope, lists, records, and tables.
- **Validation checkpoint:** Explain evaluation dependencies and test a small expression in a blank query.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 70 · M Language

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/README.md)
- **Tracked practice assets:** [`M Language.pbix`](../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/M%20Language.pbix) · Power BI report<br>[`M Language.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep69-70-M-Language-Fundamentals/M%20Language.xlsx) · Excel workbook
- **Practice focus:** Rebuild a compact M query using explicit let bindings, functions, and table/list operations.
- **Validation checkpoint:** Change one input and explain how the expression evaluates.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 71 · Practical Exercise - 3

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep71-Practical-Exercise-3/README.md)
- **Tracked practice assets:** [`Ep. 71.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep71-Practical-Exercise-3/Ep.%2071.xlsx) · Excel workbook<br>[`Practical Exercise - 3.pbix`](../07-Power-Query-Engine-and-M-Language/Ep71-Practical-Exercise-3/Practical%20Exercise%20-%203.pbix) · Power BI report
- **Practice focus:** Complete the practical M exercise without copying the PBIX query steps.
- **Validation checkpoint:** Save your solution, compare with the reference, and record correctness and alternatives.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 72 · Helper Queries

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/README.md)
- **Tracked practice assets:** [`Administration.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Administration.xlsx) · Excel workbook<br>[`Business Development.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Business%20Development.xlsx) · Excel workbook<br>[`Customer Service.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Customer%20Service.xlsx) · Excel workbook<br>[`Finance.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Finance.xlsx) · Excel workbook<br>[`Human Resources.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Human%20Resources.xlsx) · Excel workbook<br>[`IT.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/IT.xlsx) · Excel workbook<br>[`Legal.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Department%20Folder/Legal.xlsx) · Excel workbook<br>[`Helper Queries.pbix`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries.pbix) · Power BI report<br>[`Administration.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Administration.xlsx) · Excel workbook<br>[`Business Development.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Business%20Development.xlsx) · Excel workbook<br>[`Customer Service.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Customer%20Service.xlsx) · Excel workbook<br>[`Finance.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Finance.xlsx) · Excel workbook<br>[`Human Resources.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Human%20Resources.xlsx) · Excel workbook<br>[`IT.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/IT.xlsx) · Excel workbook<br>[`Legal.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep72-Helper-Queries/Helper%20Queries/Legal.xlsx) · Excel workbook
- **Practice focus:** Inspect the helper-query PBIX and the two department-folder layouts; distinguish staging/helper queries from final outputs.
- **Validation checkpoint:** Verify folder filters, function invocation, and combined row counts.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 73 · Build Custom Functions

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep73-Build-Custom-Functions/README.md)
- **Tracked practice assets:** [`Build Custom Functions.pbix`](../07-Power-Query-Engine-and-M-Language/Ep73-Build-Custom-Functions/Build%20Custom%20Functions.pbix) · Power BI report<br>[`Ep. 73.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep73-Build-Custom-Functions/Ep.%2073.xlsx) · Excel workbook
- **Practice focus:** Build a typed custom function and invoke it against the supplied workbook.
- **Validation checkpoint:** Test valid, null, and invalid parameter values and document the function contract.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 74 · Frequency vs. Sequence Analysis

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep74-Frequency-vs-Sequence-Analysis/README.md)
- **Tracked practice assets:** [`Frequency vs Sequence Analysis.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep74-Frequency-vs-Sequence-Analysis/Frequency%20vs%20Sequence%20Analysis.xlsx) · Excel workbook<br>[`Frequency vs. Sequence Analysis.pbix`](../07-Power-Query-Engine-and-M-Language/Ep74-Frequency-vs-Sequence-Analysis/Frequency%20vs.%20Sequence%20Analysis.pbix) · Power BI report
- **Practice focus:** Calculate frequency and sequence metrics using stable sort/index logic.
- **Validation checkpoint:** Test ties, repeated events, missing dates, and sequence boundaries.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 75 · Missing Fields

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep75-Missing-Fields/README.md)
- **Tracked practice assets:** [`Missing Fields.pbix`](../07-Power-Query-Engine-and-M-Language/Ep75-Missing-Fields/Missing%20Fields.pbix) · Power BI report<br>[`Missing Fields.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep75-Missing-Fields/Missing%20Fields.xlsx) · Excel workbook
- **Practice focus:** Handle fields that may be absent from a record/table using an explicit missing-field policy.
- **Validation checkpoint:** Test both present and absent columns and ensure the fallback is intentional.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 76 · Away From Zero

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep76-Away-From-Zero/README.md)
- **Tracked practice assets:** [`Away From Zero.pbix`](../07-Power-Query-Engine-and-M-Language/Ep76-Away-From-Zero/Away%20From%20Zero.pbix) · Power BI report<br>[`Away From Zero.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep76-Away-From-Zero/Away%20From%20Zero.xlsx) · Excel workbook
- **Practice focus:** Compare midpoint rounding modes, including AwayFromZero, with positive and negative values.
- **Validation checkpoint:** Test positive/negative halves and document the business rounding rule.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 77 · The Logic of Thinking

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep77-The-Logic-of-Thinking/README.md)
- **Tracked practice assets:** [`The Logic of Thinking.pbix`](../07-Power-Query-Engine-and-M-Language/Ep77-The-Logic-of-Thinking/The%20Logic%20of%20Thinking.pbix) · Power BI report<br>[`The Logic of Thinking.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep77-The-Logic-of-Thinking/The%20Logic%20of%20Thinking.xlsx) · Excel workbook
- **Practice focus:** Translate the problem statement into declarative steps before writing M.
- **Validation checkpoint:** Explain why the transformation is correct and identify hidden assumptions.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 78 · Worksheets Name

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/README.md)
- **Tracked practice assets:** [`Administration.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Administration.xlsx) · Excel workbook<br>[`Business Development.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Business%20Development.xlsx) · Excel workbook<br>[`Customer Service.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Customer%20Service.xlsx) · Excel workbook<br>[`Finance.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Finance.xlsx) · Excel workbook<br>[`Human Resources.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Human%20Resources.xlsx) · Excel workbook<br>[`IT.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/IT.xlsx) · Excel workbook<br>[`Legal.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Employees%20Datebase/Legal.xlsx) · Excel workbook<br>[`HRDatabase.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/HRDatabase.xlsx) · Excel workbook<br>[`HRDatabase2.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/HRDatabase2.xlsx) · Excel workbook<br>[`Worksheet Names.pbix`](../07-Power-Query-Engine-and-M-Language/Ep78-Worksheets-Name/Worksheet%20Names.pbix) · Power BI report
- **Practice focus:** Combine worksheets across the department workbooks using worksheet names as metadata.
- **Validation checkpoint:** Test a new worksheet and a missing worksheet; verify selection and schema handling.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 79 · Transform All Columns

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep79-Transform-All-Columns/README.md)
- **Tracked practice assets:** [`Transform All Columns.pbix`](../07-Power-Query-Engine-and-M-Language/Ep79-Transform-All-Columns/Transform%20All%20Columns.pbix) · Power BI report<br>[`Transform All Columns.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep79-Transform-All-Columns/Transform%20All%20Columns.xlsx) · Excel workbook
- **Practice focus:** Apply a transformation across columns using an explicit column/type policy.
- **Validation checkpoint:** Confirm non-target columns remain unchanged and null/type edge cases are handled.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 80 · Null Coalescing Operator

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep80-Null-Coalescing-Operator/README.md)
- **Tracked practice assets:** [`Null Coalescing Operator.pbix`](../07-Power-Query-Engine-and-M-Language/Ep80-Null-Coalescing-Operator/Null%20Coalescing%20Operator.pbix) · Power BI report<br>[`Null Coalescing Operator.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep80-Null-Coalescing-Operator/Null%20Coalescing%20Operator.xlsx) · Excel workbook
- **Practice focus:** Use the null-coalescing operator for a deliberate fallback expression.
- **Validation checkpoint:** Distinguish null from empty text/zero and test precedence/parentheses.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 81 · Try & Otherwise

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep81-Try-and-Otherwise/README.md)
- **Tracked practice assets:** [`Try and Otherwise.pbix`](../07-Power-Query-Engine-and-M-Language/Ep81-Try-and-Otherwise/Try%20and%20Otherwise.pbix) · Power BI report<br>[`Try and Otherwise.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep81-Try-and-Otherwise/Try%20and%20Otherwise.xlsx) · Excel workbook
- **Practice focus:** Use try/otherwise to handle an expected failure while preserving diagnostic information where needed.
- **Validation checkpoint:** Test success and failure paths; ensure the fallback does not hide data-quality defects.
- **Evidence to save:** Save a rebuilt PBIX or screenshots of the query/model/report plus a short validation note.

### Ep. 82 · Reference Outside Scope

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep82-Reference-Outside-Scope/README.md)
- **Tracked practice assets:** [`Reference_Outside_Scope.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep82-Reference-Outside-Scope/Reference_Outside_Scope.xlsx) · Excel workbook
- **Practice focus:** Inspect a reference that is outside the current lexical scope and trace the evaluation dependency.
- **Validation checkpoint:** Explain why the identifier is or is not visible at the point of use.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

### Ep. 83 · Complex Date Transformations

- **Lesson folder:** [Open episode notes](../07-Power-Query-Engine-and-M-Language/Ep83-Complex-Date-Transformations/README.md)
- **Tracked practice assets:** [`Complex_Date_Transformations.xlsx`](../07-Power-Query-Engine-and-M-Language/Ep83-Complex-Date-Transformations/Complex_Date_Transformations.xlsx) · Excel workbook
- **Practice focus:** Build date transformations for quarters, durations, and custom periods using explicit calendar assumptions.
- **Validation checkpoint:** Test month/year boundaries, leap days, fiscal boundaries, and null dates.
- **Evidence to save:** Save the query output or a before/after workbook and record row counts, types, and key checks.

## Cross-episode asset handling

| Asset | Recommended checks |
|---|---|
| `.xlsx` / `.xls` | Inspect sheets/tables, intended object, column types, row counts; refresh after adding a row. |
| `.csv` / `.txt` | Check delimiter, encoding, quoting, headers, locale, and malformed rows. Keep raw source unchanged. |
| `.pdf` | Identify table boundaries and repeated headers; compare extracted row counts/totals with the source. |
| `.json` | Inspect record/list nesting, expand deliberately, preserve identifiers, test optional/missing fields. |
| `.pbix` | Inspect queries/model/report separately; rebuild at least one key transformation without copying. |
| `.pbit` | Inspect parameters and source prompts; instantiate with safe test configuration. |

## Boundaries

- A file being present does not mean it has been independently audited or that the lesson has been completed.
- Some lessons are service-based and have no local binary asset.
- Several episodes share a folder and therefore share practice files.
- Keep private credentials, personal data, and restricted source material out of committed evidence.
