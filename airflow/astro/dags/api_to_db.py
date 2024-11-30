from datetime import datetime

from include.controller import (
    add_pokemon_to_db,
    fetch_pokemon_data,
    gerar_numero_aleatorio,
)

from airflow.decorators import dag, task


@dag(
    dag_id="api_db",
    description="Pipeline para capturar Pokemon",
    start_date=datetime(2024, 1, 29),
    schedule="* * * * *",
    catchup=False,
)
def api_db():

    @task(task_id="gerar_numero_aleatorio")
    def task_gerar_numero_aleatorio():
        return gerar_numero_aleatorio()

    @task(task_id="fetch_pokemon_data")
    def task_fetch_pokemon_data(numero_aleatorio):
        return fetch_pokemon_data(numero_aleatorio)

    @task(task_id="add_pokemon_to_db")
    def task_add_pokemon_to_db(pokemon_data):
        add_pokemon_to_db(pokemon_data)

    @task
    def print_de_sucesso(response):
        print(response)

    t1 = task_gerar_numero_aleatorio()
    t2 = task_fetch_pokemon_data(t1)
    t3 = task_add_pokemon_to_db(t2)
    t4 = print_de_sucesso(t3)

    t1 >> t2 >> t3 >> t4


api_db()
