# ETL Example Project: OneDrive to Snowflake via Airflow

This is an example project an ETL pipeline that automates the extraction of .csv and JSON data files from OneDrive, transforms the data using `pandas`, and loads it into Snowflake for company stakeholders to access. The process is fully automated using Apache Airflow.

## Project Structure
- **config/**: Contains configuration files for Snowflake and OneDrive.
- **sql/**: SQL scripts for loading and upserting data into Snowflake.
- **scripts/**: Python scripts for extracting, transforming, and loading data.
- **dags/**: Airflow DAG to schedule the ETL process.
- **tests/**: Unit tests for the ETL workflow.

## How to Run the Project
1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Set up your environment variables for Snowflake and OneDrive credentials in `config/config.py`.
3. Run the ETL pipeline manually or let Airflow run the DAG.

# SQL Files
-**create_database_and_schema.sql**: Creates Snowflake database and schema.
-**create_tables.sql**: Defines tables such as donations and constituents.
-**manual_data_loading.sql**: Inserts sample data into Snowflake tables.
-**select_queries.sql**: Provides examples of queries for data analysis, including joins, groupings, and date ranges.
