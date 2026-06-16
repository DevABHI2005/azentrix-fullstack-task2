import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_URL = os.getenv("API_URL")


def extract_data():

    print("Starting data extraction...")

    all_records = []

    page = 1

    while True:

        url = f"{API_URL}&page={page}"

        response = requests.get(url)

        if response.status_code != 200:
            raise Exception("API request failed")

        data = response.json()

        metadata = data[0]

        records = data[1]

        if not records:
            break

        print(f"Reading Page {page}...")

        for item in records:

            all_records.append({

                "country": item["country"]["value"],

                "country_id": item["country"]["id"],

                "year": item["date"],

                "population": item["value"]

            })

        if page >= metadata["pages"]:
            break

        page += 1

    df = pd.DataFrame(all_records)

    print(df.shape)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    raw_file_path = f"data/raw/api/raw_population_{timestamp}.csv"

    df.to_csv(raw_file_path, index=False)

    print(f"Raw data saved at: {raw_file_path}")

    return df


if __name__ == "__main__":
    extract_data()