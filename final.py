import pandas as pd

df = pd.read_csv('owid-covid-data.csv')



# Check columns
print (df.columns) 

# Preview rows 
print (df.head()) 

# Identify missing values: .
print (df.isnull().sum())






# Load the dataset (replace with your actual file path)
df = pd.read_csv('owid-covid-data.csv')

# Define countries of interest
countries = ['Kenya', 'United States', 'India']  # Use 'United States' for USA in most datasets

# Filter the DataFrame
filtered_df = df[df['location'].isin(countries)]

# Display the filtered data
print(filtered_df.head())


