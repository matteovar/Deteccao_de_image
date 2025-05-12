import os

import pandas as pd
import streamlit as st
from src.main import df, get_conditional_count, get_data_agg
from src.utils.cards import create_cards, create_title, model


def main_page():
    # Título principal
    create_title("Análise de Desempenho do Modelo")

    # Cálculos das métricas
    total_corretos_com_chapeu = get_conditional_count(df, "com_chapeu", "com_chapeu")
    total_corretos_com_sem_chapeu = get_conditional_count(
        df, "com_chapeu", "sem_chapeu"
    )
    total_corretos_sem_com_chapeu = get_conditional_count(
        df, "sem_chapeu", "com_chapeu"
    )
    total_corretos_sem_chapeu = get_conditional_count(df, "sem_chapeu", "sem_chapeu")

    precisao_cc = total_corretos_com_chapeu / (
        total_corretos_com_chapeu + total_corretos_sem_com_chapeu
    )
    precisao_sc = total_corretos_sem_chapeu / (
        total_corretos_sem_chapeu + total_corretos_com_sem_chapeu
    )

    recall_cc = total_corretos_com_chapeu / (
        total_corretos_com_chapeu + total_corretos_com_sem_chapeu
    )
    recall_sc = total_corretos_sem_chapeu / (
        total_corretos_sem_chapeu + total_corretos_sem_com_chapeu
    )

    # Função para exibir as métricas principais
    def get_metric(df):
        cols = st.columns(3)

        total = get_data_agg(df, "filename", "count")
        total_corretos = (df["true_class"] == df["predicted_class"]).sum()

        with cols[0]:
            create_cards(
                title="Acurácia do Modelo", value=f"{total_corretos / total:.4}"
            )
        with cols[1]:
            create_cards(title="Total de Imagens", value=total)
        with cols[2]:
            create_cards(title="Total de Imagens Correta", value=total_corretos)

    def precisao(df):
        model(
            title="Precisão do Modelo",
            title1="Precisão - Com Chapéu",
            value1=precisao_cc,
            title2="Precisão - Sem Chapéu",
            value2=f"{precisao_sc:.4}",
        )

    def recall(df):

        model(
            title="Recall do Modelo",
            title1="Recall - Com Chapéu",
            value1=f"{recall_cc:.2f}",
            title2="Recall - Sem Chapéu",
            value2=f"{recall_sc:.2f}",
        )

    # Função para exibir F1 Score
    def f1_score(df):

        f1_cc = 2 * (precisao_cc * recall_cc) / (precisao_cc + recall_cc)
        f1_sc = 2 * (precisao_sc * recall_sc) / (precisao_sc + recall_sc)

        model(
            title="F1 Score do Modelo",
            title1="F1 Score - Com Chapéu",
            value1=f"{f1_cc:.2f}",
            title2="F1 Score - Sem Chapéu",
            value2=f"{f1_sc:.2f}",
        )

    # Chamando as funções
    get_metric(df)
    columns = st.columns(2)
    # Add a border around the "Precisão" function
    with columns[0]:
        precisao(df)
    with columns[1]:
        recall(df)
    f1_score(df)


main_page()
