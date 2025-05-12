import pandas as pd
import streamlit as st

df = pd.read_csv("app/data/input/resultados_predicoes.csv")


def get_data_agg(df: pd.DataFrame, column_name: str, agg_type: str = "sum"):
    return df[column_name].agg(agg_type)


def get_conditional_count(
    df: pd.DataFrame, true_class: str, predicted_class: str
) -> int:
    return (
        (df["true_class"] == true_class) & (df["predicted_class"] == predicted_class)
    ).sum()
