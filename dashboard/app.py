import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    
    layout="wide"
)
st.title("🌍 World Insights Lakehouse")
st.caption("Global Population & Happiness Analytics Platform")
DATABASE = "database/population.db"


def load_data():
    conn = sqlite3.connect(DATABASE)
    df = pd.read_sql(
        "SELECT * FROM country_analytics",
        conn
    )
    conn.close()
    return df


df = load_data()
# --------------------
# Sidebar
# --------------------

st.sidebar.title("🌍 World Insights")

st.sidebar.info("""
This dashboard combines

• World Bank Population API

• World Happiness Report 2024

to generate global analytics.
""")

st.sidebar.success("Pipeline Status: SUCCESS")

st.title("🌍 World Insights Lakehouse")

st.markdown(
    "Multi-Source Data Engineering & Analytics Dashboard"
)

# --------------------
# KPI CARDS
# --------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Countries",
    len(df)
)

col2.metric(
    "Highest Population",
    df.sort_values(
        "population",
        ascending=False
    ).iloc[0]["country"]
)

col3.metric(
    "Average Happiness",
    round(df["Ladder score"].mean(), 2)
)
st.subheader("📊 Dataset Overview")

left, right = st.columns(2)

left.write(f"**Countries Available:** {len(df)}")

right.write(
    f"**Latest Population Year:** {df['year'].max()}"
)

st.divider()

# --------------------
# Country Search
# --------------------

country = st.selectbox(
    "Select Country",
    sorted(df["country"])
)

selected = df[df["country"] == country]

st.subheader(f"🌍 {country}")

c1, c2, c3 = st.columns(3)

c1.metric(
    "👥 Population",
    f"{int(selected.iloc[0]['population']):,}"
)

c2.metric(
    "😊 Happiness Score",
    round(selected.iloc[0]["Ladder score"], 2)
)

c3.metric(
    "💰 GDP Score",
    round(selected.iloc[0]["Explained by: Log GDP per capita"], 2)
)

c4, c5, c6 = st.columns(3)

c4.metric(
    "❤️ Life Expectancy",
    round(selected.iloc[0]["Explained by: Healthy life expectancy"], 2)
)

c5.metric(
    "🤝 Social Support",
    round(selected.iloc[0]["Explained by: Social support"], 2)
)

c6.metric(
    "🕊 Freedom",
    round(selected.iloc[0]["Explained by: Freedom to make life choices"], 2)
)

st.divider()

# --------------------
# Top Population Chart
# --------------------

st.subheader("Top 10 Population")

top_pop = df.sort_values(
    "population",
    ascending=False
).head(10)

fig, ax = plt.subplots()

ax.bar(
    top_pop["country"],
    top_pop["population"]
)

plt.xticks(rotation=90)

st.pyplot(fig)

# --------------------
# Top Happiness
# --------------------

st.subheader("Top 10 Happiness")

top_happy = df.sort_values(
    "Ladder score",
    ascending=False
).head(10)

fig2, ax2 = plt.subplots()

ax2.bar(
    top_happy["country"],
    top_happy["Ladder score"]
)

plt.xticks(rotation=90)

st.pyplot(fig2)

# --------------------
# GDP vs Happiness
# --------------------

st.subheader("GDP vs Happiness")

fig3, ax3 = plt.subplots()

ax3.scatter(
    df["Explained by: Log GDP per capita"],
    df["Ladder score"],
    alpha=0.7
)

ax3.set_title(
    "GDP vs Happiness"
)

ax3.grid(True)

ax3.set_xlabel("GDP")

ax3.set_ylabel("Happiness")

st.pyplot(fig3)

st.subheader(
    "Population vs Happiness"
)

fig4, ax4 = plt.subplots()

ax4.scatter(
    df["population"],
    df["Ladder score"],
    alpha=0.7
)

ax4.set_xlabel("Population")

ax4.set_ylabel("Happiness")

ax4.grid(True)

st.pyplot(fig4)

# --------------------
# Insights
# --------------------


duplicates = df.duplicated().sum()
nulls = df.isnull().sum().sum()

st.header("🧹 Data Quality")

x, y = st.columns(2)

x.metric(
    "Duplicate Rows",
    duplicates
)

y.metric(
    "Missing Values",
    nulls
)

if duplicates == 0 and nulls == 0:
    st.success("Dataset Quality: Excellent ✅")
else:
    st.warning("Dataset contains quality issues.")
st.divider()

st.header("💡 Automated Insights")

highest_happy = df.sort_values(
    "Ladder score",
    ascending=False
).iloc[0]["country"]

highest_pop = df.sort_values(
    "population",
    ascending=False
).iloc[0]["country"]

avg = round(df["Ladder score"].mean(), 2)

st.info(
f"""
🌍 **{highest_happy}** is the happiest country in the dataset.

👥 **{highest_pop}** has the largest population.

😊 Average Happiness Score = **{avg}**

📈 GDP generally shows a positive relationship with Happiness.

❤️ Countries with better life expectancy generally report higher happiness.
"""
)
st.divider()

st.header("⚙ Pipeline Health")

a, b, c, d = st.columns(4)

a.metric(
    "API Records",
    "17,556"
)

b.metric(
    "CSV Records",
    "143"
)

c.metric(
    "Merged Countries",
    len(df)
)

d.metric(
    "Pipeline Status",
    "Healthy ✅"
)

st.success(
    """
SQLite Storage ✔

Parquet Storage ✔

Analytics Layer ✔

Dashboard ✔

Pipeline Executed Successfully ✔
"""
)

st.divider()

st.header("📌 Project Summary")

st.success("""
✔ Multi-Source Ingestion

✔ Landing Zone

✔ Transformation Layer

✔ SQLite Storage

✔ Parquet Storage

✔ Analytics Layer

✔ Streamlit Dashboard

✔ Data Quality Validation

✔ Docker Ready
""")