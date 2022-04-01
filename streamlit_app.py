import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

df = pd.read_csv('time_series_covid19_confirmed_global.csv')
df
#print(df.iloc[0,700:])
fig = plt.figure()
df.iloc[0,700:].plot()
st.pyplot(fig)
st.balloons()
