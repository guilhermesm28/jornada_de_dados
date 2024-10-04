def exercicio_1():

    # Escreva um programa que soma dois números inteiros inseridos pelo usuário.

    num1 = int(input('Digite um número (int): '))
    num2 = int(input('Digite outro número (int): '))
    soma = num1 + num2

    print(f'{num1} + {num2} = {soma}')

def exercicio_2():

    # Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

    numero = int(input('Digite um número: '))
    result = numero % 5

    print(f'O resto da divisão de {numero} por 5 é {result}')

def exercicio_3():

    # Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    result = num1 * num2

    print(f'{num1} x {num2} = {result}')

def exercicio_4():

    # Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    result = int(num1 / num2)

    print(f'{num1} / {num2} = {result}')

def exercicio_5():

    # Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

    num1 = int(input('Digite um número: '))
    result = num1 ** 2

    print(f'{num1}² = {result}')

def exercicio_6():

    # Escreva um programa que receba dois números flutuantes e realize sua adição.

    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    result = num1 + num2

    print(f'{num1} + {num2} = {result}')

def exercicio_7():

    # Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite outro número: '))
    result = (num1 + num2) / 2

    print(f'A média entre {num1} e {num2} é {result}')

def exercicio_8():

    # Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

    base = float(input('Digite a base: '))
    expoente = float(input('Digite o expoente: '))
    result = base ** expoente

    print(f'O resultado da potência de base {base} e expoente {expoente} é {result}')

def exercicio_9():

    # Faça um programa que converta a temperatura de Celsius para Fahrenheit.

    celsius = float(input('Digite a temperatura (em Celsius): '))
    fahrenheit = (celsius * 9/5) + 32

    print(f'{celsius}°C é igual a {fahrenheit}°F')

def exercicio_10():

    # Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

    raio = float(input('Digite o raio de um círculo: '))
    area = (3.14159 * raio) ** 2

    print(f'A área do círculo é {area}')

def exercicio_11():

    # Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

    texto = input('Digite um texto qualquer: ')
    result = texto.upper()

    print(f'Seu texto: {texto} \nSeu texto maiúsculo: {result}')

def exercicio_12():

    # Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

    texto = input('Digite seu nome completo: ')
    result = texto.lower()

    print(f'Seu nome: {texto} \nSeu nome minúsculo: {result}')

def exercicio_13():

    # Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

    texto = input('Digite uma frase com espaços no início e fim: ')
    result = texto.strip()

    print(f'Seu texto: {texto} \nSeu texto sem espaços no início e fim: {result}')

def exercicio_14():

    # Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

    texto = input('Digite uma data no formato "dd/mm/aaaa": ')
    # dia = texto.split('/')[0]
    # mes = texto.split('/')[1]
    # ano = texto.split('/')[2]
    dia, mes, ano = texto.split('/')

    print(f'Dia: {dia} \nMês: {mes} \nAno: {ano}')

def exercicio_15():

    # Escreva um programa que concatene duas strings fornecidas pelo usuário.

    texto1 = input('Digite seu primeiro nome: ')
    texto2 = input('Digite seu sobrenome: ')
    nome_completo = texto1 + ' ' + texto2

    print(f'Seu nome completo é "{nome_completo}"')

def exercicio_16():

    # Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

    valor1 = True
    valor2 = False
    result = valor1 and valor2

    print(f'Resultado do AND lógico: {result}')

def exercicio_17():

    # Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

    valor1 = input('Digite "True" or "False": ')
    valor2 = input('Digite "True" or "False" novamente: ')
    valor1_bool = valor1 == 'True'
    valor2_bool = valor2 == 'True'

    result = valor1_bool or valor2_bool

    print(f'Resultado do OR lógico: {result}')

def exercicio_18():

    # Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

    valor1 = input('Digite "True" or "False": ')
    valor1_bool = valor1 == 'True'
    result = not valor1_bool

    print(f'O contrário do seu valor é: {result}')

def exercicio_19():

    # Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    result = num1 == num2

    print(f'{num1} == {num2} ? {result}')

def exercicio_20():

    # Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    result = num1 != num2

    print(f'{num1} != {num2} ? {result}')

def exercicio_21():

    # Escreva um programa que converta a temperatura de Celsius para Fahrenheit.
    # O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError.
    # Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

    try:
        celsius = float(input('Digite a temperatura (em Celsius): '))
        fahrenheit = (celsius * 9/5) + 32

        print(f'{celsius}°C é igual a {fahrenheit}°F')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_22():

    # Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
    # Utilize try-except para garantir que a entrada seja uma string.
    # Dica: Utilize a função isinstance() para verificar o tipo da entrada.

    texto = input('Digite um texto qualquer: ')#.strip()

    if not texto.isdigit():
        if texto == texto[::-1]:
            print(f'{texto} é um palíndromo.')
        else:
            print(f'{texto} não é um palíndromo.')
    else:
        print('Entrada inválida.')

def exercicio_23():

    # Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
    # Use try-except para lidar com divisões por zero e entradas não numéricas.
    # Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido.
    # Imprima o resultado ou uma mensagem de erro apropriada.

    try:
        num1 = float(input("Digite um número: ").strip())
        num2 = float(input("Digite outro número: ").strip())
        operador = input("Digite o operador (+, -, * ou /): ").strip()

        # if operador == '+':
        #     result = num1 + num2
        # elif operador == '-':
        #     result = num1 - num2
        # elif operador == '*':
        #     result = num1 * num2
        # elif operador == '/' and num2 != 0:
        #     result = num1 / num2
        # else:
        #     print('Operador inválido ou divisão por zero.')

        match operador:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print('Divisão por zero não é permitida.')
                    result = None
            case _:
                print('Operador inválido.')
                result = None

        print(f'Resultado: {result}')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_24():

    # Escreva um programa que solicite ao usuário para digitar um número.
    # Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero".
    # Adicionalmente, identifique se o número é "par" ou "ímpar".

    try:
        numero = int(input('Digite um número: '))
        if numero > 0:
            print(f'{numero} é positivo')
        elif numero < 0:
            print(f'{numero} é negativo')
        else:
            print('Zero')

        if numero % 2 == 0:
            print(f'{numero} é par')
        else:
            print(f'{numero} é ímpar')

    except Exception as e:
        print(f'Erro: {e}')

def exercicio_25():

    # Crie um script que solicite ao usuário uma lista de números separados por vírgula.
    # O programa deve converter a string de entrada em uma lista de números inteiros.
    # Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro.
    # Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro.
    # Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.

    entrada = input('Digite uma lista de números separados por vírgula: ').strip()
    numeros_str = entrada.split(',')
    numeros_int = []

    try:
        for num in numeros_str:
            numeros_int.append(int(num))

        print(f'Lista de inteiros: {numeros_int}')
    except Exception as e:
        print(f'Erro: {e}')

if __name__ == '__main__':
    exercicio_25()