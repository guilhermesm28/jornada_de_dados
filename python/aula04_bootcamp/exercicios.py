def exercicio_1():

    # Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

    try:

        numeros: list = list(range(1, 11))

        for numero in numeros:
            print(f'{numero}² = {numero**2}')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_2():

    # Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

    try:

        lista: list = ['Python', 'Java', 'C++', 'JavaScript']

        print(f'Lista: {lista}')

        lista.remove('C++')

        print(f'Removendo C++: {lista}')

        lista.append('Ruby')

        print(f'Adicionando Ruby: {lista}')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_3():

    # Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação.
    # Imprima cada informação.

    try:

        livros: dict = {
            'Título' : 'Harry Potter',
            'Autor' : 'J.K. Rowling',
            'Ano' : 2002
        }

        for key, value in livros.items():
            print(f'{key}: {value}')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_4():

    # Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

    try:

        frase: str = input('Digite uma frase: ')
        contagem: dict = {}

        for caractere in frase:
            contagem[caractere] = contagem.get(caractere, 0) + 1

        print(contagem)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_5():

    # Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

    try:

        lista: list = ['maçã', 'banana', 'cereja']
        precos: dict = {'maçã': 0.45, 'banana': 0.30, 'cereja': 0.65}
        total: float = sum(precos[item] for item in lista)

        print(f'Preço total: {total}')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_6():

    # Dada uma lista de emails, remover todos os duplicados.

    try:

        emails: list = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
        emails_unicos: list = list(set(emails))

        print(emails_unicos)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_7():

    # Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

    try:

        idades: list = [22, 15, 30, 17, 18]
        idades_validas: list = [idade for idade in idades if idade >= 18]

        print(idades_validas)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_8():

    # Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

    try:

        pessoas: list = [
            {'nome': 'Bob', 'idade': 25},
            {'nome': 'Carol', 'idade': 20},
            {'nome': 'Alice', 'idade': 30}
        ]

        pessoas.sort(key=lambda pessoa: pessoa['nome'])

        print(pessoas)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_9():

    # Dado um conjunto de números, calcular a média.

    try:

        numeros: list = [10, 20, 30, 40, 50]
        media: float = sum(numeros) / len(numeros)

        print(f'Média: {media}')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_10():

    # Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

    try:

        valores: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        pares: list = [valor for valor in valores if valor % 2 == 0]
        impares: list = [valor for valor in valores if valor % 2 != 0]

        print(f'Pares: {pares}')
        print(f'Ímpares: {impares}')

    except Exception as e:
        print(f'')

def exercicio_11():

    # Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

    try:

        produtos: list = [
            {'id': 1, 'nome': 'Teclado', 'preço': 100},
            {'id': 2, 'nome': 'Mouse', 'preço': 80},
            {'id': 3, 'nome': 'Monitor', 'preço': 300}
        ]

        # Atualizar o preço do produto com id 2 para 90
        for produto in produtos:
            if produto['id'] == 2:
                produto['preço'] = 90

        print(produtos)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_12():

    # Dados dois dicionários, fundi-los em um único dicionário.

    try:

        dicionario1: dict = {"a": 1, "b": 2}
        dicionario2: dict = {"c": 3, "d": 4}

        dicionario_fundido: dict = {**dicionario1, **dicionario2}

        print(dicionario_fundido)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_13():

    # Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

    try:

        estoque: dict = {'Teclado': 10, 'Mouse': 0, 'Monitor': 3, 'CPU': 0}

        estoque_positivo: dict = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

        print(estoque_positivo)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_14():

    # Dado um dicionário, criar listas separadas para suas chaves e valores.

    try:

        dicionario: dict = {'a': 1, 'b': 2, 'c': 3}
        chaves: list = list(dicionario.keys())
        valores: list = list(dicionario.values())

        print(f'Chaves: {chaves}')
        print(f'Valores: {valores}')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_15():

    # Dada uma string, contar a frequência de cada caractere usando um dicionário.

    try:

        texto: str = input('Digite um texto qualquer: ').strip()
        frequencia: dict = {}

        for caractere in texto:
            if caractere in frequencia:
                frequencia[caractere] += 1
            else:
                frequencia[caractere] = 1

        print(frequencia)

    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    exercicio_15()