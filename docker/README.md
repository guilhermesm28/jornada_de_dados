# Workshop de Docker

O Docker facilita a configuração e execução do ambiente de desenvolvimento. Ele permite criar, deployar e rodar aplicações em containers, que são ambientes isolados que contêm tudo que a aplicação precisa para rodar.

## Requisitos
- **Docker**: Certifique-se de ter o Docker instalado em sua máquina. Você pode baixar e instalar Docker [aqui](https://www.docker.com/products/docker-desktop).

## Como utilizar

1. Criar os arquivos `Dockerfile` e `.dockerignore` e preencher conforme exemplos abaixo:

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

2. Criar a imagem com o comando: `docker build -t minha_primeira_imagem .`
3. Criar e executar o container com o comando: `docker run -d -p 8501:8501 --name meu_primeiro_container minha_primeira_imagem`
