import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.metrics import confusion_matrix
from src.main import df

# Adiciona coluna de acertos
df["correto"] = df["true_class"] == df["predicted_class"]


def matriz_confusao():
    labels = sorted(df["true_class"].unique())
    cm = confusion_matrix(df["true_class"], df["predicted_class"], labels=labels)
    cm_df = pd.DataFrame(cm, index=labels, columns=labels)

    fig = px.imshow(
        cm_df,
        text_auto=True,
        color_continuous_scale="Blues",
        labels=dict(x="Classe Predita", y="Classe Verdadeira", color="Contagem"),
        title="Matriz de Confusão",
    )
    fig.update_layout(xaxis=dict(side="bottom"), yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig)


def boxplot_loss():
    fig = px.box(
        df,
        x="correto",
        y="loss",
        color="correto",
        color_discrete_map={True: "#4CAF50", False: "#F44336"},
        labels={"correto": "Previsão Correta?", "loss": "Erro (Loss)"},
        title="Distribuição do Loss por Tipo de Previsão",
    )
    st.plotly_chart(fig)


def acuracia_por_classe():
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

    fig = px.bar(
        acc_df,
        x="Classe",
        y="Acuracia",
        color="Classe",
        text="Acuracia",
        title="Acurácia por Classe Verdadeira",
        labels={"Acuracia": "Acurácia"},
        range_y=[0, 1],
    )
    fig.update_traces(texttemplate="%{text:.2%}", textposition="outside")
    st.plotly_chart(fig)


# ===============================
# Execução dos gráficos no app
# ===============================


def mostrar_todos_os_graficos():
    st.title("Análise das Previsões do Modelo")

    st.header("2. Matriz de Confusão")
    matriz_confusao()

    st.header("4. Boxplot do Loss por Tipo de Previsão")
    boxplot_loss()

    st.header("6. Acurácia por Classe")
    acuracia_por_classe()


mostrar_todos_os_graficos()
