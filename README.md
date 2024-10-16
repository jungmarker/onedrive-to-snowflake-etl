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
