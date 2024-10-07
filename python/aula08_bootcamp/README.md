# Aula 08 - Bootcamp de Python

Tópicos de estudo da aula:
- Funções em Python
- ETL com Pandas, JSON e Parquet

O desafio é criar um ETL. Como etapa inicial antes mesmo de começar o desenvolvimento do ETL, é preciso definir qual ferramentas iremos utilizar:

1. Ferramenta de processamento (Pandas, Polars, DuckDB, Spark, Dask)
2. Ferramenta de qualidade (Pydantic, Pandera)

Esse ETL terá a seguinte estrutura:

1. Arquivo com as lógicas de negócio: `etl.py`
2. Arquivo que será executado futuramente no Airflow, por exemplo: `pipeline.py`
3. Arquivo de qualidade que conterá a validação do DataFrame: `schema.py`
4. Pasta para conter os arquivos: `data`

## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula08) do Luciano.
