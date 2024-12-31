# -*- coding: utf-8 -*-
"""Task_2_Unemployement rate.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17yLk5W7S3v2fAaA_OsIkC9cEPzGghToU
"""

# Commented out IPython magic to ensure Python compatibility.
#Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
# %matplotlib inline

# Read and load data
df = pd.read_csv('/content/drive/MyDrive/CodeAlpha_Internship/Unemployment in India.csv')
df.head()

df.info()

df.columns

#Summary statistics
df.describe()

# Check the null values
df.isnull().sum()

# Drop the null values
df = df.dropna()

df.isnull().sum()

# Check and print duplicated values
print(df.duplicated().sum())

# Print column titles of the data
df.columns

# Remove the space before the column titles
df.columns = df.columns.str.strip()
df

# Print column titles of the data after removing the space
df.columns

# Adding Day, Month, and Year
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = df['Date'].dt.day
df['Month'] = df['Date'].dt.month_name()
df['Year'] = df['Date'].dt.year

# Importing Warnings library
import warnings

# Ignoring unwanted warnings
warnings.filterwarnings("ignore")

df

# Summary statistics
print(df.describe())

# Mean of Unemployment Rate
mean_unemployment = df['Estimated Unemployment Rate (%)'].mean()
print(f'Mean Unemployment Rate: {mean_unemployment:.4f}%')

# Median of Unemployment Rate
median_unemployment = df['Estimated Unemployment Rate (%)'].median()
print(f'Median Unemployment Rate: {median_unemployment:.4f}%')

# Standard deviation of Unemployment Rate
std_unemployment = df['Estimated Unemployment Rate (%)'].std()
print(f'Standard Deviation of Unemployment Rate: {std_unemployment:.4f}%')

# Bar plot for Estimated Unemployment Rate for region
fig = px.bar(df, x = 'Region', y = "Estimated Unemployment Rate (%)", color = "Region", title = "Average unemploment Rate")
fig.update_layout(xaxis = {'categoryorder':'total descending'})
fig.show()

"""The bar graph indicates that the region Tripura have the higest Estimated Unemployment Rate and the region Sikkim indicates have the smallest Estimated Unemployment Rate."""

# Bar plot for Estimated Unemployment Rate for month
fig = px.bar(df, x = 'Month', y = 'Estimated Employed', color = 'Month', title = 'Estimated Employed People')
fig.update_layout(xaxis = {'categoryorder':'total descending'})
fig.show()

"""The bar graph indicates that the month June have the higest Estimated Employed and the region April indicates have the smallest Estimated Employed."""

# Correlation between Estimated Unemployment Rate (%), Estimated Employed, and Estimated Labour Participation Rate (%)
correlation = df[['Estimated Unemployment Rate (%)', 'Estimated Employed', 'Estimated Labour Participation Rate (%)']].corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

"""From the above correlation:
a) There is negative correlation between Estimated Unemployment Rate and Estimated Employed. i.e. r=-0.22.
b) There is no correlation between the Estimated Unemployment Rate and Estimated Labour Participation Rate. i.e. r=0.00.
c) There is weak correlation between the Estimated Employed and Estimated Labour Participation Rate. i.e. r=0.01.
"""

#two sample t test to compare unemployment rate in urban and rural area
from scipy.stats import ttest_ind

urban_unemployment = df[df['Area'] == 'Urban']['Estimated Unemployment Rate (%)']
rural_unemployment = df[df['Area'] == 'Rural']['Estimated Unemployment Rate (%)']

t_stat, p_val = ttest_ind(urban_unemployment, rural_unemployment)
print(f'T-Statistic: {t_stat:.2f}')
print(f'P-Value: {p_val:.2f}')

alpha = 0.05  # Significance level

if p_val < alpha:
    print("Reject the null hypothesis: There is a significant difference between urban and rural unemployment rates.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between urban and rural unemployment rates.")
