import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

pd.options.display.max_columns = None
df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv') #new dataset
df['MA'] = df['total_cases'].rolling(window=7).mean() #7day Moving Average
df_1 = df.groupby('date')['total_cases'].sum().reset_index() #Aggregate by date

fig = plt.figure()

plt.plot(df_1['date'],df_1['total_cases'])
plt.xticks(rotation=45, ha='right')

st.title('COVID Dashboard : Petar , Maikel , Yao')
plt.xlabel('Date')
plt.ylabel('Total Confirmend Cases')
st.pyplot(fig)
st.balloons()


