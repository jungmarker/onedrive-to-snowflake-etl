import pandas as pd

def transform_csv_data(file_path):
    # Load the CSV file into pandas DataFrame
    df = pd.read_csv(file_path)
    
    # Data cleaning and transformations
    df.drop_duplicates(subset=['external_id'], inplace=True)
    df['donation_date'] = pd.to_datetime(df['donation_date'])
    
    # Save the transformed data to CSV
    transformed_file_path = '/tmp/transformed_data.csv'
    df.to_csv(transformed_file_path, index=False)
    
    return transformed_file_path
