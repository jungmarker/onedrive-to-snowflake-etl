import pandas as pd
import json

def transform_json_data(file_path):
    # Load the JSON file
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Convert JSON data to pandas DataFrame
    df = pd.DataFrame(data)
    
    # Data cleaning and transformations
    df.drop_duplicates(subset=['external_id'], inplace=True)
    df['donation_date'] = pd.to_datetime(df['donation_date'])
    
    # Save the transformed data to CSV
    transformed_file_path = '/tmp/transformed_data.csv'
    df.to_csv(transformed_file_path, index=False)
    
    return transformed_file_path
