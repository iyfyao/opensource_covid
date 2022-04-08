import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px
st.set_page_config(page_title='COVID-19 Dashboard', page_icon=':smiley')

# pd.options.display.max_columns = None
url_to_data = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
@st.cache
def load_data():
   data = pd.read_csv(url_to_data)
   return data

df = load_data()


selected_country = st.multiselect(
     'Which country to display?',
     df['location'].unique())

life_death = st.selectbox(
     'Cases Or Death?',
     ('Total Death', 'Total Cases'),key=2)

df['MA'] = df['total_cases'].rolling(window=7).mean() #7day Moving Average

df_1 = df.groupby('iso_code').sum().reset_index() #Aggregate by country
fig= None
st.write(life_death)
if life_death == 'Total Death' :
    fig = px.line(df, x='date', y='total_deaths')

elif life_death == 'Total Cases' :
    fig = px.line(df, x='date', y='total_cases')
if fig != None:
    st.plotly_chart(fig)

st.balloons()


