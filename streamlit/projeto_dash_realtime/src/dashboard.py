import pandas as pd

import streamlit as st

st.set_page_config(
    page_title="Workshop Streamlit - Realtime Dashboard", page_icon="📈", layout="wide"
)


@st.cache_data
def get_data():
    df = pd.read_parquet("data/orders.parquet")
    df["order_date"] = pd.to_datetime(df["order_date"])

    return df


orders_df = get_data()

st.title("Workshop Streamlit - Realtime Dashboard")

st.dataframe(orders_df)
