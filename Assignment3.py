import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

demographic_df = pd.read_csv('dataset1.csv')  # Demographic data
screen_time_df = pd.read_csv('dataset2.csv')  # Screen time data
wellbeing_df = pd.read_csv('dataset3.csv')    # Well-being data

wellbeing_indicators = ['Optm', 'Usef', 'Relx', 'Engs', 'Conf', 'Dealpr',
                        'Thcklr', 'Goodme', 'Clsep', 'Mkmind', 'Loved', 'Intthg', 'Cheer']
wellbeing_df['combined_wellbeing_score'] = wellbeing_df[wellbeing_indicators].mean(
    axis=1)

merged_df = pd.merge(pd.merge(screen_time_df, wellbeing_df[[
                     'ID', 'combined_wellbeing_score']], on='ID'), demographic_df, on='ID')

merged_df['total_weekend_screen_time'] = merged_df[[
    'C_we', 'G_we', 'S_we', 'T_we']].sum(axis=1)
merged_df['total_weekday_screen_time'] = merged_df[[
    'C_wk', 'G_wk', 'S_wk', 'T_wk']].sum(axis=1)


merged_df['total_screen_time'] = merged_df['total_weekend_screen_time'] + \
    merged_df['total_weekday_screen_time']

# Prepare the data for linear regression
X = merged_df[['total_screen_time']]
y = merged_df['combined_wellbeing_score']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict well-being scores on the test set
y_pred = model.predict(X_test)

# Evaluate the model using MSE and R-Squared
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-Squared: {r2}")

# Visualize the regression line on the scatter plot
sns.regplot(x='total_screen_time', y='combined_wellbeing_score',
            data=merged_df, scatter_kws={'s': 10}, line_kws={'color': 'red'})
plt.title('Regression Line: Total Screen Time vs Well-Being Score')
plt.xlabel('Total Screen Time (hours)')
plt.ylabel('Combined Well-Being Score')
plt.show()

#  Print the model coefficients
print(f"Intercept: {model.intercept_}")
print(f"Coefficient for Screen Time: {model.coef_[0]}")

# Create a correlation matrix for relevant columns
correlation_columns = ['total_screen_time', 'combined_wellbeing_score',
                       'total_weekend_screen_time', 'total_weekday_screen_time']
correlation_matrix = merged_df[correlation_columns].corr()

# Create a correlation matrix for all numeric columns in the merged dataset
correlation_matrix_full = merged_df.corr()

# Plot the full correlation heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix_full, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Full Correlation Heatmap: All Numeric Variables')
plt.show()

