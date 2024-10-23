 -- Criação da tabela
CREATE TABLE
  pessoas (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(3),
    last_name VARCHAR(3),
    estado VARCHAR(3)
  );

-- Inserção de 1 milhão de registros
CREATE
OR REPLACE FUNCTION random_estado () RETURNS VARCHAR(3) AS $$
BEGIN
   RETURN CASE floor(random() * 5)
         WHEN 0 THEN 'SP'
         WHEN 1 THEN 'RJ'
         WHEN 2 THEN 'MG'
         WHEN 3 THEN 'ES'
         ELSE 'DF'
         END;
END;
$$ LANGUAGE plpgsql;

-- Inserir dados na tabela pessoas com estados aleatórios
INSERT INTO
  pessoas (first_name, last_name, estado)
SELECT
  substring(md5(random()::text), 0, 3),
  substring(md5(random()::text), 0, 3),
  random_estado ()
FROM
  generate_series(1, 10000000);

-- Criação do índice
CREATE INDEX
  first_name_index ON pessoas (first_name);

-- Busca pelo índice - 0.185 s
SELECT
  COUNT(*)
FROM
  pessoas
WHERE
  first_name = 'aa';

-- Busca sem índice - 0.337 s
SELECT
  COUNT(*)
FROM
  pessoas
WHERE
  last_name = 'aa';
