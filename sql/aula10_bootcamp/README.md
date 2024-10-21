# Aula 10 - Bootcamp de SQL

Tópicos de estudo da aula:
- Transações `ACID`

`A` -> Atomicidade (ou funciona 100% *commit* ou não funciona *rollback*)

```sql
BEGIN;
UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
UPDATE conta SET saldo = saldo + 100 WHERE id = 2;
COMMIT;
```

```sql
BEGIN;
UPDATE conta SET saldo = saldo - 100 WHERE id = 1;
UPDATE conta SET saldo = saldo + 100 WHERE id = 2;
ROLLBACK;
```

`C` -> Consistência (dados consistentes com regras de negócio)

Checa todas as regras de negócio no banco de dados antes de commitar (constraint, trigger, etc)

`I` -> Isolamento (transações não interferem uma na outra)

```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN;
SELECT nome, count(nome) FROM exemplo
GROUP by nome;
SELECT * FROM exemplo;
COMMIT;
```

O comando `WITH (NO LOCK)` é usado para evitar que outras transações modifiquem os dados enquanto a consulta está sendo executada. O level de isolamento `REPEATABLE READ` é o mais restritivo, mas pode causar *lock* no banco de dados.

Existem outros níveis de isolamento:
- `READ COMMITTED` -> Não bloqueia a leitura de dados
- `READ UNCOMMITTED` -> Não bloqueia a leitura de dados
- `SERIALIZABLE` -> Bloqueia a leitura de dados

`D` -> Durabilidade (dados persistem mesmo que haja falhas)

Garante que os dados estejam salvos mesmo que haja falhas no sistema.

## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20SQL%20e%20Analytics/Aula-10) do Luciano.
