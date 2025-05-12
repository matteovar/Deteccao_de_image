import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.metrics import confusion_matrix
from src.main import df


def plot_confusion_matrix():
    # Gerar a matriz de confusão
    labels = sorted(df["true_class"].unique())
    cm = confusion_matrix(df["true_class"], df["predicted_class"], labels=labels)

    # Converter para DataFrame para visualização com Plotly
    cm_df = pd.DataFrame(cm, index=labels, columns=labels)

    # Gráfico com plotly
    fig = px.imshow(
        cm_df,
        text_auto=True,
        color_continuous_scale="Blues",
        labels=dict(x="Classe Predita", y="Classe Verdadeira", color="Contagem"),
        x=labels,
        y=labels,
        title="Matriz de Confusão",
    )

    # Ajuste de layout para melhor visualização
    fig.update_layout(
        xaxis=dict(side="bottom"),
        yaxis=dict(autorange="reversed"),  # Coloca a origem no canto superior esquerdo
    )

    # Mostrar no Streamlit
    st.plotly_chart(fig)


plot_confusion_matrix()
