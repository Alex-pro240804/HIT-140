import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load datasets
demographics_df = pd.read_csv('dataset1.csv')
screentime_df = pd.read_csv('dataset2.csv')

# Merge the datasets on 'ID'
merged_df = pd.merge(demographics_df, screentime_df, on='ID')


# Calculate Mean, Median, Mode for Weekdays (By Gender)
# Filter by gender
males_df = merged_df[merged_df['gender'] == 1]
females_df = merged_df[merged_df['gender'] == 0]

# Calculate descriptive statistics for males (weekdays)
mean_males = males_df[['C_wk', 'G_wk', 'S_wk', 'T_wk']].mean()
median_males = males_df[['C_wk', 'G_wk', 'S_wk', 'T_wk']].median()
mode_males = males_df[['C_wk', 'G_wk', 'S_wk', 'T_wk']].mode().iloc[0]

# Calculate descriptive statistics for females (weekdays)
mean_females = females_df[['C_wk', 'G_wk', 'S_wk', 'T_wk']].mean()
median_females = females_df[['C_wk', 'G_wk', 'S_wk', 'T_wk']].median()
mode_females = females_df[['C_wk', 'G_wk', 'S_wk', 'T_wk']].mode().iloc[0]

# Display results
print("Males (Weekdays) - Mean:\n", mean_males)
print("Males (Weekdays) - Median:\n", median_males)
print("Males (Weekdays) - Mode:\n", mode_males)

print("Females (Weekdays) - Mean:\n", mean_females)
print("Females (Weekdays) - Median:\n", median_females)
print("Females (Weekdays) - Mode:\n", mode_females)

# Calculate descriptive statistics for males (weekends)
mean_males_we = males_df[['C_we', 'G_we', 'S_we', 'T_we']].mean()
median_males_we = males_df[['C_we', 'G_we', 'S_we', 'T_we']].median()
mode_males_we = males_df[['C_we', 'G_we', 'S_we', 'T_we']].mode().iloc[0]

# Calculate descriptive statistics for females (weekends)
mean_females_we = females_df[['C_we', 'G_we', 'S_we', 'T_we']].mean()
median_females_we = females_df[['C_we', 'G_we', 'S_we', 'T_we']].median()
mode_females_we = females_df[['C_we', 'G_we', 'S_we', 'T_we']].mode().iloc[0]

# Display results
print("Males (Weekends) - Mean:\n", mean_males_we)
print("Males (Weekends) - Median:\n", median_males_we)
print("Males (Weekends) - Mode:\n", mode_males_we)

print("Females (Weekends) - Mean:\n", mean_females_we)
print("Females (Weekends) - Median:\n", median_females_we)
print("Females (Weekends) - Mode:\n", mode_females_we)


# Combine data for comparison
combined_means = pd.DataFrame({
    'Activity': ['Computers', 'Video Games', 'Smartphones', 'TV'],
    'Males_Weekdays': mean_males.values,
    'Females_Weekdays': mean_females.values,
    'Males_Weekends': mean_males_we.values,
    'Females_Weekends': mean_females_we.values
})

# Plot comparison
combined_means.set_index('Activity').plot(kind='bar', figsize=(12, 8))
plt.title('Screen Time Comparison (Weekdays vs Weekends) by Gender')
plt.ylabel('Average Hours per Day')
plt.xticks(rotation=0)
plt.show()
