import pandas as pd
import matplotlib.pyplot as plt

df_rate = pd.read_csv('DFF.csv')
df_unrate = pd.read_csv('UNRATE.csv')
df_cpi = pd.read_csv('CPIAUCSL.csv')

df_rate['observation_date'] = pd.to_datetime(df_rate['observation_date'])
df_unrate['observation_date'] = pd.to_datetime(df_unrate['observation_date'])
df_cpi['observation_date'] = pd.to_datetime(df_cpi['observation_date'])

df_rate = df_rate[(df_rate['observation_date'] >= '2000-01-01') & (df_rate['observation_date'] <= '2020-12-31')]
df_unrate = df_unrate[(df_unrate['observation_date'] >= '2000-01-01') & (df_unrate['observation_date'] <= '2020-12-31')]
df_cpi = df_cpi[(df_cpi['observation_date'] >= '2000-01-01') & (df_cpi['observation_date'] <= '2020-12-31')]

df_cpi['inflation'] = df_cpi['CPIAUCSL'].pct_change(12) * 100

plt.figure(figsize=(14, 6))

plt.plot(df_rate['observation_date'], df_rate['DFF'], linewidth=2, color='darkred', label='Fed Funds Rate')
plt.plot(df_unrate['observation_date'], df_unrate['UNRATE'], linewidth=2, color='steelblue', label='Unemployment Rate')
plt.plot(df_cpi['observation_date'], df_cpi['inflation'], linewidth=2, color='darkorange', label='CPI Inflation')

plt.axvspan(pd.to_datetime('2007-12-01'), pd.to_datetime('2009-06-01'), alpha=0.2, color='gray', label='Financial Crisis')
plt.axvspan(pd.to_datetime('2020-02-01'), pd.to_datetime('2020-04-01'), alpha=0.2, color='lightcoral', label='COVID-19')

plt.title('US Economic Indicators (2000-2020)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage (%)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
