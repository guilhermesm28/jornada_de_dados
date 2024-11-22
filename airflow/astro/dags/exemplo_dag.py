from datetime import datetime
from time import sleep

from airflow.decorators import dag, task


@dag(
    dag_id="minha_primeira_dag",
    description="Minha primeira DAG",
    schedule="* * * * *",
    start_date=datetime(2024, 11, 21),
    catchup=False,  # para não executar as tarefas anteriores (backfill)
)
def pipeline():

    @task
    def primeira_atividade():
        print("Primeira atividade iniciada...")
        sleep(2)
        print("Primeira atividade finalizada!")

    @task
    def segunda_atividade():
        print("Segunda atividade iniciada...")
        sleep(2)
        print("Segunda atividade finalizada!")

    @task
    def terceira_atividade():
        print("Terceira atividade iniciada...")
        sleep(2)
        print("Terceira atividade finalizada!")

    t1 = primeira_atividade()
    t2 = segunda_atividade()
    t3 = terceira_atividade()

    t1 >> t2 >> t3


pipeline()
