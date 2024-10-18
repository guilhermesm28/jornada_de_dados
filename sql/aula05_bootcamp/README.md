# Aula 05 - Bootcamp de SQL

Projeto de estudo de SQL com o banco de dados [Northwind](https://github.com/pthom/northwind_psql).

Para cada pergunta foi criado uma view no PostgreSQL, conforme abaixo:

1. Qual foi o total de receitas no ano de 1997? `total_revenues_1997_view`
2. Faça uma análise de crescimento mensal e o cálculo de YTD `view_receitas_acumuladas`
3. Qual é o valor total que cada cliente já pagou até agora? `view_total_revenues_per_customer`
4. Separe os clientes em 5 grupos de acordo com o valor pago por cliente `view_total_revenues_per_customer_group`
5. Agora somente os clientes que estão nos grupos 3, 4 e 5 para que seja feita uma análise de Marketing especial com eles `clients_to_marketing`
6. Identificar os 10 produtos mais vendidos. `top_10_products`
7. Quais clientes do Reino Unido pagaram mais de 1000 dólares? `uk_clients_who_pay_more_then_1000`

Para executar o projeto, é necessário ter o [Docker](https://www.docker.com/) instalado na máquina.

## Como executar

1. Clone o repositório
2. Suba os containers com o comando `docker-compose up -d`
3. Acesse o PgAdmin no endereço [http://localhost:5050/browser/](http://localhost:5050/browser/)
4. Configurar a senha master do PgAdmin como `postgres`
5. Criar um novo servidor clicando com o botão direito do mouse em `Server -> Register -> Server...` e preencher com os seguintes dados:

    ```
    General -> Name: db
    Connection -> Host: db
    Connection -> Username: postgres
    Connection -> Password: postgres
    ```


## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/Northwind-SQL-Analytics/tree/main) do Luciano.
