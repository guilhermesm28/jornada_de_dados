# Aula 15 - Bootcamp de Python

Nesta aula, o foco foi concluir os estudos sobre Programação Orientada a Objetos (POO) em Python e realizar alguns exercícios.

O intuito foi criar uma API simples para demonstrar o uso de POO com algumas bibliotecas muito úteis, como por exemplo a **Faker**.

Para executar o FastAPI corretamente é necessário instalar o Uvicorn, que é um servidor ASGI para Python, com o comando:

`poetry add uvicorn`

Para rodar a API, execute o comando:

`poetry run uvicorn src.FakeAPI.start:app --reload`

Para acessar a documentação da API, acesse o link:

`http://127.0.0.1:8000/docs`

Para gerar uma lista de compras, você pode acessar o endpoint:

`http://127.0.0.1:8000/gerar_compras/{numero_registro}`

Substituindo o `{numero_registro}` pelo número de registros que você deseja gerar.

## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados) do Luciano.
