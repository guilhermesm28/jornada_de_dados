# Workshop de Docker

O Docker facilita a configuração e execução do ambiente de desenvolvimento. Ele permite criar, deployar e rodar aplicações em containers, que são ambientes isolados que contêm tudo que a aplicação precisa para rodar.

## Requisitos
- **Docker**: Certifique-se de ter o Docker instalado em sua máquina. Você pode baixar e instalar Docker [aqui](https://www.docker.com/products/docker-desktop).

## Como utilizar

Se o projeto for pequeno, basta utilizar apenas o **Dockerfile**, se não é melhor utilizar em conjunto com o **docker-compose.yml** para não ter que ficar criando vários arquivos para cada container.

Resumindo:

- Dockerfile constrói uma imagem individual.
- Docker Compose coordena e roda múltiplos containers juntos.

1. Criar os arquivos `.dockerignore`, `Dockerfile` e `docker-compose.yml` e preencher conforme exemplos abaixo:

    ### .dockerignore

    ```.dockerignore
    .venv
    ```

    ### Dockerfile

    ```Dockerfile
    FROM python:3.12
    RUN pip install poetry
    COPY . /src
    WORKDIR /src
    RUN poetry install
    EXPOSE 8501
    ENTRYPOINT [ "poetry", "run", "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]
    ```

    ### docker-compose.yml

    ```docker-compose.yml
    version: '3.8'

    services:
        db:
            image: postgres
            volumes:
            - postgres_data:/var/lib/postgresql/data
            environment:
            POSTGRES_USER: myuser
            POSTGRES_PASSWORD: mypassword
            POSTGRES_DB: mydatabase
            ports:
            - "5432:5432"

        pgadmin:
            image: dpage/pgadmin4
            environment:
            PGADMIN_DEFAULT_EMAIL: user@domain.com
            PGADMIN_DEFAULT_PASSWORD: adminpassword
            ports:
            - "8080:80"
            depends_on:
            - db

        app:
            build: .
            ports:
            - "8501:8501"
            environment:
            DB_HOST: db
            DB_NAME: mydatabase
            DB_USER: myuser
            DB_PASS: mypassword
            depends_on:
            - db

    volumes:
        postgres_data:
    ```

2. Criar a imagem com o comando: `docker build -t minha_primeira_imagem .`
3. (opcional) Criar e executar o container com o comando (essa etapa pode ser feita via Docker Desktop): `docker run -d -p 8501:8501 --name meu_primeiro_container minha_primeira_imagem`
4. (opcional) Ao final dos testes, desligar e remover os containers e imagens para não sobrecarregar o disco.

## Comandos

- Baixar imagens: `docker pull wordpress`
- Verificar imagens: `docker images`
- Executar uma imagem criando um container: `docker run --name -p 8080:80 -d wordpress`
- Listar containers em execução: `docker ps`
- Parar um container: `docker stop ID_DO_CONTAINER`
- Iniciar um container: `docker start ID_DO_CONTAINER`
- Reiniciar um container: `docker restart ID_DO_CONTAINER`
- Remover um container (deve estar parado): `docker rm ID_DO_CONTAINER`
- Remover uma imagem (o container deve estar parado): `docker rmi ID_DA_IMAGEM`

## Referências

O repositório com o conteúdo da aula está no [Github](https://github.com/lvgalvao/data-engineering-roadmap/tree/main/03-deploy-de-apps-dados-com-docker) do Luciano.
