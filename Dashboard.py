import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data_sources/time_series_covid19_confirmed_global.csv')
print(df.iloc[0,700:])
df.iloc[0,700:].plot()
plt.show()