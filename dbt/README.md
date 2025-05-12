# Bootcamp de DBT

O DBT é um framework para o desenvolvimento de pipelines de dados. Para mais detalhes sobre o curso, consulte o [Github](https://github.com/lvgalvao/dbt-core-northwind-project) do projeto original.

## Iniciando um novo ambiente de desenvolvimento:

1. Verificar quais versões do Python já estão instaladas no Pyenv: `pyenv versions`
2. Selecionar uma versão local para o ambiente: `pyenv local 3.12.1`
3. Inicializar o projeto com o UV: `uv init`
4. Criar o ambiente virtual com o UV: `uv venv`
5. Instalar o DBT: `uv add dbt`
6. Instalar o driver do banco de dados (Ex: PostgreSQL): `uv add psycopg2-binary`
7. Iniciar o DBT: `dbt init`
8. Verificar o status do DBT: `dbt debug`
