import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt

#import datasheet with obesity info
report = pd.read_csv('ObesityDataSet_raw_and_data_sinthetic.csv')
print(report.head())
print(report.info())

#calculate mean from the column weight
weight_mean = np.mean(report['Weight'])
print(weight_mean)

#calculate median from the column weight
weight_median = np.median(report['Weight'])
print(weight_median)

#calculate average weight from male and female and round to 2 decimals
weight_mean_male = round(np.mean(report[report['Gender'] == 'Male']['Weight']), 2)
weight_mean_female = round(np.mean(report[report['Gender'] == 'Female']['Weight']), 2)
print("Average weight male :", weight_mean_male)
print("Average weight female :", weight_mean_female)

#calculate average age from male and female and round to one decimal
avg_age_male = round(np.mean(report[report['Gender'] == 'Male']['Age']), 1)
avg_age_female = round(np.mean(report[report['Gender'] == 'Female']['Age']), 1)
print("The average male age is :", avg_age_male)
print("The average female age is : ", avg_age_female)

#smoker by gender
smk_by_gender = report.groupby('Gender')['SMOKE'].value_counts()
print(smk_by_gender)

#filter by genres
female_smokers = report[(report['Gender'] == 'Female') & (report['SMOKE'] == 'yes')]
print("The amount of female smokers is: ", len(female_smokers))
male_smokers = report[(report['Gender'] == 'Male') & (report['SMOKE'] == 'yes')]
print("The amount of male smokers is: ", len(male_smokers))

#Plot the columns - first filter data by gender
males = report[report['Gender'] == 'Male']
females = report[report['Gender'] == 'Female']

# Plot scatter with different colors
plt.scatter(males['Weight'], males['Height'], alpha=0.3, color='red', label='Male')
plt.scatter(females['Weight'], females['Height'], alpha=0.3, color='blue', label='Female')

# Labels, title, and legend
plt.title("Relation Weight and Height Male and Female")
plt.ylabel("Height")
plt.xlabel("Weight")
plt.legend()

plt.show()