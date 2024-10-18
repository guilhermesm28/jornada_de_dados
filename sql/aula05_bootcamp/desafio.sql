-- Qual foi o total de receitas no ano de 1997?
CREATE VIEW total_revenues_1997_view AS
SELECT SUM((order_details.unit_price) * order_details.quantity * (1.0 - order_details.discount)) AS total_revenues_1997
FROM order_details
INNER JOIN (
    SELECT order_id
    FROM orders
    WHERE EXTRACT(YEAR FROM order_date) = '1997'
) AS ord
ON ord.order_id = order_details.order_id;

-- Faça uma análise de crescimento mensal e o cálculo de YTD
CREATE VIEW view_receitas_acumuladas AS
WITH ReceitasMensais AS (
    SELECT
        EXTRACT(YEAR FROM orders.order_date) AS Ano,
        EXTRACT(MONTH FROM orders.order_date) AS Mes,
        SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS Receita_Mensal
    FROM
        orders
    INNER JOIN
        order_details ON orders.order_id = order_details.order_id
    GROUP BY
        EXTRACT(YEAR FROM orders.order_date),
        EXTRACT(MONTH FROM orders.order_date)
),
ReceitasAcumuladas AS (
    SELECT
        Ano,
        Mes,
        Receita_Mensal,
        SUM(Receita_Mensal) OVER (PARTITION BY Ano ORDER BY Mes) AS Receita_YTD
    FROM
        ReceitasMensais
)
SELECT
    Ano,
    Mes,
    Receita_Mensal,
    Receita_Mensal - LAG(Receita_Mensal) OVER (PARTITION BY Ano ORDER BY Mes) AS Diferenca_Mensal,
    Receita_YTD,
    (Receita_Mensal - LAG(Receita_Mensal) OVER (PARTITION BY Ano ORDER BY Mes)) / LAG(Receita_Mensal) OVER (PARTITION BY Ano ORDER BY Mes) * 100 AS Percentual_Mudanca_Mensal
FROM
    ReceitasAcumuladas
ORDER BY
    Ano, Mes;

-- Qual é o valor total que cada cliente já pagou até agora?
CREATE VIEW view_total_revenues_per_customer AS
SELECT
    customers.company_name,
    SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS total
FROM
    customers
INNER JOIN
    orders ON customers.customer_id = orders.customer_id
INNER JOIN
    order_details ON order_details.order_id = orders.order_id
GROUP BY
    customers.company_name
ORDER BY
    total DESC;

-- Separe os clientes em 5 grupos de acordo com o valor pago por cliente
CREATE VIEW view_total_revenues_per_customer_group AS
    SELECT
    customers.company_name,
    SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS total,
    NTILE(5) OVER (ORDER BY SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) DESC) AS group_number
FROM
    customers
INNER JOIN
    orders ON customers.customer_id = orders.customer_id
INNER JOIN
    order_details ON order_details.order_id = orders.order_id
GROUP BY
    customers.company_name
ORDER BY
    total DESC;

-- Agora somente os clientes que estão nos grupos 3, 4 e 5 para que seja feita uma análise de Marketing especial com eles
CREATE VIEW clients_to_marketing AS
WITH clientes_para_marketing AS (
    SELECT
    customers.company_name,
    SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS total,
    NTILE(5) OVER (ORDER BY SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) DESC) AS group_number
FROM
    customers
INNER JOIN
    orders ON customers.customer_id = orders.customer_id
INNER JOIN
    order_details ON order_details.order_id = orders.order_id
GROUP BY
    customers.company_name
ORDER BY
    total DESC
)

SELECT *
FROM clientes_para_marketing
WHERE group_number >= 3;

-- Identificar os 10 produtos mais vendidos.
CREATE VIEW top_10_products AS
SELECT products.product_name, SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS sales
FROM products
INNER JOIN order_details ON order_details.product_id = products.product_id
GROUP BY products.product_name
ORDER BY sales DESC;

-- Quais clientes do Reino Unido pagaram mais de 1000 dólares?
CREATE VIEW uk_clients_who_pay_more_then_1000 AS
SELECT customers.contact_name, SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount) * 100) / 100 AS payments
FROM customers
INNER JOIN orders ON orders.customer_id = customers.customer_id
INNER JOIN order_details ON order_details.order_id = orders.order_id
WHERE LOWER(customers.country) = 'uk'
GROUP BY customers.contact_name
HAVING SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) > 1000;
