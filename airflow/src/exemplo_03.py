import subprocess

import pandas as pd
import streamlit as st


def load_data():
    df = pd.read_csv("execution_logs.log")
    return df


def run_python_script():
    subprocess.run("poetry run python src/exemplo_02.py")


def main():
    st.title("Visualização de logs e execução de scripts")

    # Carregar os dados do arquivo de log
    df = load_data()

    # Exibir os dados na interface do Streamlit
    st.write("Logs de execução:", df)

    # Botão para atualizar os dados
    if st.button("Atualizar dados"):
        df = load_data()
        st.write("Dados atualizados com sucesso!")

    # Botão para executar o script Python
    if st.button("Executar script python"):
        run_python_script()
        st.write("Script python executado com sucesso!")


if __name__ == "__main__":
    main()
