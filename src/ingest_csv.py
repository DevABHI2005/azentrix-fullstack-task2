import pandas as pd


def ingest_csv():

    print("Reading CSV dataset...")

    file_path = "data/raw/csv/WHR2024.csv"

    df = pd.read_csv(file_path)

    # Rename column for merging
    df.rename(
        columns={
            "Country name": "country"
        },
        inplace=True
    )

    print(df.head())

    print(f"CSV Loaded Successfully! Rows: {len(df)}")

    return df


if __name__ == "__main__":
    ingest_csv()