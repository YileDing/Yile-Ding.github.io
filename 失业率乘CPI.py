import pandas as pd
import matplotlib.pyplot as plt

cpi = pd.read_csv('CPIAUCSL.csv', parse_dates=['observation_date'])
unemp = pd.read_csv('UNRATE.csv', parse_dates=['observation_date'])

df = pd.merge(cpi, unemp, on='observation_date')

df['inflation'] = (df['CPIAUCSL'] / df['CPIAUCSL'].shift(12) - 1) * 100

df['product'] = df['UNRATE'] * df['inflation']

df = df.dropna()

df = df[df['observation_date'] >= '2000-01-01']

plt.figure(figsize=(12, 6))
plt.plot(df['observation_date'], df['product'], color='red', linewidth=1.5)
plt.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
plt.title('Unemployment Rate × Inflation Rate (2000-2026)', fontsize=12)
plt.xlabel('Year')
plt.ylabel('Product (Unemp% × Inf%)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
