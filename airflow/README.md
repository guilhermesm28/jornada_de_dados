# Workshop de Airflow

**Apache Airflow** é uma plataforma de código aberto para criar, agendar e monitorar fluxos de trabalho programáticos. Com sua interface em Python, permite definir tarefas complexas como grafos acíclicos direcionados (DAGs) e gerenciar sua execução. Ideal para automatizar e orquestrar pipelines de dados, o Airflow se conecta a várias tecnologias, facilitando a integração e monitoramento de processos.

Basicamente, para utilizar o Airflow em códigos Python, basta seguir o seguinte passo a passo:
- Colocar o script .py na pasta "dags"
- Incluir o decorador @dag antes do pipeline principal
- Incluir o decorador @task antes de cada tarefa do pipeline
- Definir a sequência de execução das tarefas no final do pipeline

Observações:
- Caso tenham várias scripts na pasta "dags", é preciso que o *dag_id* e o nome da função sejam diferentes em cada script.

## Como executar

Como o Airflow depende de muitas configurações para que a infra funcione, utilizamos o [Astro CLI](https://www.astronomer.io/docs/astro/cli/install-cli?tab=windowswithwinget#install-the-astro-cli) para nos auxiliar na criação da infraestrutura.

Após realizar a instalação clicando no link acima e seguindo o passo a passo, basta acessar algum diretório vazio e executar o comando:
`astro dev init`

Neste caso, criei uma pasta **astro** e dentro dela executei o comando acima.
Após a execução, vários arquivos e diretórios são gerados automaticamente para configurarmos a infraestrutura do Airflow.

O próximo comando que devemos executar é o `astro dev start`, que irá baixar um container do Docker com o Airflow já configurado.
É necessário estar no diretório onde foi executado o comando de início do astro e estar com o Docker em execução.

Caso seja necessário atualizar os containers, basta executar o comando `astro dev restart`.

Para fazer o deploy (pago) na Astronomer, basta executar o comando `astro deploy`.

## Arquivos de exemplo (src)

- `exemplo_00.py`: Pipeline simples com 3 atividades encadeadas
- `exemplo_01.py`: Pipeline programada para executar a cada 10 segundos
- `exemplo_02.py`: Pipeline refatorada com logs
- `exemplo_03.py`: Pipeline com tela no streamlit para visualizar o log

## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/04-workflow-orchestration-deploy-airflow) do Luciano.
