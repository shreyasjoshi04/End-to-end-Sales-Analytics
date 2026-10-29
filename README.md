# End-to-end-Sales-Analytics
End-to-end sales analytics: Excel → Python (pandas) → MySQL → Power BI dashboard for monthly sales growth.

<h1 align="center">📊 Monthly Sales Growth Analysis</h1>

<p align="center">
  <b>An end-to-end data analytics pipeline: Excel → Python → MySQL → Power BI</b><br>
  Turning raw sales records into clean, queryable data and decision-ready insights.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pandas-Data%20Cleaning-150458?logo=pandas&logoColor=white" alt="pandas">
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?logo=powerbi&logoColor=black" alt="Power BI">
  <img src="https://img.shields.io/badge/Excel-Raw%20Data-217346?logo=microsoftexcel&logoColor=white" alt="Excel">
</p>

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Business Questions](#-business-questions)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Repository Structure](#-repository-structure)
- [Dataset](#-dataset)
- [Data Cleaning](#-data-cleaning)
- [Key Insights](#-key-insights)
- [Dashboard](#-dashboard)
- [How to Run](#-how-to-run)
- [Skills Demonstrated](#-skills-demonstrated)
- [Future Improvements](#-future-improvements)

---

## 🎯 Overview

Businesses live and die by their sales trends, but raw spreadsheets hide the story. This project builds a complete analytics workflow that:

1. **Extracts** raw sales data from Excel
2. **Cleans and transforms** it with Python (pandas)
3. **Loads** it into a MySQL database for structured storage and SQL querying
4. **Visualizes** monthly sales growth, profit and performance in a Power BI dashboard

The result is a reproducible pipeline that takes messy source data and turns it into insights anyone can read.

## ❓ Business Questions

- How are sales, cost and profit trending month over month?
- Which **regions** and **products** drive the most revenue and profit?
- Who are the **top customers**?
- What is the overall **profit margin**, and is it consistent across segments?
- Are there months with unusual growth or decline?

## 🏗️ Architecture

```
┌──────────────┐    ┌──────────────┐    ┌──────────────────┐    ┌───────────┐    ┌───────────┐
│ raw_data.xlsx│ →  │ cleaning.py  │ →  │ Sales_cleaned.csv│ →  │ main.py   │ →  │  MySQL    │
│  (520 rows)  │    │   (pandas)   │    │    (482 rows)    │    │(SQLAlchemy)│   │ salesdb   │
└──────────────┘    └──────────────┘    └──────────────────┘    └───────────┘    └─────┬─────┘
                                                                                       ↓
                                                                              ┌─────────────────┐
                                                                              │ Power BI (.pbix)│
                                                                              └─────────────────┘
```

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Source data | Microsoft Excel |
| Data cleaning & transformation | Python, pandas, openpyxl |
| Database | MySQL |
| DB connectivity | SQLAlchemy, PyMySQL |
| Visualization | Power BI Desktop |

## 📁 Repository Structure

```
├── raw_data.xlsx              # Original raw sales dataset (520 rows)
├── cleaning.py                # Cleaning + feature engineering script
├── Sales_cleaned.csv          # Cleaned dataset (482 rows)
├── main.py                    # Loads cleaned data into MySQL
├── connections.sql            # Database setup & sanity-check queries
├── Monthly_Sales_Growth.pbix  # Power BI dashboard
└── README.md
```

## 🗂️ Dataset

| Column | Type | Description |
|---|---|---|
| `Order_ID` | Integer | Unique order identifier |
| `Order_Date` | Date | Date the order was placed |
| `Customer` | Text | Customer name (10 customers) |
| `Region` | Text | North, South, East, West |
| `Product` | Text | Mobile, Laptop, Monitor, Printer, Tablet |
| `Sales` | Integer | Revenue from the order |
| `Cost` | Integer | Cost of the order |
| `profit` | Integer | **Derived:** `Sales − Cost` |
| `year` | Integer | **Derived:** extracted from `Order_Date` |
| `month` | Integer | **Derived:** extracted from `Order_Date` |

**Coverage:** January 2023 to December 2024 · **482 unique orders**

## 🧹 Data Cleaning

| Step | Action | Impact |
|---|---|---|
| 1 | Removed duplicate rows | 20 duplicates removed |
| 2 | Converted `Order_Date` to datetime (`errors='coerce'`) | Invalid dates flagged |
| 3 | Dropped rows with unparseable dates | 18 rows removed |
| 4 | Engineered `profit`, `year`, `month` | 3 new analysis-ready columns |
| 5 | Exported to `Sales_cleaned.csv` | 520 → **482 clean rows** |

## 🔍 Key Insights

### Overall performance

| Metric | Value |
|---|---|
| 💰 Total Sales | **₹19,809,635** |
| 📦 Total Cost | **₹14,817,481** |
| 📈 Total Profit | **₹4,992,154** |
| 🧮 Profit Margin | **25.2%** |
| 🧾 Average Order Value | **₹41,099** |
| 🛒 Total Orders | **482** |

### Region performance

| Region | Sales | Profit | Margin |
|---|---|---|---|
| South | ₹5,176,309 | ₹1,240,464 | 24.0% |
| North | ₹5,138,427 | ₹1,351,593 | **26.3%** |
| West | ₹4,819,905 | ₹1,186,520 | 24.6% |
| East | ₹4,674,994 | ₹1,213,577 | 26.0% |

- **South** leads in sales, but **North** earns the most profit thanks to the best margin (26.3%).
- Revenue is evenly spread across regions, so no single region dominates.

### Product performance

| Product | Sales | Profit | Margin |
|---|---|---|---|
| Printer | ₹4,562,567 | ₹1,163,637 | 25.5% |
| Tablet | ₹3,990,632 | ₹1,013,764 | 25.4% |
| Laptop | ₹3,967,919 | ₹974,693 | 24.6% |
| Monitor | ₹3,744,366 | ₹965,039 | **25.8%** |
| Mobile | ₹3,544,151 | ₹875,021 | 24.7% |

- **Printer** is the top product by both sales and profit.
- **Monitor** has the best margin (25.8%) despite lower volume.
- **Mobile** has the lowest sales and profit.

### Customer performance

- **Suresh** (₹2.30M) and **Vikas** (₹2.25M) are the top customers by revenue.
- **Priya** has the highest margin (27.6%) but the lowest revenue (₹1.46M), so there is room to grow the account.

### Sales trend

- **2023 was the stronger year:** ₹16.13M in sales and ₹4.09M in profit across 385 orders.
- **Peak month:** August 2023 with **₹1.93M** in sales, a +28% jump over July.
- **Biggest 2023 dip:** November 2023 fell 45% month over month, then recovered by 51% in December.
- **2024 data thins out sharply after March**, with very few orders recorded, so the month-over-month growth swings later in 2024 are large in percentage terms but small in absolute terms. This is worth keeping in mind when reading the dashboard.
- **Every order was profitable:** no order has a negative profit.

## 📊 Dashboard

The Power BI report (`Monthly_Sales_Growth.pbix`) is connected to the cleaned dataset and is built to track:

- 📈 **Monthly sales growth** (month-over-month %)
- 💵 **Sales, cost and profit** trends over time
- 🌍 **Regional** and 📦 **product-level** performance
- 👥 **Customer** contribution
- 🎛️ Filters by year, region and product

Open the `.pbix` file in **Power BI Desktop** to explore it interactively.

## ▶️ How to Run

### Prerequisites

- Python 3.9+
- MySQL Server (running locally)
- Power BI Desktop (to view the dashboard)

### Steps

**1. Get the project**

Download the repository as a ZIP or clone it with Git, then open a terminal in the project folder.

**2. Install dependencies**

```bash
pip install pandas openpyxl sqlalchemy pymysql
```

**3. Clean the data**

```bash
python cleaning.py
```

This reads the raw Excel file and generates `Sales_cleaned.csv`.

**4. Create the database**

Run this in MySQL:

```sql
CREATE DATABASE salesdb;
```

**5. Load data into MySQL**

Update the connection string in `main.py` with your own MySQL username and password, then run:

```bash
python main.py
```

This creates the `sales_data` table inside `salesdb`.

**6. Verify the load**

```sql
USE salesdb;
SELECT COUNT(*) FROM sales_data;   -- expected: 482
```

**7. Open the dashboard**

Open `Monthly_Sales_Growth.pbix` in Power BI Desktop and refresh the data source if needed.

## 💡 Skills Demonstrated

- **Data cleaning:** deduplication, date parsing, handling invalid records
- **Feature engineering:** profit, year and month derivation
- **ETL pipeline design:** Excel → CSV → MySQL
- **SQL:** database creation, table loading, validation queries
- **Python:** pandas, SQLAlchemy, working with relational databases
- **Business intelligence:** KPI design and dashboarding in Power BI
- **Analytical storytelling:** turning data into business insights

## 🚀 Future Improvements

- Automate the pipeline with a scheduler (cron / Apache Airflow)
- Store database credentials securely in environment variables
- Add sales forecasting for upcoming months
- Add customer segmentation and retention analysis
- Add data-quality checks and logging to the cleaning step

---

<p align="center">⭐ If you found this project useful, consider giving it a star!</p>
