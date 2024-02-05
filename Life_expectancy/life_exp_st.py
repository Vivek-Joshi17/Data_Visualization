
import pandas as pd 
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Life Expectancy :)",
                   page_icon="chart_with_upwards_trend",
                   layout="wide")

st.header('Life Expectancy Analysis')
st.write(f"In this case study we are going to analyse Life Expectancy Dataset from Kaggle.We are going to compare Male and Female Life expectancy gap in each country with its increase population.")

dataset_link="https://www.kaggle.com/datasets/saimondahal/life-expectancy-trends-for-males-and-females"

st.write(f"Given below is the dataset from the Kaggle ({dataset_link}) on which we are going to work")
life_exp_df=pd.read_csv("life_expectancy.csv")

st.write("\n\n\n")
st.write("")

#Drop Id from the life_exp_dataframe
st.subheader("Dataframe")
life_exp_df=life_exp_df.drop(life_exp_df.columns[0],axis=1)
st.dataframe(life_exp_df)

st.markdown('---')

def individual_(country):
    temp_df=life_exp_df[life_exp_df['Country']==country]
    x_min = temp_df['Population'].min()-100000000
    x_max = temp_df['Population'].max()+100000000

    y_min = temp_df['Life Expectancy Gap'].min()-3
    y_max = temp_df['Life Expectancy Gap'].max()+3

    fig=px.scatter(temp_df,x='Population',y='Life Expectancy Gap',range_x=[x_min,x_max],range_y=[y_min,y_max],size=temp_df['Population'],color='Country',
                   animation_frame='Year',animation_group='Country',title=f"Country's Population vs Life Expectancy Gap")
    
    return fig

figure = individual_('India')
st.plotly_chart(figure)