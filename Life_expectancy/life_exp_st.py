
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


left_column,right_column = st.columns(2)
with left_column:
    st.subheader("Dataframe")

with right_column:
    st.subheader("Specification of Datframe")



#Drop Id from the life_exp_dataframe
life_exp_df=life_exp_df.drop(life_exp_df.columns[0],axis=1)



left_column,right_column = st.columns(2)
#for dataframe vizualization 
with left_column:
    #updated dataframe
    st.dataframe(life_exp_df)
#for dataframe specification 
with right_column:
    
    st.write("")# for optimal gap
    #country
    #total number of country present in dataframe
    total_country = life_exp_df.groupby('Country').size().count()
    #total_country = life_exp_df.groupby[]'Country'].nunique()
    st.write(f"Country :- Total number of countries present in the given dataset are {total_country} .")
    
    #Country code
    st.write(f"Country Code :-For uniquely identify country.Same unique values as country i.e. {total_country} .")

    #Year
    min_year=life_exp_df['Year'].min()# minimun year in dataset
    max_year = life_exp_df['Year'].max()# maximun year in dataset
    st.write(f"Year :- The given dataset holds the data from year {min_year} to {max_year} .")

    #Female Life Expectancy 
    min_female_exp = life_exp_df['Female Life Expectancy'].min()#minimum value in Female Life Expectancy column
    max_female_exp = life_exp_df['Female Life Expectancy'].max()#maximum value in Female Life Expectancy column
    st.write(f"Female Life Expectancy  :- The values of this column ranges from {min_female_exp} to { max_female_exp} .")

    #Male Life Expectancy 
    min_male_exp = life_exp_df['Male Life Expectancy'].min()#minimum value in Female Life Expectancy column
    max_male_exp = life_exp_df['Male Life Expectancy'].max()#maximum value in Female Life Expectancy column
    st.write(f"Male Life Expectancy  :- The values of this column ranges from {min_male_exp} to { max_male_exp} .")

    #Population 
    st.write(f"Population  :- This column holds values of countrie's population for each year .")

    #Life Expectancy Gap
    neg_value = life_exp_df.loc[life_exp_df['Life Expectancy Gap'] < 0, 'Life Expectancy Gap'].count()
    pos_value = life_exp_df.loc[life_exp_df['Life Expectancy Gap'] > 0, 'Life Expectancy Gap'].count()
    st.write(f"Life Expectancy Gap :- Life expectancy gap column holds {round(neg_value)} negative value and {round(pos_value)} positive values for {total_country} over the year .")


st.markdown('---')

#Subheading for graph 
st.subheader("Analysing the Population vs Life Expectancy gap of a country ")
st.write("")

# Function which on passing country name returns object fig which holds animated graph of countries life exp gap vs population
def individual_(country):
    temp_df=life_exp_df[life_exp_df['Country']==country]
    x_min = temp_df['Population'].min()-temp_df['Population'].min()/25
    x_max = temp_df['Population'].max()+temp_df['Population'].max()/25

    y_min = temp_df['Life Expectancy Gap'].min()-3
    y_max = temp_df['Life Expectancy Gap'].max()+3

    fig=px.scatter(temp_df,x='Population',y='Life Expectancy Gap',range_x=[x_min,x_max],range_y=[y_min,y_max],size=temp_df['Population'],color='Country',
                   animation_frame='Year',animation_group='Country',title=f"Country's Population vs Life Expectancy Gap")
    
    return fig

unique_country = life_exp_df['Country'].unique()

# Custom CSS to reduce the width of the select box
custom_css = """
    <style>
        div[data-baseweb="select"] {
            max-width: 200px;  
        }
    </style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

left_column,right_column = st.columns(2)

with right_column:
    selected_country=st.selectbox("Select country ",unique_country)
    custom_width = 1000
    custom_height = 1000
    figure = individual_(selected_country)
    st.plotly_chart(figure, use_container_width=False, width=custom_width, height=custom_height)

with left_column:
    st.write("")
    st.markdown(f"##### With the help of this graph we can easily visualize change in the Life expectancy gap with respect to the population over the year .")
    st.write("")
    st.markdown("##### If we take an example of Algeria we can easily see the change in life expectancy gap dering (1950 - 2020). On analysing the graph we observe a sudden decrease in Life Expectancy column around 1955 and again exponential increase in life expectancy gap around 1964 .")


