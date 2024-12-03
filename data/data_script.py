import csv
import pandas as pd
std_labels = ["country","date","total_cases","new_cases","total_deaths","new_deaths","hosp_patients","icu_patients","total_vaccinations","people_vaccinated","new_vaccinations"]
add_labels= ["population", "population_density", "median_age", "hospital_beds_per_thousand", "human_development_index" , "weekly_hosp_admissions", "weekly_icu_admissions", "stringency_index"]
countries = ["Austria", "Luxemburg", "Switzerland","Germany", "Poland", "Lichtenstein"]

# for each line if country==choosen country, select choosen labels and write the columns for them into a new file


#df = pd.read_csv('all_data.csv')

#df.to_csv('your_file_name.csv', index=False)