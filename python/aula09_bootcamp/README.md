# Aula 09 - Bootcamp de Python

Tópicos de estudo da aula:
- Logs
- Decoradores (@)

Implementando o **utils_log.py** com a função `log_decorator`, não é necessário incluir *try-except* em todas as funções, pois essa função com o log de erro no decorador já chama a função original e mantém a tratativa de erros apenas nele, tornando o código mais limpo.

Na aula vimos que o uso de decoradores é infinito e vai da criatividade do desenvolvedor, como por exemplo criar um decorador de tempo de execução de uma função, um decorador de tentativas de execução de uma função que aborta caso estoure um limite pré-definido ou até mesmo um decorador de cache.

## Loguru

Principal biblioteca de log do Python.

1. Instalar a biblioteca: `poetry add loguru`
2. Importar a biblioteca no projeto: `from loguru import logger`

Abaixo está um exemplo de como configurar o **Loguru** para salvar os logs tanto em um arquivo quanto exibi-los na saída padrão **stderr**:

```
from loguru import logger
from sys import stderr

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="INFO" # qual o nível de log que quero gravar no arquivo
)

# Exemplo de uso do logger
logger.debug("Este é um log para o desenvolvedor no momento do debug.")
logger.info("Este é um log de informação.")
logger.warning("Este é um log de atenção.")
logger.error("Este é um log de erro.")
logger.critical("Este é um log de falha crítica que aborta a aplicação.")
```

## Sentry

O [Sentry](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula09) é uma outra opção de analisar logs, que tem uma SDK que envia os logs para o servidor, assim como Dynatrace por exemplo.

## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula09) do Luciano.
