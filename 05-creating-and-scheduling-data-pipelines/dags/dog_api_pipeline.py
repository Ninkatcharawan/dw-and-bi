from airflow import DAG
from airflow.utils import timezone
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

import requests
import json

def get_dog_api():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    logging.info(data)
    with open("/opt/airflow/dags/dog.json", "w") as f:
        json.dump(data, f)


with DAG(
    "dog_api_pipeline",
    start_date=timezone.datetime(2024, 3, 23),
    schedule="@daily", # Cron expression
    tags=["DS525"],
):

    start = EmptyOperator(task_id"start")

    get_dog_api = BashOperator(
        task_id = "echo_hello",
        bash_command="echon 'hello'",
    )

    read_data =PythonOperator(
        task_id="read_"
    )

    end = EmptyOperation(task_id="end")

    start >> get_dog_api >> end