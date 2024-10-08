import glob
import os

import pandas as pd

from utils_log import log_decorator


@log_decorator
def extrair_dados_e_concatenar(pasta: str) -> pd.DataFrame:
    """
    Função responsável por extrair e concatenar os dados JSON
    """
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


@log_decorator
def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Função responsável por criar a nova coluna 'Total' no DataFrame
    """
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


@log_decorator
def salvar_arquivo(df: pd.DataFrame, formato_arquivo: list):
    """
    Função responsável por salvar um arquivo CSV e/ou Parquet
    """
    for formato in formato_arquivo:
        if formato == "csv":
            df.to_csv("dados.csv", index=False)
        if formato == "parquet":
            df.to_parquet("dados.parquet")


@log_decorator
def pipeline_calcular_kpi_consolidado(pasta: str, formato_saida: list):
    df = extrair_dados_e_concatenar(pasta)
    df_calculado = calcular_kpi_total_vendas(df)
    salvar_arquivo(df_calculado, formato_saida)
