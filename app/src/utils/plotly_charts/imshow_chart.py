import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np


def imshow_chart(
    data,
    title: str = "Imagem",
    x_label: str = None,
    y_label: str = None,
    color_continuous_scale: str = "Viridis",
    zmin=None,
    zmax=None,
    text_auto=True,
):
    fig = px.imshow(
        data,
        color_continuous_scale=color_continuous_scale,
        zmin=zmin,
        zmax=zmax,
        labels={
            "x": x_label if x_label else "x",
            "y": y_label if y_label else "y",
            "color": "Intensidade",
        },
        title=title,
        text_auto=text_auto,
    )
    fig.update_layout(xaxis=dict(side="bottom"), yaxis=dict(autorange="reversed"))
    st.plotly_chart(fig)
