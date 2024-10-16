import snowflake.connector
from config import SNOWFLAKE_CONN
import os

def load_to_snowflake(file_path):
    """
    Load the transformed data from CSV into Snowflake using the PUT command to stage the file, 
    and then merge the data into the final table using the SQL `MERGE` statement.
    """
    # Step 1: Connect to Snowflake
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_CONN['user'],
        password=SNOWFLAKE_CONN['password'],
        account=SNOWFLAKE_CONN['account'],
        warehouse=SNOWFLAKE_CONN['warehouse'],
        database=SNOWFLAKE_CONN['database'],
        schema=SNOWFLAKE_CONN['schema']
    )
    cursor = conn.cursor()

    # Step 2: Load the CSV file into Snowflake's staging area
    try:
        file_name = os.path.basename(file_path)
        put_command = f"PUT file://{file_path} @STAGE_PATH AUTO_COMPRESS=TRUE"
        cursor.execute(put_command)
        print(f"Successfully uploaded {file_name} to Snowflake stage.")
    except Exception as e:
        print(f"Failed to load file into Snowflake stage: {e}")
        raise

    # Step 3: Execute the MERGE statement to upsert data into the final Snowflake table
    try:
        with open('sql/merge_into_snowflake.sql', 'r') as merge_sql_file:
            merge_sql = merge_sql_file.read()

        cursor.execute(merge_sql)
        print("Data successfully merged into Snowflake table.")
    except Exception as e:
        print(f"Failed to execute MERGE statement: {e}")
        raise

    # Step 4: Close the cursor and connection
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    # Example usage (you would replace this with your actual transformed file path)
    load_to_snowflake('/tmp/transformed_data.csv')
