import sqlite3
import pandas as pd


DATABASE = "database/population.db"


def run_query(query):
    conn = sqlite3.connect(DATABASE)

    df = pd.read_sql_query(query, conn)

    conn.close()

    return df


# -----------------------------
# Query 1
# Top 10 Happiest Countries
# -----------------------------

def top_happiest():

    query = """
    SELECT country,
           "Ladder score"
    FROM country_analytics
    ORDER BY "Ladder score" DESC
    LIMIT 10
    """

    return run_query(query)


# -----------------------------
# Query 2
# Top 10 Populated Countries
# -----------------------------

def top_population():

    query = """
    SELECT country,
           population
    FROM country_analytics
    ORDER BY population DESC
    LIMIT 10
    """

    return run_query(query)


# -----------------------------
# Query 3
# Average Happiness
# -----------------------------

def average_happiness():

    query = """
    SELECT AVG("Ladder score") AS avg_happiness
    FROM country_analytics
    """

    return run_query(query)


# -----------------------------
# Query 4
# Highest GDP Countries
# -----------------------------

def top_gdp():

    query = """
    SELECT country,
           "Explained by: Log GDP per capita"
    FROM country_analytics
    ORDER BY "Explained by: Log GDP per capita" DESC
    LIMIT 10
    """

    return run_query(query)


# -----------------------------
# Query 5
# Highest Life Expectancy
# -----------------------------

def top_life_expectancy():

    query = """
    SELECT country,
           "Explained by: Healthy life expectancy"
    FROM country_analytics
    ORDER BY "Explained by: Healthy life expectancy" DESC
    LIMIT 10
    """

    return run_query(query)
def generate_insights():

    print("\n========== INSIGHTS ==========\n")

    print("Highest Happiness Country:")
    print(top_happiest().iloc[0])

    print()

    print("Highest Population Country:")
    print(top_population().iloc[0])

    print()

    print("Average Happiness:")
    print(average_happiness())




# -----------------------------
# Test
# -----------------------------

if __name__ == "__main__":

    print(top_happiest())

    print(top_population())

    print(average_happiness())

    print(top_gdp())

    print(top_life_expectancy())

    generate_insights()