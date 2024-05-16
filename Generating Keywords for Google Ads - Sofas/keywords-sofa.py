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
    # Loop through words
    for word in words:
        # Append combinations
        keywords_list.append(product + ' ' + word)
        keywords_list.append(word + ' ' + product)
        
# Inspect keyword list
#print(keywords_list)

# Convert the list of lists into a DataFrame
keywords_df = pd.DataFrame(keywords_list, columns=['Keyword'])

# Rename the columns of the DataFrame
def extract_ad_group(keyword):
    for product in sorted(products, key=len, reverse=True): 
        if product.strip() in keyword:  # Strip spaces before comparison
            return product
    return "Other"  # If no product is found (unlikely)
    
keywords_df['Ad Group'] = keywords_df['Keyword'].apply(extract_ad_group)

# Define campaign colum SEM_Sofas
keywords_df['Campaign'] = 'SEM_Sofas'
keywords_df['Criterion Type'] = 'Exact Match'

# Make a copy of the keywords DataFrame into 'phrase' match
keywords_phrase = keywords_df.copy()

# Change criterion type match to phrase
keywords_phrase['Criterion Type'] = 'Phrase'

# Append the DataFrames (combine exact and phrase match)
keywords_df_final = pd.concat([keywords_df, keywords_phrase])

# Reset the index for the final DataFrame
keywords_df_final = keywords_df_final.reset_index(drop=True)

#Reorder the columns
keywords_df_final_r = keywords_df_final[['Campaign', 'Ad Group', 'Keyword', 'Criterion Type']]
print(keywords_df_final_r)

# Export to CSV
keywords_df_final_r.to_csv('keywords_for_sofas.csv', index=False)
print("Keywords exported to keywords_for_sofas.csv")

# View a summary of our campaign work
summary = keywords_df_final_r.groupby(['Ad Group', 'Criterion Type'])['Keyword'].count()
print(summary)
