from etl import pipeline_calcular_kpi_consolidado

pasta_argumento: str = "data"
formato_saida: list = ["csv", "parquet"]

pipeline_calcular_kpi_consolidado(pasta_argumento, formato_saida)
