import pandas as pd
import plotly.express as px
import streamlit as st
from src.main import df
from src.utils.plotly_charts.imshow_chart import imshow_chart
from src.utils.plotly_charts.bar_chart import bar_chart1
from src.utils.plotly_charts.box_plot import box_plot_chart

df["correto"] = df["true_class"] == df["predicted_class"]


def matriz_confusao(df):
    labels = sorted(df["true_class"].unique())

    # Criar a matriz de confusão
    cm_df = pd.crosstab(
        df["true_class"],
        df["predicted_class"],
        rownames=["Classe Verdadeira"],
        colnames=["Classe Predita"],
        dropna=False,
    )

    cm_df = cm_df.reindex(index=labels, columns=labels, fill_value=0)

    # Chamar a função genérica de imshow
    imshow_chart(
        data=cm_df,
        title="Matriz de Confusão",
        x_label="Classe Predita",
        y_label="Classe Verdadeira",
        color_continuous_scale="Blues",
    )


def boxplot_loss(df):
    box_plot_chart(
        df=df,
        x="correto",
        y="loss",
        color="correto",
        title="Distribuição do Loss por Tipo de Previsão",
        x_label="Previsão Correta?",
        y_label="Erro (Loss)",
        color_label="Previsão Correta?",
        color_discrete_map={True: "#4CAF50", False: "#F44336"},
    )


def acuracia_por_classe(df):
    total_por_classe = df["true_class"].value_counts()
    acertos = df[df["correto"] == True]["true_class"].value_counts()

    acc_df = pd.DataFrame(
        {
            "Classe": total_por_classe.index,
            "Acuracia": [
                acertos.get(cls, 0) / total_por_classe[cls]
                for cls in total_por_classe.index
            ],
        }
    )

    bar_chart1(
        df=acc_df,
        x="Classe",
        y="Acuracia",
        title="Acurácia por Classe Verdadeira",
        color="Classe",
        x_label="Classe",
        y_label="Acurácia",
        range_y=[0, 1],
        text_auto=True,
        text_format=".2%",
    )


# ===============================
# Execução dos gráficos no app
# ===============================


def mostrar_todos_os_graficos():
    st.title("Análise das Previsões do Modelo")

    matriz_confusao(df)

    cols = st.columns(2)
    with cols[0]:
        boxplot_loss(df)
    with cols[1]:
        acuracia_por_classe(df)


mostrar_todos_os_graficos()
