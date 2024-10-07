from etl import (
    filtrar_produtos_entregues,
    filtrar_produtos_nao_entregues,
    ler_csv,
    somar_valores,
)

nome_arquivo: str = "vendas.csv"

csv = ler_csv(nome_arquivo)

print(f"Lista de produtos: \n{csv}")

entregues = filtrar_produtos_entregues(csv)

print(f"Produtos entregues: \n{entregues}")

nao_entregues = filtrar_produtos_nao_entregues(csv)

print(f"Produtos não entregues: \n{nao_entregues}")

soma_entregues = somar_valores(entregues)

print(f"Soma dos produtos entregues: R$ {soma_entregues:.2f}")

soma_nao_entregues = somar_valores(nao_entregues)

print(f"Soma dos produtos não entregues: R$ {soma_nao_entregues:.2f}")
