from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default argument configuration
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'flights_end_to_end_pipeline',
    default_args=default_args,
    description='Complete pipeline: Python Extract + Python Load + DBT Transform + Tests',
    schedule_interval = timedelta(minutes=30),
    catchup=False
) as dag:
    
    # 1. Python script execution (Extract and load)
    extract_and_load = BashOperator(
        task_id = 'python_extract_load',
        bash_command = 'export PYTHONPATH=$PYTHONPATH:/opt/airflow && python /opt/airflow/src/pipeline.py',
        dag=dag,
    )

    # 2. DBT transform (Staging and Marts)
    dbt_run = BashOperator(
        task_id = 'dbt_run',
        bash_command = 'cd /opt/airflow/flights_dbt && /home/airflow/.local/bin/dbt run'
    )

    # 3. Quality control (dbt tests)
    dbt_test = BashOperator(
        task_id = 'dbt_test',
        bash_command = 'cd /opt/airflow/flights_dbt && dbt test'
    )

    # Dependency definition (Pipelina DAG)
    extract_and_load >> dbt_run >> dbt_test