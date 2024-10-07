# Aula 06 - Bootcamp de Python

## Iniciando um novo ambiente de desenvolvimento:

1. Verificar quais versões do Python já estão instaladas no Pyenv: `pyenv versions`
2. Selecionar uma versão local para o ambiente: `pyenv local 3.12.1`
3. Padronizar o projeto com o Poetry: `poetry init`
4. Criar o ambiente virtual com o Poetry: `poetry env use 3.12.1`
5. Ativar o ambiente virtual com o Poetry: `poetry shell`

## Instalando bibliotecas para revisão e boas práticas de código

### Flake8

A biblioteca **Flake8** não altera o código, apenas dá as dicas para que a correção seja feita de forma manual.

1. Adicionar a biblioteca: `poetry add flake8`
2. Executar a biblioteca (substituir o nome do arquivo): `poetry run flake8 main.py`

Como a biblioteca Flake8 e a Black não se conversam devido a algumas definições diferentes, é possível criar um arquivo `.flake8` e inserir o conteúdo abaixo:

```
[flake8]
max-line-length = 89
extend-ignore = E203,E701,W291
```

### Black

A biblioteca **Black** altera o código de acordo com as boas práticas, porém não se conversa muito bem com a biblioteca Flake8.

1. Adicionar a biblioteca: `poetry add black`
2. Executar a biblioteca (substituir o nome do arquivo): `poetry run black main.py`

### Blue

A biblioteca **Blue** altera o código de acordo com as boas práticas e já possui embutido em seu script as bibliotecas Flake8 e Black.

1. Adicionar a biblioteca: `poetry add blue`
2. Executar a biblioteca (substituir o nome do arquivo): `poetry run blue main.py`

### iSort

A biblioteca **iSort** altera o código de acordo com as boas práticas, assim como o Black e o Blue.

Para poder executar as 3 bibliotecas juntas (Flake8, Black e iSort) é preciso adicionar no arquivo `pyproject.toml` as linhas abaixo:

```
[tool.isort]
profile = "black"
```

### Pre-Commit

A biblioteca **pre-commit** garante que todo o script segue um padrão no momento do commit a partir de várias bibliotecas. No [link](https://pre-commit.com/hooks) é possível verificar todos os hooks possíveis com a biblioteca.

As bibliotecas utilizadas no pre-commit devem ser alinhadas entre o time de desenvolvimento, mas os mais comuns são as bibliotecas de formatação como **Flake8**, **iSort** e **Black**, além da biblioteca **Bandit** que é focada em segurança.

1. Adicionar a biblioteca: `poetry add pre-commit`
2. Criar o arquivo `.pre-commit-config.yaml` com o conteúdo abaixo:

```
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
        args: [--markdown-linebreak-ext=md]
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: detect-private-key
      - id: check-added-large-files
  - repo: https://github.com/psf/black-pre-commit-mirror
    rev: 24.1.1
    hooks:
      - id: black
        language_version: python3.12.1
  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        name: isort (python)
  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
```

3. Garantir que a versão do Python citada no script acima está instalada no Pyenv.
4. Executar o comando para configurar o pre-commit dentro da pasta .git: `poetry run pre-commit install`
5. Executar o commit para que a biblioteca faça a análise dos scripts: `git commit -m 'configurando bibliotecas para padronização de código'`
6. Caso algum ajuste falhar, as bibliotecas farão o ajuste automaticamente e é preciso adicionar as mudanças e fazer o commit novamente. É possível que alguma falha não seja corrigida automaticamente, principalmente se for a biblioteca Flake8, então é preciso fazer o ajuste manualmente como por exemplo o código **E501**, ou então inserir esse ID como *extend-ignore* no arquivo **.flake8**.

Não é necessário ter as bibliotecas instaladas a parte, apenas com o pre-commit e o arquivo de configuração já é possível executar, mas apenas no momento do commit. Se for necessário fazer algum teste antes, é recomendado instalar as bibliotecas separadamente.

## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula06/aovivo) do Luciano.
