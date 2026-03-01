#🏙️ Luxury Housing Sales Analysis – Bengaluru

---


##📌 Project Overview

This project presents an end-to-end real estate analytics solution focused on the luxury housing market in Bengaluru. The objective is to simulate a real-world enterprise data pipeline by performing advanced data cleaning using Python, loading the refined dataset into a SQL database, and building an interactive Power BI dashboard directly connected to SQL for business intelligence and decision-making.

The analysis is conducted on a large-scale dataset containing 100,000+ housing records, enabling deep insights into pricing trends, builder performance, configuration demand, and infrastructure impact across Bengaluru’s micro-markets.

---

##🎯 Problem Statement

Build a complete real estate analytics workflow using:

Python for data cleaning and feature engineering

SQL for data warehousing and aggregation

Power BI for interactive dashboards

The goal is to replicate a production-level analytics environment and derive actionable business insights for stakeholders in the luxury housing sector.

---

##🧠 Business Use Cases

1,Market Intelligence
Identify high-performing micro-markets and builder-wise pricing trends.

2.Competitive Pricing Analysis
Compare ticket prices across builders, configurations, and locations.

3.Configuration Demand Analysis
Understand buyer preference for housing configurations (e.g., 3BHK, 4BHK).

4.Infrastructure & Amenity Impact
Analyze how infrastructure, connectivity, amenities, and traffic influence pricing.

5.Quarterly Trend Tracking
Track market behavior across fiscal quarters to support investment decisions.

6.Sales Channel Effectiveness
Evaluate which sales channels contribute most to primary market transactions.

---

##🛠️ Tech Stack

-Python (Pandas, NumPy)

-PostgreSQL

-Power BI

-SQL

-Git & GitHub

##🧩 Dataset Description

Dataset Size: 100,000+ rows

Domain: Luxury Housing – Bengaluru

Key Columns:

-Project_ID

-Micro_Market

-Developer_Name

-Ticket_Price_Cr

-Unit_Size_Sqft

-Configuration

-Amenity_Score

-Connectivity_Score

-Locality_Infra_Score

-Avg_Traffic_Time_Min

-Transaction_Type (Primary / Secondary)

-Sales_Channel

-Purchase_Quarter (Date)

---

##🔄 Project Workflow
🐍 Step 1: Python – Data Cleaning & Feature Engineering

-Loaded raw CSV dataset

-Handled missing and invalid values

-Corrected negative numerical values

-Winsorized extreme outliers

-Normalized text fields

-Derived new features:

 *Year

 *Quarter

 *Price_per_Sqft

-Exported cleaned data for database insertion

Output: Cleaned dataset ready for SQL ingestion

🧠 Step 2: SQL – Data Warehousing & Aggregation

-Created SQL table programmatically using Python

-Inserted cleaned dataset into PostgreSQL

-Executed multiple aggregation queries to analyze:

*Market trends

*Builder performance

*Configuration demand

*Infrastructure & amenity impact

*Sales channel efficiency

📂 All queries are documented in:

sql/aggregation_queries.sql
📊 Step 3: Power BI – Interactive Dashboard

-Connected Power BI directly to PostgreSQL

-Built interactive dashboards with:

-Slicers for Builder, Quarter, Micro-Market

-KPI cards

-Bar, Line, Donut, and Matrix visuals

-Enabled drill-down analysis for deeper insights

##📈 SQL Aggregation Highlights

Key analyses performed using SQL:

-Quarterly booking trends across micro-markets

-Builder-wise revenue and average ticket size

-Configuration demand distribution

-Amenity and infrastructure score impact on pricing

-Traffic impact on demand

-Sales channel efficiency

-Top-performing builders by revenue

##📊 Power BI Visualization Overview

-Market Trends: Quarterly transaction trends by micro-market

-Builder Performance: Revenue and average ticket size comparison

-Configuration Demand: Most preferred housing configurations

-Amenity & Infrastructure Impact: Pricing vs quality indicators

-Sales Channel Analysis: Channel-wise contribution

-Top Performers: Top 5 builders by revenue

---

##📊 Power BI Visualization Screenshots


##✅ Results & Insights

-Identified premium and emerging micro-markets in Bengaluru

-Revealed builder dominance and competitive pricing patterns

-Found strong correlation between amenity/infrastructure scores and pricing

##📂 Project Structure
```
Luxury_house_sale_analysis/
│
├── data/
│   ├── raw/
│   ├── cleaned/
│
├── sql/
│   └── aggregation_queries.sql
│
├── notebooks / scripts/
│   └── data_cleaning_and_loading.py
│
├── power_bi/
│   └── dashboard.pbix
│
├── README.md
```

##🏁 Conclusion

This project successfully demonstrates a real-world data analytics pipeline applied to luxury real estate. By integrating Python, SQL, and Power BI, it delivers actionable insights that can support pricing strategy, market expansion, and investment decision-making in the Bengaluru luxury housing market.
