import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.title('COVID Dashboard')
df

f1 = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")

f1.head()

st.write(f1.head())

datagraph=f1['total_cases']
st.line_chart(datagraph)
