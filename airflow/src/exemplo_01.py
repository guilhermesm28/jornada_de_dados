from time import sleep


def primeira_atividade():
    print("Primeira atividade iniciada...")
    sleep(2)
    print("Primeira atividade finalizada!")


def segunda_atividade():
    print("Segunda atividade iniciada...")
    sleep(2)
    print("Segunda atividade finalizada!")


def terceira_atividade():
    print("Terceira atividade iniciada...")
    sleep(2)
    print("Terceira atividade finalizada!")


def pipeline():
    print("\nPipeline em execução...\n")
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print("\nPipeline finalizada!")


if __name__ == "__main__":
    while True:
        pipeline()
        sleep(10)
