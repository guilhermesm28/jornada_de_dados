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

orders_col, items_col, ticket_col, total_col = st.columns(4)

with orders_col:
    quantity = len(orders_df)
    quantity = f"{quantity:,.0f}"
    st.metric("Orders", quantity)

with items_col:
    items = orders_df["quantity"].sum()
    items = f"{items:,.0f}"
    st.metric("Items", items)

with ticket_col:
    ticket = orders_df["total_price"].mean()
    ticket = f"{ticket:,.0f}"
    st.metric("Ticket", ticket)

with total_col:
    total = orders_df["total_price"].sum()
    total = f"{total:,.0f}"
    st.metric("Total", total)

vendor_barchat, region_barchat = st.columns(2)

st.header("Charts")
with vendor_barchat:
    st.subheader("Vendors")
    st.bar_chart(orders_df, x="vendor", y="total_price")

with region_barchat:
    st.subheader("Regions")
    st.bar_chart(orders_df, x="region", y="total_price")

st.header("Sales by Date")

orders_df = orders_df.sort_values(by="order_date")
line_df = orders_df.groupby("order_date")["total_price"].sum().reset_index()

st.line_chart(line_df, x="order_date", y="total_price")

st.header("Orders table")

st.dataframe(orders_df)
