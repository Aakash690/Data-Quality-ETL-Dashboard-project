# 📊 ETL Data Quality & Monitoring Dashboard

A real-world data analytics project that simulates enterprise ETL job monitoring and data quality reporting using **Python, SQL (simulated with CSV), and Power BI**.

> 👤 **Author**: Aakash Srivastava  
> 🏢 Clients Served: Intel (Data Compliance), VMware (Unified Reporting Platform)

---

## 🎯 Project Goal

To build a lightweight but insightful data quality monitoring tool for ETL jobs — using automation in Python, data cleanup, and visual analytics in Power BI.

---

## 🛠 Tech Stack

| Tool         | Purpose                          |
|--------------|----------------------------------|
| **Python**   | Data cleaning, delay calculation, email alert simulation |
| **Power BI** | Visualization & Dashboarding     |
| **Pandas**   | Data wrangling                   |
| **CSV (SQL-like)** | Simulates ETL job logs       |

---

## 🧪 Key Features

- ✅ Detects null values, duplicates, and job delays
- ✅ Calculates average and maximum delay per job
- ✅ Simulates alert emails if quality thresholds are crossed
- ✅ Power BI dashboard with filters, KPIs, and visuals
- ✅ Easy-to-read summary table and date-wise delay line chart

---
## Run The Project
### Install required Python packages
```bash
pip install pandas
```
### Run the Python script
```bash
python '.\python etl_quality_check.py'
```
## 📁 Folder Structure

data-quality-etl-dashboard/
├── data/
│ ├── etl_sample_data.csv # Input simulated job data
│ └── etl_clean_output.csv # Cleaned output for Power BI
├── scripts/
│ └── etl_quality_check.py # Python automation script
├── PowerBI_Dashboard.pbix # Power BI dashboard file
├── README.md # You're here!
