import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cpi = pd.read_csv('CPIAUCSL.csv', parse_dates=['observation_date'])
unemp = pd.read_csv('UNRATE.csv', parse_dates=['observation_date'])

df = pd.merge(cpi, unemp, on='observation_date')

df['inflation'] = (df['CPIAUCSL'] / df['CPIAUCSL'].shift(12) - 1) * 100

df = df.dropna()

df = df[df['observation_date'] >= '2000-01-01']

# 画散点图
plt.figure(figsize=(10, 6))
plt.scatter(df['UNRATE'], df['inflation'], s=20, alpha=0.5, color='steelblue')

# 添加趋势线
z = np.polyfit(df['UNRATE'], df['inflation'], 1)
p = np.poly1d(z)
x_trend = np.linspace(df['UNRATE'].min(), df['UNRATE'].max(), 100)
plt.plot(x_trend, p(x_trend), 'r--', alpha=0.8, label=f'Trend line (slope={z[0]:.2f})')

plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Inflation Rate (%)')
plt.title('Phillips Curve (2000-2026)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 打印相关系数
corr = df['UNRATE'].corr(df['inflation'])
print(f'Correlation between unemployment and inflation: {corr:.3f}')
