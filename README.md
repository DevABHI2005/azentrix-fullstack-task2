# 🌍 World Insights Lakehouse

## Global Population & Happiness Analytics Platform

A **Mini Data Lakehouse with Analytics Dashboard** built using **Python, SQLite, Parquet, Streamlit, and Docker Compose**.

This project demonstrates a complete **Data Engineering Pipeline**, from **multi-source data ingestion** to **analytics visualization**, following a modern layered architecture.

---

# 📌 Project Objective

Modern data engineering systems ingest data from multiple sources, store raw data separately, transform it into structured datasets, and provide analytics through dashboards.

This project implements that architecture by combining:

* 🌐 World Bank Population API
* 📄 World Happiness Report 2024 CSV

into a unified analytics platform.

---

# 🚀 Features

* ✅ Multi-source Data Ingestion
* ✅ Landing Zone (Raw Storage)
* ✅ Data Cleaning & Transformation
* ✅ Data Merging
* ✅ SQLite Database Storage
* ✅ Parquet Data Storage
* ✅ Analytics Layer
* ✅ Interactive Streamlit Dashboard
* ✅ Dockerized Deployment
* ✅ Data Quality Checks
* ✅ Automated Insights Generation

---

# 🏗 Project Architecture

```
                   World Bank API
                          │
                          ▼
             Raw Population Data (CSV)

                          │

World Happiness CSV ───────────────┐
                                   │
                                   ▼

                     Transformation Layer
                 (Cleaning + Merging + Validation)

                                   │
                  ┌────────────────┴──────────────┐
                  ▼                               ▼

          SQLite Database                 Parquet Storage

                  │                               │
                  └──────────────┬────────────────┘
                                 ▼

                    Analytics Query Layer

                                 ▼

                   Streamlit Analytics Dashboard
```

---

# 📂 Project Structure

```
world-insights-lakehouse/

│
├── analytics/
│      analytics_queries.py
│
├── dashboard/
│      app.py
│
├── data/
│      raw/
│      processed/
│      parquet/
│
├── database/
│      population.db
│
├── logs/
│
├── src/
│      ingest_api.py
│      ingest_csv.py
│      transform.py
│      load.py
│      logger.py
│      main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .env
```

---

# 📥 Data Sources

## Source 1

World Bank Population API

Provides:

* Country
* Country ID
* Year
* Population

---

## Source 2

World Happiness Report 2024 CSV

Provides:

* Happiness Score
* GDP
* Social Support
* Life Expectancy
* Freedom
* Corruption
* Generosity

---

# ⚙ ETL Pipeline

## 1️⃣ Extract

Population data is downloaded from the World Bank API.

The Happiness dataset is read from the CSV file.

Raw files are stored inside:

```
data/raw/
```

---

## 2️⃣ Transform

The transformation layer:

* Removes null values
* Removes duplicate records
* Selects latest population
* Standardizes columns
* Merges datasets
* Performs validation

Processed files are stored inside:

```
data/processed/
```

---

## 3️⃣ Load

The merged dataset is loaded into:

```
SQLite Database
```

and also saved as

```
Parquet
```

for analytics workloads.

---

# 📊 Analytics Dashboard

The Streamlit dashboard provides:

* Country Search
* Population Metrics
* Happiness Metrics
* GDP Metrics
* Life Expectancy
* Social Support
* Freedom Score
* Top Population Chart
* Top Happiness Chart
* GDP vs Happiness Chart
* Population vs Happiness Chart
* Data Quality Report
* Pipeline Health Report
* Automated Insights

---

# 🧹 Data Quality Checks

The project validates:

* Missing Values
* Duplicate Rows
* Merge Consistency
* Record Counts

---

# 🐳 Docker Support

The project is fully containerized.

Run using:

```
docker compose up
```

Docker automatically:

* Builds the image
* Creates container
* Installs dependencies
* Starts Streamlit
* Exposes port 8501

---

# ▶ Running Without Docker

## Step 1

Clone repository

```
git clone <YOUR_GITHUB_REPO>
```

---

## Step 2

Go inside project

```
cd world-insights-lakehouse
```

---

## Step 3

Create virtual environment

Windows

```
python -m venv venv
```

Activate

```
venv\Scripts\activate
```

---

## Step 4

Install dependencies

```
pip install -r requirements.txt
```

---

## Step 5

Run ETL Pipeline

```
python src/main.py
```

---

## Step 6

Start Dashboard

```
streamlit run dashboard/app.py
```

---

Open:

```
http://localhost:8501
```

---

# 🐳 Running With Docker

Clone project

```
git clone <YOUR_GITHUB_REPO>
```

```
cd world-insights-lakehouse
```

Run

```
docker compose up
```

Open

```
http://localhost:8501
```

---

# 📈 Technologies Used

* Python
* Pandas
* Requests
* SQLite
* SQLAlchemy
* Streamlit
* Docker
* Docker Compose
* Matplotlib
* PyArrow

---

# 📸 Dashboard Screenshots

## Home Dashboard

```
docs/dashboard_home.png
```

---

## Country Analytics

```
docs/country_view.png
```

---

## Pipeline Health

```
docs/pipeline_health.png
```

---

## Data Quality

```
docs/data_quality.png
```

---

# 📌 Future Improvements

* Cloud Deployment
* Airflow Scheduling
* MinIO Data Lake
* PostgreSQL Storage
* Power BI Integration
* Real-time Streaming Pipeline

---

# 👨‍💻 Author

Developed as part of the Azentrix Full Stack Data Engineering Internship Task.

This project demonstrates a complete end-to-end Data Lakehouse architecture with multi-source ingestion, transformation, storage, analytics, and dashboard visualization.
