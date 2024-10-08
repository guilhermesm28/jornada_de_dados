# Aula 09 - Bootcamp de Python

Tópicos de estudo da aula:
- Logs
- Decoradores

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
    level="INFO"
)

# Exemplo de uso do logger
logger.info("Este é um log de informação.")
logger.error("Este é um log de erro.")
```

## Sentry

O [Sentry](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula09) é uma outra opção de analisar logs, que tem uma SDK que envia os logs para o servidor, assim como Dynatrace por exemplo.

## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula09) do Luciano.
