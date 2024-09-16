import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.weightstats import ztest


df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')


df = pd.merge(df1, df2, on="ID")


df['total_screen_time'] = df[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].sum(axis=1)


deprived_screen_time = df[df['deprived'] == 1]['total_screen_time']
non_deprived_screen_time = df[df['deprived'] == 0]['total_screen_time']

# Descriptive Statistics by deprivation level
print("Descriptive statistics for Deprived Areas:")
print(deprived_screen_time.describe())

print("\nDescriptive statistics for Non-Deprived Areas:")
print(non_deprived_screen_time.describe())

# 1. Visualization - Bar Chart
avg_screen_time_by_deprivation = df.groupby('deprived')['total_screen_time'].mean()

plt.figure(figsize=(8, 6))
avg_screen_time_by_deprivation.plot(kind='bar', color=['red', 'green'], legend=False)
plt.title('Average Total Screen Time: Deprived vs Non-Deprived Areas')
plt.ylabel('Average Total Screen Time (hours)')
plt.xticks(ticks=[0, 1], labels=['Non-Deprived', 'Deprived'], rotation=0)
plt.show()

# 2. Visualization - Box Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x='deprived', y='total_screen_time', data=df, palette=['green', 'red'])
plt.title('Total Screen Time Distribution: Deprived vs Non-Deprived Areas')
plt.xlabel('Deprivation Level (0 = Non-Deprived, 1 = Deprived)')
plt.ylabel('Total Screen Time (hours)')
plt.xticks(ticks=[0, 1], labels=['Non-Deprived', 'Deprived'])
plt.show()

# 3. Inferential Analysis - Z-Test
z_stat, p_value = ztest(deprived_screen_time, non_deprived_screen_time)

print(f"\nZ-statistic: {z_stat}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("There is a statistically significant difference between the screen time of individuals in deprived vs non-deprived areas.")
else:
    print("There is no statistically significant difference between the screen time of individuals in deprived vs non-deprived areas.")
