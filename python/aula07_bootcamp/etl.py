import csv


def ler_csv(nome_arquivo: str) -> list[dict]:
    """
    Função que lê um arquivo CSV e retorna uma lista de dicionários
    """
    try:
        lista: list = []
        with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                lista.append(linha)

        return lista
    except Exception as e:
        return f"Erro: {e}"


def filtrar_produtos_entregues(lista_produtos: list[dict]) -> list[dict]:
    """
    Função que filtra produtos que foram entregues
    """
    try:
        lista_filtrados: list = []
        for produto in lista_produtos:
            if produto.get("entregue") == "True":
                lista_filtrados.append(produto)

        return lista_filtrados
    except Exception as e:
        return f"Erro: {e}"


def filtrar_produtos_nao_entregues(lista_produtos: list[dict]) -> list[dict]:
    """
    Função que filtra produtos que não foram entregues
    """
    try:
        lista_filtrados: list = []
        for produto in lista_produtos:
            if produto.get("entregue") == "False":
                lista_filtrados.append(produto)

        return lista_filtrados
    except Exception as e:
        return f"Erro: {e}"


def somar_valores(lista_produtos: list[dict]) -> float:
    """
    Função que soma os valores dos produtos
    """
    try:
        valor_total: float = 0
        for produto in lista_produtos:
            valor_total += float(produto.get("price"))

        return valor_total
    except Exception as e:
        return f"Erro: {e}"
