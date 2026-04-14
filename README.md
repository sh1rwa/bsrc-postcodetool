# Bristol Postcode to Ward Lookup Tool

This is an interactive web tool designed to map Bristol postcodes to their corresponding wards and provide quick insights into the data.

It was built during my placement at a charity, where staff frequently needed to identify wards for reporting and data entry. Previously, this process relied on manually searching through Excel spreadsheets. This tool streamlines that workflow into a fast, user-friendly interface with added data visualisation and filtering capabilities.

---

## Live Tool

Access the tool here:  
https://bristolpostcode2ward.onrender.com

---

## What the tool does

- Allows users to enter one or multiple postcodes at once  
- Instantly returns the corresponding ward for each postcode  
- Supports duplicate postcodes for real-world data entry scenarios  
- Highlights invalid inputs and postcodes not found in the dataset  
- Provides intelligent suggestions for mistyped postcodes  
- Enables batch processing for large inputs  
- Allows results to be downloaded as a CSV file  

---

## Data visualisation & filtering

- Generate a bar chart showing the distribution of postcodes across wards  
- Filter results by ward using an interactive dropdown with checkboxes to hide invalid/not found results  
- View dynamic counts for each ward directly in the filter menu  
- Automatically update the chart, table, and totals when filters are applied  
- Reset filters to return to the full dataset  
- Export the chart as an image, including postcode counts per ward  

---

## Who it’s for

This tool was built for staff and volunteers working at charities across Bristol who need to:

- Quickly identify wards for clients  
- Reduce manual lookup time  
- Improve data accuracy when inputting into systems like Salesforce  
- Gain quick insights into postcode distributions for reporting  

---

## Technologies used

- **Python (Flask)** – backend API for postcode lookup  
- **Pandas** – data cleaning and processing from Excel  
- **HTML, CSS, JavaScript** – frontend interface and interactivity  
- **Chart.js** – data visualisation  
- **Render** – deployment and hosting  
- **GitHub** – version control  

---

## Key features

- Fast lookup using a pre-processed dataset  
- Live autocomplete suggestions while typing  
- Clickable corrections for incorrect postcodes  
- Input validation (invalid format vs not found)  
- Interactive filtering across chart and table  
- Dynamic counts and real-time updates  
- CSV export and chart image download  
- Clean, responsive UI with user guidance  

---

## How it works

The tool uses a cleaned dataset of Bristol postcodes mapped to wards.  
User input is sent to a Flask backend, which performs fast lookups using a dictionary-based approach. Results are returned instantly and rendered in the frontend, where additional features like filtering, charting, and exporting are handled dynamically.

---

## Notes

- The tool is designed specifically for Bristol postcodes  
- Duplicate entries are supported to reflect real-world usage  
- Invalid inputs are clearly highlighted and excluded from downloads  
- Filtering affects the table, chart, and total counts simultaneously  

---

## Future improvements

- Integration with Salesforce to automatically populate ward fields  
- More advanced postcode validation and matching  
- Enhanced visualisations (e.g. percentages, pie charts)  
- User authentication for internal deployment  

---
