from airflow import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime
from airflow.decorators import dag

default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 2, 6),
    "retries": 1,
}


@dag(
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    description="A simple DAG",
)
def simple_dag():
    start = DummyOperator(task_id="start")
    end = DummyOperator(task_id="end")

    start >> end


dag = simple_dag()
