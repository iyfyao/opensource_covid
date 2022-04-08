import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.options.display.max_columns = None
df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')
df['MA'] = df['total_cases'].rolling(window=7).mean()
df_1 = df.groupby('date')['total_cases'].sum().reset_index()
plt.plot(df_1['date'],df_1['total_cases'])
plt.xticks(rotation=45, ha='right')
plt.show()
print(df)
