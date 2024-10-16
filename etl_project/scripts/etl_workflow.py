from scripts.extract_onedrive_data import download_file_from_onedrive
from scripts.transform_csv_data import transform_csv_data
from scripts.transform_json_data import transform_json_data
from scripts.load_to_snowflake import load_to_snowflake

def etl_workflow(file_name):
    # Step 1: Extract from OneDrive
    file_path, file_extension = download_file_from_onedrive(file_name)

    # Step 2: Transform the data based on file type
    if file_extension == 'csv':
        transformed_file_path = transform_csv_data(file_path)
    elif file_extension == 'json':
        transformed_file_path = transform_json_data(file_path)
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

    # Step 3: Load into Snowflake
    load_to_snowflake(transformed_file_path)

if __name__ == "__main__":
    # Example of running with a CSV file
    etl_workflow('donations.csv')
    
    # Example of running with a JSON file
    # etl_workflow('donations.json')
