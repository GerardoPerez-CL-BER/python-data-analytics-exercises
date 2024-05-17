import numpy as np 
import pandas as pd

# Products
products = ['sofas', 'convertible sofas', 'love seats', 'recliners', 'sofa beds']
# Words to modify product terms
words = ['buy', 'shop', 'order', 'purchase', 'cheap', 'affordable', 'discount', 'deal', 'offer', 'promotion']

# Create an empty list
keywords_list = []

# Loop through products
for product in products:
    for word in words:
        keywords_list.append([product, product + ' ' + word])
        
# Inspect keyword list
from pprint import pprint
pprint(keywords_list)

# Create a DataFrame from list
keywords_df = pd.DataFrame.from_records(keywords_list)

# Rename the columns of the DataFrame
keywords_df = keywords_df.rename(columns={0: 'Ad Group', 1: 'Keyword'})

# Define campaign colum SEM_Sofas
keywords_df['Campaign'] = 'SEM_Sofas'
keywords_df['Criterion Type'] = 'Exact'

# Make a copy of the keywords DataFrame
keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase
keywords_phrase['Criterion Type'] = 'Phrase'

# Append the DataFrames
keywords_df_final = pd.concat([keywords_df, keywords_phrase])

# Save the final keywords to a CSV file
keywords_df_final.to_csv('final_keywords.csv', index=False)

# View a summary of our campaign work
summary = keywords_df_final.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)
