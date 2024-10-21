# Aula 11 - Bootcamp de SQL

Tópicos de estudo da aula:
- Performance Tuning em SQL
- Ordem de execução e otimização de consultas

## Ordem de execução

1. Verifica se existe erro de sintaxe
2. Verifica se existe erro de semântica
3. Verifica se existe cache para a consulta
4. Otimiza a consulta gerando o plano de execução
5. Executa a consulta

## Ordem de execução de uma consulta (padrão, mas pode variar dependendo do passo 4 anterior)

1. FROM
2. JOIN (e ON)
3. WHERE
4. GROUP BY
5. HAVING
6. SELECT
7. ORDER BY
8. LIMIT

## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20SQL%20e%20Analytics/Aula-11) do Luciano.
