from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone

with DAG(
    "my_first_dag", #dag id need to edit when created new file
    start_date=timezone.datetime(2024, 3, 23),
    schedule=None,
    tags=["DS525"],

):
    my_first_task = EmptyOperator(task_id="my_first_task")
    my_second_task = EmptyOperator(task_id="my_second_task")

    my_first_task >> my_second_task #รันอันแรกก่อน ค่อยรันอันที่ 2