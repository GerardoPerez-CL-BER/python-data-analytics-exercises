import pandas as pd 
from matplotlib import pyplot as plt
import plotly.express as px

#import csv file and convert it to python list
report = pd.read_csv('self-reported-loneliness-older-adults new.csv')
print(report.head())

#Taking and renaming column
self_reported = report['Self-reported feelings of loneliness among older adults']
siglas = report.siglas

#print(self_reported)
#print(siglas)
#print(report[self_reported > 40])

print(sorted(self_reported, reverse=False))

#Creating line plots
plt.plot(report.country, self_reported)
plt.title('Testing Python')
plt.ylabel('Self-reported Loneliness')
plt.xlabel('Country')
plt.show()

#fig = px.pie(self_reported, names=(report.country), title='Self-reported feelings of loneliness among older adults')
#fig.show()



