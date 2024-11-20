# Workshop de Streamlit

O **Streamlit** é basicamente uma abstração de HTML, CSS e Javascript no Python, o que torna fácil o desenvolvimento de front-end.

## Ruff

Nesse Workshop, aprendemos a utilizar o **Ruff**, que é uma biblioteca responsável por checar o código assim como o Flake e Black por exemplo, mas de uma maneira mais rápida.

Uma boa prática é separar bibliotecas de desenvolvimento e bibliotecas de ação (que são realmente necessárias para o projeto em produção).
Para isso, executamos o seguinte comando no poetry:

`poetry add --group dev ruff`

### Configurando Ruff no `pyproject.toml``

```
[tool.ruff]
# Configurações de linting
line-length = 88  # Comprimento máximo de linha
select = ["E", "F", "W"]  # Seleciona as categorias de erros e avisos
ignore = ["E203", "W503"]  # Ignora regras específicas

# Adicione paths específicos se necessário
exclude = ["build", "dist"]

# Para especificar o conjunto de regras do Black para formatação
extend-select = ["B"]
```

### Análise estática (ajustes manuais)

```
ruff check .
```

### Correção automática e formatação

```
ruff check . --fix
ruff format .
```

## Dashboard Realtime

Para o projeto *Dashboard Realtime*, utilizamos o Kafka. Para isso, foi necessário se cadastrar no site do [Confluent](https://confluent.cloud/home) e no menu *Billing & Payment* incluir o cupom **CONFLUENTDEV1** para não ter a necessidade de incluir o cartão de crédito. Após isso, basta criar um novo environment com as opções básicas.

## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/09-streamlit-dashboard-realtime) do Luciano.
