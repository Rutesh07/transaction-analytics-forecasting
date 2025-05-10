# 🛒 Transaction Analytics & Forecasting

This project simulates a real-world Python Developer Intern task focused on building a full data analytics pipeline for transactional data. The system includes automated data cleaning, customer segmentation using RFM and KMeans, and 90-day sales forecasting using Prophet.

## 🔍 Project Objectives

- Automate ingestion and preprocessing of transactional data
- Segment customers using RFM (Recency, Frequency, Monetary) analysis and clustering
- Forecast future sales trends using time-series modeling
- Provide reusable outputs: cleaned CSVs, charts, and summary tables

---

## 🧰 Technologies Used

- **Python 3.10+**
- **Pandas** for data manipulation
- **Scikit-learn** for clustering
- **Facebook Prophet** for forecasting
- **Matplotlib & Seaborn** for visualization

---

## 📁 Project Structure

```
python-intern-transaction-analytics/
├── data/
│   └── online_retail.xlsx
├── scripts/
│   ├── data_pipeline.py
│   ├── customer_segmentation.py
│   └── sales_forecasting.py
├── outputs/
│   ├── tables/
│   │   ├── cleaned_data.csv
│   │   ├── rfm_segmented.csv
│   │   ├── cluster_summary.csv
│   │   └── forecast_90_days.csv
│   └── charts/
│       ├── monetary_by_cluster.png
│       ├── sales_forecast.png
│       └── forecast_components.png
└── README.md
```

---

## ▶️ How to Run

1. Clone this repo and install requirements:

```bash
pip install -r requirements.txt
```

2. Run each script step-by-step:
```bash
python scripts/data_pipeline.py
python scripts/customer_segmentation.py
python scripts/sales_forecasting.py
```

3. Outputs will be saved in the `outputs/` folder.

---

## 📊 Sample Outputs

- RFM Segment Distribution: `monetary_by_cluster.png`
- Sales Forecast Chart: `sales_forecast.png`
- Forecast Table: `forecast_90_days.csv`

---

## 📌 Dataset Source

**Online Retail II Dataset**  
[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/online+retail+ii)

---

## 👨‍💻 Author

**Rutesh Zalavadiya**  
Master of Applied Computing @ University of Windsor  
GitHub: [github.com/ruteshz](https://github.com/ruteshz)

---

## ⭐️ If you found this helpful, give it a star!
