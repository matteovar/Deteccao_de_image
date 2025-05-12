import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dettecao de Chapeu", layout="wide")


def main():

    pages_1 = {
        "Pages": [
            st.Page("src/pages/main_page.py", title="Main Page"),
            st.Page("src/pages/deteccacao.py", title="Deteccao de Chapeu"),
        ],
    }

    pg = st.navigation(pages_1)
    pg.run()


if __name__ == "__main__":
    main()
