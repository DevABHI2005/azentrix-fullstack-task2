from sqlalchemy import create_engine
from datetime import datetime
import os


def load_data(df):

    print("Starting data loading...")

    # SQLite
    engine = create_engine(
        "sqlite:///database/population.db"
    )

    df.to_sql(
        "country_analytics",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into SQLite database.")

    # Ensure folder exists
    os.makedirs("data/parquet", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    parquet_path = (
        f"data/parquet/country_analytics_{timestamp}.parquet"
    )

    df.to_parquet(
        parquet_path,
        index=False
    )

    print(f"Parquet file saved at {parquet_path}")