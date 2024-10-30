from time import sleep

from loguru import logger

logger.add(
    "execution_logs.log", format="{time} - {message}", level="INFO", rotation="1 day"
)


def primeira_atividade():
    logger.info("Primeira atividade iniciada...")
    sleep(2)
    logger.info("Primeira atividade finalizada!")


def segunda_atividade():
    logger.info("Segunda atividade iniciada...")
    sleep(2)
    logger.info("Segunda atividade finalizada!")


def terceira_atividade():
    logger.info("Terceira atividade iniciada...")
    sleep(2)
    logger.info("Terceira atividade finalizada!")


def pipeline():
    logger.info("Pipeline em execução...")
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline finalizada!")


if __name__ == "__main__":
    while True:
        pipeline()
        sleep(10)
