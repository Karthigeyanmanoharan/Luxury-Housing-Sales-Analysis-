# 🏙️ LUXURY HOUSING SALES ANALYSIS – BENGALURU

## 📌 PROJECT OVERVIEW

This project presents an end-to-end real estate analytics solution focused on the luxury housing market in Bengaluru. The objective is to simulate a real-world enterprise data pipeline by performing advanced data cleaning using **PYTHON**, loading the refined dataset into a **SQL** database, and building an interactive **POWER BI** dashboard directly connected to SQL for business intelligence and decision-making.

The analysis is conducted on a large-scale dataset containing 100,000+ housing records, enabling deep insights into pricing trends, builder performance, configuration demand, and infrastructure impact across Bengaluru’s micro-markets.

## 🎯 PROBLEM STATEMENT

Build a complete real estate analytics workflow using:
*   **PYTHON** for data cleaning and feature engineering
*   **SQL** for data warehousing and aggregation
*   **POWER BI** for interactive dashboards

The goal is to replicate a production-level analytics environment and derive actionable business insights for stakeholders in the luxury housing sector.

## 🧠 BUSINESS USE CASES

1. **MARKET INTELLIGENCE**: Identify high-performing micro-markets and builder-wise pricing trends.
2. **COMPETITIVE PRICING ANALYSIS**: Compare ticket prices across builders, configurations, and locations.
3. **CONFIGURATION DEMAND ANALYSIS**: Understand buyer preference for housing configurations (e.g., 3BHK, 4BHK).
4. **INFRASTRUCTURE & AMENITY IMPACT**: Analyze how infrastructure, connectivity, amenities, and traffic influence pricing.
5. **QUARTERLY TREND TRACKING**: Track market behavior across fiscal quarters to support investment decisions.
6. **SALES CHANNEL EFFECTIVENESS**: Evaluate which sales channels contribute most to primary market transactions.

## 🛠️ TECH STACK

*   **PYTHON** (Pandas, NumPy)
*   **POSTGRESQL**
*   **POWER BI**
*   **SQL**
*   **GIT & GITHUB**

## 🧩 DATASET DESCRIPTION

**DATASET SIZE**: 100,000+ rows
**DOMAIN**: Luxury Housing – Bengaluru

**KEY COLUMNS**:
- `Project_ID`, `Micro_Market`, `Developer_Name`
- `Ticket_Price_Cr`, `Unit_Size_Sqft`, `Configuration`
- `Amenity_Score`, `Connectivity_Score`, `Locality_Infra_Score`
- `Avg_Traffic_Time_Min`, `Transaction_Type`, `Sales_Channel`, `Purchase_Quarter`

## 🔄 PROJECT WORKFLOW

### 🐍 STEP 1: PYTHON – DATA CLEANING & FEATURE ENGINEERING
- Loaded raw CSV dataset and handled missing/invalid values.
- Corrected negative numerical values and **WINSORIZED** extreme outliers.
- **NORMALIZED** text fields and derived new features: **YEAR**, **QUARTER**, and **PRICE_PER_SQFT**.

### 🧠 STEP 2: SQL – DATA WAREHOUSING & AGGREGATION
- Created SQL tables programmatically using **PYTHON**.
- Executed multiple **AGGREGATION QUERIES** to analyze market trends and builder performance.
- Queries documented in: `sql/aggregation_queries.sql`

### 📊 STEP 3: POWER BI – INTERACTIVE DASHBOARD
- Connected **POWER BI** directly to **POSTGRESQL**.
- Built interactive visuals including **KPI CARDS**, **SLICERS**, and **DRILL-DOWN** analysis.

## 📈 SQL AGGREGATION HIGHLIGHTS

Key analyses performed:
*   **QUARTERLY BOOKING TRENDS** across micro-markets.
*   **BUILDER-WISE REVENUE** and average ticket size.
*   **CONFIGURATION DEMAND** distribution.
*   **TRAFFIC IMPACT** on demand and pricing.

## 📊 POWER BI VISUALIZATION OVERVIEW

- **MARKET TRENDS**: Quarterly transaction trends.
- **BUILDER PERFORMANCE**: Revenue comparison.
- **AMENITY IMPACT**: Pricing vs quality indicators.
- **TOP PERFORMERS**: Top 5 builders by revenue.

## 📊 POWER BI VISUALIZATION SCREENSHOTS

![Alt text](<Screenshot 2026-03-01 144353.png>)

![Alt text](<Screenshot 2026-03-01 144418.png>)

## ✅ RESULTS & INSIGHTS

- Identified premium and emerging micro-markets in Bengaluru.
- Revealed builder dominance and competitive pricing patterns.
- Found strong correlation between **AMENITY SCORES** and **PRICING**.

## 📂 PROJECT STRUCTURE

```text
Luxury_house_sale_analysis/
│
├── data/
│   ├── raw/
│   └── cleaned/
│
├── sql/
│   └── aggregation_queries.sql
│
├── notebooks/
│   └── data_cleaning_and_loading.py
│
├── power_bi/
│   └── dashboard.pbix
│
└── README.md
```

## 🏁 CONCLUSION

This project successfully demonstrates a real-world data analytics pipeline applied to luxury real estate. By integrating Python, SQL, and Power BI, it delivers actionable insights that can support pricing strategy, market expansion, and investment decision-making in the Bengaluru luxury housing market.
