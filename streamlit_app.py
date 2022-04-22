import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px
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
     df['location'].unique())
st.write(type(selected_country))
life_death = st.sidebar.selectbox(
     'Cases Or Death?',
     ('Total Death', 'Total Cases'),key=2)

#Condition_country = df.loc[df['location']==selected_country,] #filter by country

df['MA'] = df['total_cases'].rolling(window=7).mean() #7day Moving Average

df_1 = df.groupby('iso_code').sum().reset_index() #Aggregate by country

fig= None
date_start = st.sidebar.date_input('Choose a start date', datetime.date(2011,1,1))
date_end = st.sidebar.date_input('Choose an end date', datetime.date.today())

if life_death == 'Total Death' :
    if len(selected_country) > 0:
            fig = px.line(df[df['location'].isin(selected_country)], x='date', y='total_deaths',range_x = [date_start,date_end])

if life_death == 'Total Cases':
    if len(selected_country) > 0:
            fig = px.line(df[df['location'].isin(selected_country)], x='date', y='total_cases',range_x = [date_start,date_end])

if fig != None:
    st.plotly_chart(fig)

st.balloons()


