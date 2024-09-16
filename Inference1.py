import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.weightstats import ztest

# Load dataset
df1 = pd.read_csv('dataset1.csv')
df2 = pd.read_csv('dataset2.csv')

# Merge datasets on the ID column
df = pd.merge(df1, df2, on="ID")

# Calculate total screen time for the entire week
df['total_screen_time'] = df[['C_we', 'C_wk', 'G_we', 'G_wk', 'S_we', 'S_wk', 'T_we', 'T_wk']].sum(axis=1)

# Separate screen time data by gender (gender: 1 = boys, 0 = girls)
boys_screen_time = df[df['gender'] == 1]['total_screen_time']
girls_screen_time = df[df['gender'] == 0]['total_screen_time']

# 1. Descriptive Statistics
print("Descriptive statistics for Boys:")
print(boys_screen_time.describe())

print("\nDescriptive statistics for Girls:")
print(girls_screen_time.describe())

# 2. Z-Test for Inferential Analysis
z_stat, p_value_z = ztest(boys_screen_time, girls_screen_time)

# Z-Test Results
print(f"\nZ-statistic: {z_stat}")
print(f"P-value: {p_value_z}")

# Conclusion based on p-value
if p_value_z < 0.05:
    print("There is a statistically significant difference between the screen time of boys and girls.")
else:
    print("There is no statistically significant difference between the screen time of boys and girls.")

# 3. Visualization - Bar Chart (Total Screen Time: Boys vs Girls)
total_screen_time_by_gender = df.groupby('gender')['total_screen_time'].sum()

plt.figure(figsize=(8, 6))
total_screen_time_by_gender.plot(kind='bar', color=['pink', 'blue'], legend=False)
plt.title('Total Screen Time Throughout the Week: Boys vs Girls')
plt.ylabel('Total Hours')
plt.xticks(ticks=[0, 1], labels=['Girls', 'Boys'], rotation=0)
plt.show()

# 4. Visualization - Box Plot (Distribution of Total Screen Time by Gender)
plt.figure(figsize=(8, 6))
sns.boxplot(x='gender', y='total_screen_time', data=df, palette=['pink', 'blue'])
plt.title('Screen Time Distribution by Gender')
plt.xlabel('Gender (0=Girls, 1=Boys)')
plt.ylabel('Total Screen Time (hours)')
plt.xticks(ticks=[0, 1], labels=['Girls', 'Boys'])
plt.show()

