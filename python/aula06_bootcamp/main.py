CONSTANTE_BONUS: int = 1000

usuarios: dict = {}
continuar: str = "s"

while continuar == "s":

    # Solicitar ao usuário que digite seu nome

    nome_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False

    while nome_valido is not True:

        try:

            nome: str = input("Digite seu nome: ").strip()

            if nome.isdigit():
                raise ValueError("Você digitou um número.")
            if len(nome) == 0:
                raise ValueError("O nome não pode estar vazio.")
            else:
                nome_valido = True

        except Exception as e:
            print(f"Erro: {e}")

    # Solicitar ao usuário que digite o valor do seu salário
    # e converter a entrada para um número flutuante

    while salario_valido is not True:

        try:

            salario: float = float(input("Digite seu salário: "))

            if salario < 0:
                raise ValueError("Salário inválido.")
            else:
                salario_valido = True

        except Exception as e:
            print(f"Erro: {e}")

    # Solicitar ao usuário que digite a porcentagem do bônus recebido
    # e converter a entrada para um número flutuante

    while bonus_valido is not True:

        try:

            bonus: float = float(input("Digite a porcentagem do bônus: "))

            if bonus < 0:
                raise ValueError("Bônus inválido.")
            else:
                bonus_valido = True

        except Exception as e:
            print(f"Erro: {e}")

    # Calcular o valor do bônus final

    kpi: float = CONSTANTE_BONUS + (salario * bonus)

    if nome not in usuarios:
        usuarios[nome] = {
            "Nome": nome,
            "Salário": salario,
            "Bônus": bonus,
            "Valor bônus": kpi,
        }
    else:
        print(f"O usuário {nome} já existe e será atualizado")
        usuarios[nome]["Salário"] = salario
        usuarios[nome]["Bônus"] = bonus
        usuarios[nome]["Valor bônus"] = kpi

    continuar: str = input("Cadastrar novo usuário? (s/n): ").strip().lower()

print("\nLista de usuários:")

for key, value in usuarios.items():

    print(f"{key}: {value}")
