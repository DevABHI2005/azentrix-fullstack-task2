import pandas as pd
from datetime import datetime


def transform_data(api_df):

    print("Starting Transformation Layer...")

    # Read Happiness CSV
    csv_df = pd.read_csv("data/raw/csv/WHR2024.csv")

    # Rename column for merging
    csv_df.rename(
        columns={
            "Country name": "country"
        },
        inplace=True
    )

    # Remove missing population values
    api_df = api_df.dropna(subset=["population"])

    # Convert datatypes
    api_df["population"] = api_df["population"].astype(int)
    api_df["year"] = api_df["year"].astype(int)

    # Sort by latest year
    api_df = api_df.sort_values(
        by="year",
        ascending=False
    )

    # Keep latest record for each country
    api_df = api_df.drop_duplicates(
        subset=["country"],
        keep="first"
    )

    # Remove regional aggregates
    aggregates = [
        "Africa Eastern and Southern",
        "Africa Western and Central",
        "Arab World",
        "Caribbean small states",
        "Central Europe and the Baltics",
        "Early-demographic dividend",
        "East Asia & Pacific",
        "East Asia & Pacific (excluding high income)"
    ]

    api_df = api_df[
        ~api_df["country"].isin(aggregates)
    ]

    print("Rows after latest selection:", len(api_df))

    # -----------------------
    # DEBUGGING
    # -----------------------

    api_countries = set(api_df["country"])
    csv_countries = set(csv_df["country"])

    print("API countries:", len(api_countries))
    print("CSV countries:", len(csv_countries))

    print("\nMissing from API:")
    print(sorted(csv_countries - api_countries))

    print("\nMissing from CSV:")
    print(sorted(api_countries - csv_countries))

    # -----------------------
    # Merge
    # -----------------------

    merged_df = pd.merge(
        api_df,
        csv_df,
        on="country",
        how="inner"
    )

    print("\nMerged Rows:", len(merged_df))

    merged_df = merged_df.drop_duplicates()

    merged_df.reset_index(
        drop=True,
        inplace=True
    )

    # Save processed file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_path = (
        f"data/processed/merged_dataset_{timestamp}.csv"
    )

    merged_df.to_csv(
        output_path,
        index=False
    )

    print(
        f"Merged dataset saved to {output_path}"
    )

    return merged_df