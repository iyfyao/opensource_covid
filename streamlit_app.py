import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px
import datetime
st.set_page_config(page_title='COVID-19 Dashboard', page_icon=':smiley')

# pd.options.display.max_columns = None
url_to_data = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
@st.cache(allow_output_mutation=True)
def load_data():
   data = pd.read_csv(url_to_data)
   return data

df = load_data()

st.title('Dashboard Project by MPY')

selected_country = st.sidebar.multiselect(
     'Which country to display?',
     df['location'].unique(),  default=["France"])
life_death = st.sidebar.selectbox(
     'Cases Or Death?',
     ('Total Death', 'Total Cases'),key=2)

cumelative_smooth = st.sidebar.selectbox(
     'Type of Data?',
     ('Cumelative Cases', 'Cumelative Deaths' , 'New Cases Smoothed','New Death Smoothed'),key=3)

#Condition_country = df.loc[df['location']==selected_country,] #filter by country

df['MA'] = df['total_cases'].rolling(window=7).mean() #7day Moving Average

df_1 = df.groupby('iso_code').sum().reset_index() #Aggregate by country

fig= None
date_start = st.sidebar.date_input('Choose a start date', datetime.date(2020,1,1))
date_end = st.sidebar.date_input('Choose an end date', datetime.date.today()-datetime.timedelta(days=1))

if life_death == 'Total Death' :
    if len(selected_country) > 0:
        if cumelative_smooth == 'Cumelative Deaths':
            fig = px.line(df[df['location'].isin(selected_country)], x='date', y='total_deaths',range_x = [date_start,date_end], color = 'location',labels = {"total_deaths" : "Total death Per Million",  "location" : "Country name"}, title = "Total number of cases Line plot")
        if cumelative_smooth == 'New Death Smoothed':
            fig = px.line(df[df['location'].isin(selected_country)], x='date', y='new_deaths_smoothed_per_million',range_x = [date_start,date_end], color = 'location',labels = {"total_deaths" : "Total death Per Million",  "location" : "Country name"}, title = "Total number of cases Line plot")
        else:
            fig = px.line(df[df['location'].isin(selected_country)], x='date', y='total_deaths',range_x = [date_start,date_end], color = 'location',labels = {"total_deaths" : "Total death Per Million",  "location" : "Country name"}, title = "Total number of cases Line plot")

            
if life_death == 'Total Cases':
    if len(selected_country) > 0:
            fig = px.line(df[df['location'].isin(selected_country)], x='date', y='total_cases',range_x = [date_start,date_end], color = 'location',labels = {"total_deaths" : "Total death Per Million",  "location" : "Country name"}, title = "Total number of cases Line plot")

if fig != None:
    st.plotly_chart(fig)

st.balloons()


