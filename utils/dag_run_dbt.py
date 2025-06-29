from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# Configuração padrão da DAG
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Criando a DAG
dag = DAG(
    "run_dbt_transformed_stock_data",
    default_args=default_args,
    description="Runs dbt model transformed_stock_data.sql",
    schedule_interval="0 11 * * *",  # Roda todo dia às 11:00 UTC
    catchup=False,
)

# Comando para rodar o dbt
run_dbt = BashOperator(
    task_id="run_dbt_model",
    bash_command="cd C:/Users/alexs/OneDrive/Documentos/DBT && dbt run --select transformed_stock_data",
    dag=dag,
)


run_dbt
