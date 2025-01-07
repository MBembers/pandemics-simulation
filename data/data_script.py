import csv
import pandas as pd
std_labels = ['country','date','total_cases','new_cases','total_deaths','new_deaths','hosp_patients','icu_patients','total_vaccinations','people_vaccinated','new_vaccinations']
additional_labels= ['population', 'population_density', 'median_age', 'hospital_beds_per_thousand', 'human_development_index' , 'weekly_hosp_admissions', 'weekly_icu_admissions', 'stringency_index']
countries = ['Austria','Luxembourg', 'Switzerland','Germany', 'Poland', 'Liechtenstein']

# for each line if country==choosen country, select choosen labels and write the columns for them into a new file
#read csv as a pandas dataframe
df = pd.read_csv('raw_data/all_data.csv')
#copy to the new df only important columns
df = df[std_labels].copy()
#creating new file for each country
for countryname in countries:

    new_df = df.loc[df['country'] == countryname]
    if len(new_df.index) !=0:
        new_df.to_csv(countryname+'.csv', index=False)
    else:
        print("No data for ", countryname)

