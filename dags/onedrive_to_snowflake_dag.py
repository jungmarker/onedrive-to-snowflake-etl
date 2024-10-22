from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from etl_project.config import ONEDRIVE
from scripts.etl_workflow import etl_workflow



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'onedrive_to_snowflake_etl',
    default_args=default_args,
    description='ETL pipeline to extract CSV and JSON from OneDrive and load into Snowflake',
    schedule_interval='@daily',
)

etl_csv_task = PythonOperator(
    task_id='run_etl_csv',
    python_callable=etl_workflow, 
    op_args=['donations.csv'],
    dag=dag
)

etl_json_task = PythonOperator(
    task_id='run_etl_json',
    python_callable=etl_workflow,
    op_args=['donations.json'],
    dag=dag
)

etl_csv_task >> etl_json_task
