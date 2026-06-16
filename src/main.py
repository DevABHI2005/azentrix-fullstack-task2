from ingest_api import extract_data
from transform import transform_data
from load import load_data
from logger import logger


def run_pipeline():

    try:
        logger.info("Pipeline Started")

        # Extract
        raw_df = extract_data()

        # Transform
        processed_df = transform_data(raw_df)

        row_count = len(processed_df)

        # Load
        load_data(processed_df)

        logger.info(
            f"Pipeline Success | Rows Loaded: {row_count}"
        )

        print("ETL Pipeline Completed Successfully!")


        

    except Exception as e:

        import traceback

        print("\n========================")
        print("FULL ERROR")
        print("========================")

        traceback.print_exc()

        print("\nPipeline Failed")


if __name__ == "__main__":
    run_pipeline()