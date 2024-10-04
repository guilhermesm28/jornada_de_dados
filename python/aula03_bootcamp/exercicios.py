def exercicio_1():

    # Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço.
    # Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

    try:

        quantidade = float(input('Digite a quantidade de um produto: '))
        preco = float(input('Digite o preço de um produto: '))

        if quantidade > 0 and preco > 0:
            print('Dados válidos!')
        else:
            print('Dados inválidos!')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_2():

    # Imagine que você está trabalhando com dados de sensores IoT.
    # Os dados incluem medições de temperatura.
    # Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'.
    # Considerando que:
    # Temperatura < 18°C é 'Baixa'
    # Temperatura >= 18°C e <= 26°C é 'Normal'
    # Temperatura > 26°C é 'Alta'

    try:

        temperatura = int(input('Digite uma temperatura: '))

        if temperatura < 18:
            print(f'{temperatura}° - Temperatura baixa')
        elif temperatura >= 18 and temperatura <=  26:
            print(f'{temperatura}° - Temperatura normal')
        else:
            print(f'{temperatura}° - Temperatura alta')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_3():

    # Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'.
    # Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

    try:

        log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

        if log['level'] == 'ERROR':
            print(log['message'])

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_4():

    # Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido.
    # Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

    try:

        idade = int(input('Digite sua idade: '))
        email = input('Digite seu e-mail: ')

        if not 18 <= idade <= 65:
            print('Idade fora do intervalo permitido')
        elif '@' not in email or '.' not in email:
            print('Email inválido')
        else:
            print('Dados de usuário válidos')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_5():

    # Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas.
    # Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
    # Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

    try:

        transacao = {'valor': 12000, 'hora': 20}

        if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
            print('Transação suspeita')
        else:
            print('Transação normal')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_6():

    # Dado um texto, contar quantas vezes cada palavra única aparece nele.

    try:

        texto = input('Digite um texto qualquer: ')
        palavras = texto.split()
        contagem_palavras = {}

        for palavra in palavras:
            if palavra in contagem_palavras:
                contagem_palavras[palavra] += 1
            else:
                contagem_palavras[palavra] = 1

        print(f'Total de palavras no seu texto: {contagem_palavras}')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_7():

    # Normalizar uma lista de números para que fiquem na escala de 0 a 1.

    try:

        numeros = [10, 20, 30, 40, 50]
        minimo = min(numeros)
        maximo = max(numeros)
        normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

        print(normalizados)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_8():

    # Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

    try:

        usuarios = [
            {"nome": "Alice", "email": "alice@example.com"},
            {"nome": "Bob", "email": ""},
            {"nome": "Carol", "email": "carol@example.com"}
        ]

        usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

        print(usuarios_validos)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_9():

    # Dada uma lista de números, extrair apenas aqueles que são pares.

    try:

        numeros = range(1, 11)
        pares = [x for x in numeros if x % 2 == 0]

        print(pares)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_10():

    # Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

    try:

        vendas = [
            {"categoria": "eletrônicos", "valor": 1200},
            {"categoria": "livros", "valor": 200},
            {"categoria": "eletrônicos", "valor": 800}
        ]

        total_por_categoria = {}

        for venda in vendas:
            categoria = venda["categoria"]
            valor = venda["valor"]
            if categoria in total_por_categoria:
                total_por_categoria[categoria] += valor
            else:
                total_por_categoria[categoria] = valor

        print(total_por_categoria)

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_11():

    # Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

    try:

        entrada = ''

        while entrada.lower() != "sair":
            entrada = input("Digite um valor (ou 'sair' para terminar): ")

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_12():

    # Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

    try:

        numero = int(input('Digite um número entre 1 e 10: '))

        while not 1 <= numero <= 10:
            print('Número fora do intervalo!')
            numero = int(input('Por favor, digite um número entre 1 e 10: '))

        print('Número válido!')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_13():

    # Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas

    try:

        pagina_atual = 1
        paginas_totais = int(input('Digite o total de páginas para simular: ')) # Simulação, na prática, isso viria da API

        while pagina_atual <= paginas_totais:
            print(f'Processando página {pagina_atual} de {paginas_totais}')
            pagina_atual += 1

        print('Todas as páginas foram processadas.')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_14():

    # Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

    try:

        tentativas_maximas = 5
        tentativa = 1

        while tentativa <= tentativas_maximas:
            print(f'Tentativa {tentativa} de {tentativas_maximas}')

            if tentativa == 5: # Suponha que a conexão foi bem-sucedida
                print('Conexão bem-sucedida!')
                break
            tentativa += 1
        else:
            print('Falha ao conectar após várias tentativas.')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_15():

    # Processar itens de uma lista até encontrar um valor específico que indica a parada.

    try:

        itens = [1, 2, 3, 'parar', 4, 5]

        i = 0

        while i < len(itens):
            if itens[i] == 'parar':
                print('Encerrando o processamento.')
                break
            print(f'Processando item: {itens[i]}')
            i += 1

    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    exercicio_15()