import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dettecao de Chapeu", layout="wide")


def main():

    pages_1 = {
        "Identificador de Chapeu": [
            st.Page("src/pages/main_page.py", title="Desempenho do Modelo"),
            st.Page("src/pages/deteccacao.py", title="Classificador de Chapeu"),
            st.Page("src/pages/graph.py", title="Análise das Previsões do Modelo"),
        ],
    }

    pg = st.navigation(pages_1)
    pg.run()


if __name__ == "__main__":
    main()
