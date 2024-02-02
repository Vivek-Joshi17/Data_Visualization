import pandas as pd
import streamlit as st
import plotly.express as px



st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout ="wide")

df = pd.read_excel("supermarkt_sales.xlsx",skiprows=2,header=1)
st.dataframe(df)

st.sidebar.header("Filter Here: ")
city = st.sidebar.multiselect(
    "Select the city:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

st.sidebar.header("Filter Here: ")
customer_type = st.sidebar.multiselect(
    "Select customer type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)

st.sidebar.header("Filter Here: ")
gender = st.sidebar.multiselect(
    "Select gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)