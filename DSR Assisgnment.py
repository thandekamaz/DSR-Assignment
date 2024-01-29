
import pandas as pd

print("\nQ2a: ")
df = pd.read_excel('pone.0212445.s004.xlsx', sheet_name='estimates', skiprows=1)

# Filter rows by Estimate == 'Survey'
survey_data = df[df['Estimate'] == 'Survey']

# Calculate the total NoPLHIV for the Survey estimate
total_no_plhiv_survey = survey_data['NoPLHIV'].sum()

print(f'Total number of PLHIV all listed districts according to the Survey estimate: {total_no_plhiv_survey}')

print("\nQ2b: ")
# Filter rows by district == Xhariep
xhariep_data = df[df['District'] == 'Xhariep']

# Calculate the average NoPLHIV for the two estimates
average_no_plhiv = xhariep_data.groupby('Estimate')['NoPLHIV'].mean()

print(f'Average number of PLHIV for Xhariep district:\n{average_no_plhiv}')

print("\nQ2c: ")

# Calculate the total population using NoPLHIV and prev
total_population = df['NoPLHIV'] / (df['Prevalence_%'] / 100)

# Subtract NoPLHIV from total pop to get NoNotHIH
df['NoNotHIV'] = total_population - df['NoPLHIV']

# Convert output from scientific notion to decimal points
pd.set_option('display.float_format', '{:.2f}'.format)

# Display the DataFrame with the new columns
print(df)

# Add the new column to the excel spreadsheet
# df.to_excel('pone.0212445.s004.xlsx', sheet_name='estimates', index=False)

print("\nQ2d: ")

# Filter rows for districts containing "city" or "metro" in the name
city_districts = df[df['District'].str.contains('city|metro', case=False, regex=True)]

# Calculate the total NoPLHIV in all the cities
total_no_plhiv_cities = city_districts['NoPLHIV'].sum()

print(f'Total number of PLHIV in all cities: {total_no_plhiv_cities}')

print("\nQ3: ")

# Replace all special characters with an empty string
df.columns = df.columns.str.replace(r'[^a-zA-Z0-9_ %]', '')

# Print the resultant column names
print(df)
