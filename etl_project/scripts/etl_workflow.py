from scripts.extract_onedrive_data import download_file_from_onedrive
from scripts.transform_csv_data import transform_csv_data
from scripts.transform_json_data import transform_json_data
from scripts.load_to_snowflake import load_to_snowflake

def etl_workflow(file_name):
    """ETL workflow"""
    file_path, file_extension = download_file_from_onedrive(file_name)

    # Choose the appropriate transformation function based on the file type
    if file_extension == 'csv':
        transformed_file_path = transform_csv_data(file_path)
    elif file_extension == 'json':
        transformed_file_path = transform_json_data(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

    # Load the transformed data into Snowflake
    load_to_snowflake(transformed_file_path)

if __name__ == "__main__":
    etl_workflow('donations.csv')  # Replace with 'donations.json' for JSON
