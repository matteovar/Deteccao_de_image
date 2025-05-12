import plotly.express as px
import streamlit as st
import pandas as pd


def box_plot_chart(
    df: pd.DataFrame,
    x: str = None,
    y: str = None,
    color: str = None,
    title: str = "Boxplot",
    x_label: str = None,
    y_label: str = None,
    color_label: str = None,
    points: str = "outliers",  # "all", "outliers", False
    color_discrete_map: dict = None,
):
    labels = {}
    if x:
        labels[x] = x_label if x_label else x
    if y:
        labels[y] = y_label if y_label else y
    if color and color_label:
        labels[color] = color_label

    fig = px.box(
        df,
        x=x,
        y=y,
        color=color,
        points=points,
        labels=labels,
        title=title,
        color_discrete_map=color_discrete_map,
    )
    st.plotly_chart(fig)
