 -- Subquery
SELECT
  product_id
FROM
  (
    SELECT
      product_id
    FROM
      (
        SELECT
          product_id,
          rank
        FROM
          (
            SELECT
              product_id,
              SUM(
                det.quantity * det.unit_price * (1 - det.discount)
              ) sold_value,
              RANK() OVER (
                ORDER BY
                  SUM(
                    det.quantity * det.unit_price * (1 - det.discount)
                  ) DESC
              ) rank -- WINDOWS FUNCTION
            FROM
              order_details det
            GROUP BY
              det.product_id
            ORDER BY
              rank
          )
        WHERE
          rank <= 5
      )
    WHERE
      product_id BETWEEN 35 and 65
  )
ORDER BY
  product_id DESC;

-- CTE
WITH
  CalculatedValues AS (
    SELECT
      product_id,
      SUM(
        det.quantity * det.unit_price * (1 - det.discount)
      ) AS sold_value,
      RANK() OVER (
        ORDER BY
          SUM(
            det.quantity * det.unit_price * (1 - det.discount)
          ) DESC
      ) AS rank
    FROM
      order_details det
    GROUP BY
      product_id
  ),
  TopRankedProducts AS (
    SELECT
      product_id
    FROM
      CalculatedValues
    WHERE
      rank <= 5
  ),
  FilteredProducts AS (
    SELECT
      product_id
    FROM
      TopRankedProducts
    WHERE
      product_id BETWEEN 35 AND 65
  )
SELECT
  product_id
FROM
  FilteredProducts
ORDER BY
  product_id DESC;

-- View
CREATE VIEW
  TotalRevenues AS
SELECT
  customers.company_name,
  SUM(
    order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)
  ) AS total
FROM
  customers
  INNER JOIN orders ON customers.customer_id = orders.customer_id
  INNER JOIN order_details ON order_details.order_id = orders.order_id
GROUP BY
  customers.company_name;

SELECT
  *
FROM
  TotalRevenues;

-- Temp table
CREATE TEMP TABLE
  TempTotalRevenues AS
SELECT
  customers.company_name,
  SUM(
    order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)
  ) AS total
FROM
  customers
  INNER JOIN orders ON customers.customer_id = orders.customer_id
  INNER JOIN order_details ON order_details.order_id = orders.order_id
GROUP BY
  customers.company_name;

SELECT
  *
FROM
  TempTotalRevenues;

-- Materialized view
CREATE MATERIALIZED VIEW
  MaterializedTotalRevenues AS
SELECT
  customers.company_name,
  SUM(
    order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)
  ) AS total
FROM
  customers
  INNER JOIN orders ON customers.customer_id = orders.customer_id
  INNER JOIN order_details ON order_details.order_id = orders.order_id
GROUP BY
  customers.company_name;

SELECT
  *
FROM
  MaterializedTotalRevenues;

REFRESH MATERIALIZED VIEW MaterializedTotalRevenues;
