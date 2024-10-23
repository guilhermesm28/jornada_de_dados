-- Criação da tabela com particionamento RANGE
CREATE TABLE pessoas_part (
         id SERIAL PRIMARY KEY,
         first_name VARCHAR(3),
         last_name VARCHAR(3),
         estado VARCHAR(3)
     ) PARTITION BY RANGE (id);

-- Criar as partições
CREATE TABLE pessoas_part1 PARTITION OF pessoas_part FOR VALUES FROM (MINVALUE) TO (2000001);
CREATE TABLE pessoas_part2 PARTITION OF pessoas_part FOR VALUES FROM (2000001) TO (4000001);
CREATE TABLE pessoas_part3 PARTITION OF pessoas_part FOR VALUES FROM (4000001) TO (6000001);
CREATE TABLE pessoas_part4 PARTITION OF pessoas_part FOR VALUES FROM (6000001) TO (8000001);
CREATE TABLE pessoas_part5 PARTITION OF pessoas_part FOR VALUES FROM (8000001) TO (MAXVALUE);

-- Inserir dados na tabela pessoas_part com estados aleatórios
INSERT INTO
  pessoas_part (first_name, last_name, estado)
SELECT
  substring(md5(random()::text), 0, 3),
  substring(md5(random()::text), 0, 3),
  random_estado ()
FROM
  generate_series(1, 10000000);

-- Criação da tabela com particionamento LIST (é preciso inserir na PK também caso não seja a própria PK)
CREATE TABLE pessoas_part_estado (
    id SERIAL,
    first_name VARCHAR(3),
    last_name VARCHAR(3),
    estado VARCHAR(3),
    PRIMARY KEY (id, estado)
) PARTITION BY LIST (estado);

-- Criar as partições
CREATE TABLE pessoas_sp PARTITION OF pessoas_part_estado FOR VALUES IN ('SP');
CREATE TABLE pessoas_rj PARTITION OF pessoas_part_estado FOR VALUES IN ('RJ');
CREATE TABLE pessoas_mg PARTITION OF pessoas_part_estado FOR VALUES IN ('MG');
CREATE TABLE pessoas_es PARTITION OF pessoas_part_estado FOR VALUES IN ('ES');
CREATE TABLE pessoas_df PARTITION OF pessoas_part_estado FOR VALUES IN ('DF');

-- Inserir dados na tabela pessoas_part_estado com estados aleatórios
INSERT INTO
  pessoas_part_estado (first_name, last_name, estado)
SELECT
  substring(md5(random()::text), 0, 3),
  substring(md5(random()::text), 0, 3),
  random_estado ()
FROM
  generate_series(1, 10000000);
