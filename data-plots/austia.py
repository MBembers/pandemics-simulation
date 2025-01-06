import pandas as pd
import matplotlib.pyplot as plt

# Run this file from the root directory of the repository

# Load the data
data = pd.read_csv('Austria.csv')

# Convert the date column to datetime
data['date'] = pd.to_datetime(data['date'])

# Plot Total Cases and Total Deaths Over Time
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['total_cases'], label='Total Cases')
plt.plot(data['date'], data['total_deaths'], label='Total Deaths', color='red')
plt.yscale('log')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Total Cases and Total Deaths in Austria Over Time (Logarithmic Scale)')
plt.legend()
plt.tight_layout()
plt.show()

# Plot New Cases and New Deaths Over Time
plt.figure(figsize=(10, 6))
plt.scatter(data['date'], data['new_cases'], label='New Cases', s=10)
plt.scatter(data['date'], data['new_deaths'], label='New Deaths', color='red', s=10)
plt.yscale('log')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('New Cases and New Deaths in Austria Over Time (Logarithmic Scale)')
plt.legend()
plt.tight_layout()
plt.show()

# Plot Total Number of People Vaccinated and New Vaccinations Over Time
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['people_vaccinated'], label='People Vaccinated')
plt.plot(data['date'], data['new_vaccinations'], label='New Vaccinations', color='red')
plt.yscale('log')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Total Number of People Vaccinated and New Vaccinations in Austria Over Time (Logarithmic Scale)')
plt.legend()
plt.tight_layout()
plt.show()

# Plot Number of Hospitalized Patients and ICU Patients Over Time
plt.figure(figsize=(10, 6))
plt.scatter(data['date'], data['hosp_patients'], label='Number of Hospitalized Patients', s=10)
plt.scatter(data['date'], data['icu_patients'], label='Number of ICU Patients', color='red', s=10)
plt.yscale('log')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Number of Hospitalized Patients and ICU Patients in Austria Over Time (Logarithmic Scale)')
plt.legend()

# New Cases and Total Cases Over Time
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['new_cases'], label='New Cases')
plt.plot(data['date'], data['total_cases'], label='Total Cases', color='red')
plt.yscale('log')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('New Cases and Total Cases in Austria Over Time (Logarithmic Scale)')
plt.legend()
plt.tight_layout()
plt.show()

# New Deaths and Total Deaths Over Time
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['new_deaths'], label='New Deaths')
plt.plot(data['date'], data['total_deaths'], label='Total Deaths', color='red')
plt.yscale('log')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('New Deaths and Total Deaths in Austria Over Time (Logarithmic Scale)')
plt.legend()
plt.tight_layout()
plt.show()

# ICU Patients and New Deaths Over Time
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['icu_patients'], label='ICU Patients', color='blue')
plt.plot(data['date'], data['new_deaths'], label='New Deaths', color='red')
plt.yscale('log')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('ICU Patients and New Deaths in Austria Over Time (Logarithmic Scale)')
plt.legend()

plt.tight_layout()
plt.show()
