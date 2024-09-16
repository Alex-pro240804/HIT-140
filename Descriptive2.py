import pandas as pd
import matplotlib.pyplot as plt

demographics_df = pd.read_csv('dataset1.csv')
screentime_df = pd.read_csv('dataset2.csv')
merged_df = pd.merge(demographics_df, screentime_df, on='ID')


deprived = merged_df[merged_df['deprived'] == 1]
non_deprived = merged_df[merged_df['deprived'] == 0]


mean_deprived_weekdays = deprived[['C_wk', 'G_wk', 'S_wk', 'T_wk']].mean()
median_deprived_weekdays = deprived[['C_wk', 'G_wk', 'S_wk', 'T_wk']].median()
mode_deprived_weekdays = deprived[['C_wk', 'G_wk', 'S_wk', 'T_wk']].mode().iloc[0]

mean_non_deprived_weekdays = non_deprived[['C_wk', 'G_wk', 'S_wk', 'T_wk']].mean()
median_non_deprived_weekdays = non_deprived[['C_wk', 'G_wk', 'S_wk', 'T_wk']].median()
mode_non_deprived_weekdays = non_deprived[['C_wk', 'G_wk', 'S_wk', 'T_wk']].mode().iloc[0]


mean_deprived_weekends = deprived[['C_we', 'G_we', 'S_we', 'T_we']].mean()
median_deprived_weekends = deprived[['C_we', 'G_we', 'S_we', 'T_we']].median()
mode_deprived_weekends = deprived[['C_we', 'G_we', 'S_we', 'T_we']].mode().iloc[0]

mean_non_deprived_weekends = non_deprived[['C_we', 'G_we', 'S_we', 'T_we']].mean()
median_non_deprived_weekends = non_deprived[['C_we', 'G_we', 'S_we', 'T_we']].median()
mode_non_deprived_weekends = non_deprived[['C_we', 'G_we', 'S_we', 'T_we']].mode().iloc[0]

# Create DataFrame to compare the mean screen time for both groups on weekdays and weekends (Mean Only)
weekdays_comparison_mean = pd.DataFrame({
    'Activity': ['Computers (Weekdays)', 'Video Games (Weekdays)', 'Smartphones (Weekdays)', 'TV (Weekdays)'],
    'Deprived Mean': mean_deprived_weekdays.values,
    'Non-Deprived Mean': mean_non_deprived_weekdays.values
})

weekends_comparison_mean = pd.DataFrame({
    'Activity': ['Computers (Weekends)', 'Video Games (Weekends)', 'Smartphones (Weekends)', 'TV (Weekends)'],
    'Deprived Mean': mean_deprived_weekends.values,
    'Non-Deprived Mean': mean_non_deprived_weekends.values
})

# Plotting the means for weekdays
weekdays_comparison_mean.set_index('Activity').plot(kind='bar', figsize=(10, 6), color=['skyblue', 'salmon'])
plt.title('Screen Time on Weekdays: Deprived vs Non-Deprived (Mean Only)')
plt.ylabel('Average Hours per Day')
plt.xticks(rotation=0)
plt.show()

# Plotting the means for weekends
weekends_comparison_mean.set_index('Activity').plot(kind='bar', figsize=(10, 6), color=['lightgreen', 'lightcoral'])
plt.title('Screen Time on Weekends: Deprived vs Non-Deprived (Mean Only)')
plt.ylabel('Average Hours per Day')
plt.xticks(rotation=0)
plt.show()

# Displaying the calculated statistics (Mean, Median, Mode) for both groups
print("Weekdays Screen Time (Deprived vs Non-Deprived):")
print(weekdays_comparison_mean)

print("\nWeekends Screen Time (Deprived vs Non-Deprived):")
print(weekends_comparison_mean)
