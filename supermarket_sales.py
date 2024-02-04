import pandas as pd
import streamlit as st
import plotly.express as px



st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout ="wide")

df = pd.read_excel("supermarkt_sales.xlsx",skiprows=2,header=1)


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

df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)

st.dataframe(df_selection)

# Main Page
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# Top KPI's
total_sales = int(df_selection["Total"].sum())
average_rating= round(df_selection["Rating"].mean(),1)
star_rating = ":star:"* int(round(average_rating,0))
average_sales_by_transaction = round(df_selection["Total"].mean(),2)

left_column,middle_column,right_column=st.columns([1,1,1])


with left_column:
    st.subheader("Total_sales :")
    st.markdown(f"**IND ₹{total_sales:,}**")

with middle_column:
    st.subheader("Average Rating :")
    st.markdown(f"**{average_rating}  {star_rating}**")

with right_column:
    st.subheader("Average Sales Per Transaction :")
    st.markdown(f"**IND ₹{average_sales_by_transaction}**")

st.markdown("---")
# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = df_selection.groupby(by=["Product line"])[["Total"]].sum().sort_values(by="Total")
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

st.plotly_chart(fig_product_sales)