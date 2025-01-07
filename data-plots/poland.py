import pandas as pd
import matplotlib.pyplot as plt

# Run this file from the root directory of the repository

# Load the data
data = pd.read_csv('./data/Poland.csv')

# Convert the date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Plot total cases and total deaths against time in the first subplot
ax1.plot(data['date'], data['total_cases'], label='Total Cases')
ax1.plot(data['date'], data['total_deaths'], label='Total Deaths', color='red')
ax1.set_yscale('log')
ax1.set_xlabel('Date')
ax1.set_ylabel('Count')
ax1.set_title('Total Cases and Total Deaths in Poland Over Time (Logarithmic Scale)')
ax1.legend()

# Plot new cases and new deaths against time in the second subplot
ax2.scatter(data['date'], data['new_cases'], label='New Cases', s=10)
ax2.scatter(data['date'], data['new_deaths'], label='New Deaths', color='red', s=10)
ax2.set_yscale('log')
ax2.set_xlabel('Date')
ax2.set_ylabel('Count')
ax2.set_title('New Cases and New Deaths in Poland Over Time (Logarithmic Scale)')
ax2.legend()

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()