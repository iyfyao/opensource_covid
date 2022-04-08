import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

pd.options.display.max_columns = None
url_to_data = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
@st.cache
def load_data():
   data = pd.read_csv(url_to_data)
   return data

df = load_data()


selected_country = st.selectbox(
     'Which country to display?',
     df['location'].unique())



df['MA'] = df['total_cases'].rolling(window=7).mean() #7day Moving Average
df_1 = df.groupby('date').sum().reset_index() #Aggregate by date

fig = plt.figure()

plt.plot(df_1['date'],df_1['total_cases'])
plt.plot(df_1['date'],df_1['total_deaths'])

plt.xticks(rotation=45, ha='right')

st.title('COVID Dashboard : Petar , Maikel , Yao')
plt.xlabel('Date')
plt.ylabel('Total Confirmend Cases')

fig1 = plt.figure()

df_group_by = df.groupby(by=df['location']).sum().reset_index()
df_group_by = df_group_by.loc[df_group_by['location'] == selected_country]
plt.bar(df_group_by['location'], df_group_by['total_cases'])
plt.title('Number of deaths for every country')
plt.xlabel('List of countries')
plt .ylabel('Numer of deaths')
plt.xticks(rotation=45, ha='right')

df_death_per_cases = df[['total_deaths','total_cases','location']]
df_death_per_cases['deaths_per_cases']=df_death_per_cases['total_deaths'] / df_death_per_cases['total_cases']
fig2 = plt.figure()
df_death_per_cases = df_death_per_cases.loc[df_death_per_cases['location'] == selected_country]
plt.bar(df_death_per_cases['location'], df_death_per_cases['deaths_per_cases'])
plt.title('Number of deaths for every country normalized')
plt.xlabel('List of countries')
plt .ylabel('Number of deaths per cases')
plt.xticks(rotation=45, ha='right')



st.pyplot(fig)
st.pyplot(fig1)
st.pyplot(fig2)

st.balloons()


