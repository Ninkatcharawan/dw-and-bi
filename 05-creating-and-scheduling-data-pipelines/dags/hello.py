from airflow import DAG
from airflow.utils import timezone
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator

def _say_hello():
    print("hello")

with DAG(
    "hello",
    start_date=timezone.datetime(2024, 3, 23),
    schedule=None,
    tags=["DS525"],
):

    start = EmptyOperator(task_id"start")

    echo_hello = BashOperator(
        task_id = "echo_hello",
        bash_command="echon 'hello'",
    )

    say_hello = PythonOperator(
        task_id="say_hello",
        python_callable=_say_hello
    )
    
    end = EmptyOperator(task_id="end")

    start >> end_hello >> end
    start >> say_hello >> end