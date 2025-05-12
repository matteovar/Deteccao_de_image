import pandas as pd
import streamlit as st

st.set_page_config(page_title="Deteccacao", layout="wide")
from src.pages.deteccacao import deteccacao as show_detect
from src.pages.graph import plot_confusion_matrix as show_graph
from src.pages.main_page import main_page as show_main
from streamlit_option_menu import option_menu


def main():
    with st.sidebar:
        # Adicionando o CSS para centralizar o conteúdo da sidebar
        st.sidebar.markdown(
            """
            <style>
                .css-1d391kg {  /* Sidebar container */
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100%;
                }
                .css-1d391kg > div {  /* Menu container */
                    width: 100%;
                }
                .css-1k2zi58 {  /* Title container */
                    text-align: center;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

        selected = option_menu(
            menu_title="Identificador de Chapeu",
            menu_icon="mortarboard",
            options=[
                "Desempenho do Modelo",
                "Classificador de Chapéu",
                "Grafico",
            ],
            default_index=0,
            icons=["easel fill", "radar", "radar"],
            styles={
                "container": {
                    "padding": "5!important",
                    "background-color": "#033572",
                    "width": "100%",
                },
                "icon": {"color": "white", "font-size": "20px"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "padding": "2px",
                    "margin": "0px",
                    "--hover-color": "#000",
                },
            },
        )
    if selected == "Desempenho do Modelo":
        show_main()
    elif selected == "Classificador de Chapéu":
        show_detect()
    elif selected == "Grafico":
        show_graph()


if __name__ == "__main__":
    main()
