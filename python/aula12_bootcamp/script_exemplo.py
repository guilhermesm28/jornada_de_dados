import pandas as pd
from src.interface.classes.csv_class import CsvProcessor

caminho_csv = "./data/exemplo.csv"

# análise sem o uso de POO (classes)

df = pd.read_csv(caminho_csv)
df_filtrado = df[df["estado"] == "SP"]
df_filtrado = df[df["preco"] == "10,50"]
print(f"\nCSV filtrado sem uso de POO: \n{df_filtrado}")

# análise com o uso de POO (classes)

arquivo_csv = CsvProcessor(caminho_csv)
arquivo_csv.carregar_csv()
print(
    f"\nCSV filtrado com uso de POO: \n{arquivo_csv.filtrar_por(['estado', 'preco'], ['SP', '10,50'])}"
)
