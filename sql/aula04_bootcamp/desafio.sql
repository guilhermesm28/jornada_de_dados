 -- Faça a classificação dos produtos mais vendidos usando RANK(), DENSE_RANK() e ROW_NUMBER()
SELECT
  o.order_id,
  p.product_name,
  (o.unit_price * o.quantity) AS total_sale,
  ROW_NUMBER() OVER (
    ORDER BY
      (o.unit_price * o.quantity) DESC
  ) AS order_rn,
  RANK() OVER (
    ORDER BY
      (o.unit_price * o.quantity) DESC
  ) AS order_rank,
  DENSE_RANK() OVER (
    ORDER BY
      (o.unit_price * o.quantity) DESC
  ) AS order_dense
FROM
  order_details o
  JOIN products p ON p.product_id = o.product_id;

-- Listar funcionários dividindo-os em 3 grupos usando NTILE
SELECT
  first_name,
  last_name,
  title,
  NTILE(3) OVER (
    ORDER BY
      first_name
  ) AS group_number
FROM
  employees;

-- Ordenando os custos de envio pagos pelos clientes de acordo
-- com suas datas de pedido, mostrando o custo anterior e o custo posterior usando LAG e LEAD:
SELECT
  customer_id,
  TO_CHAR(order_date, 'YYYY-MM-DD') AS order_date,
  shippers.company_name AS shipper_name,
  LAG(freight) OVER (
    PARTITION BY
      customer_id
    ORDER BY
      order_date DESC
  ) AS previous_order_freight,
  freight AS order_freight,
  LEAD(freight) OVER (
    PARTITION BY
      customer_id
    ORDER BY
      order_date DESC
  ) AS next_order_freight
FROM
  orders
  JOIN shippers ON shippers.shipper_id = orders.ship_via;
