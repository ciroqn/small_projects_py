import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

files = glob.glob('states*.csv')

df_list = []
for file in files:
  data = pd.read_csv(file)
  df_list.append(data)

us_census = pd.concat(df_list)

print(us_census.head())
print(us_census.columns)
print(us_census.dtypes)

# getting rid of $ in Income column
us_census.Income = us_census['Income'].replace('[\$]', '', regex=True)

# convert to numeric type
us_census.Income = pd.to_numeric(us_census.Income)

# split the 'GenderPop' column
string_split = us_census['GenderPop'].str.split('_')

# create 'Men' column
us_census['Men'] = string_split.str.get(0)

# create 'Women' column
us_census['Women'] = string_split.str.get(1)

# remove the 'M' and 'F' from the Men and Women columns
us_census['Men'] = us_census['Men'].replace('[M]', '', regex=True)

us_census['Women'] = us_census['Women'].replace('[F]', '', regex=True)

# then convert to numeric type
us_census['Men'] = pd.to_numeric(us_census['Men'])

us_census['Women'] = pd.to_numeric(us_census['Women'])

print(us_census.head())
print(us_census.dtypes)

# make scatter plot
plt.scatter(us_census['Women'], us_census['Income'])
plt.show()
plt.close()

print(us_census['Women'])

# replace rows in Women column that have a 'nan' value with the TotalPop minus Men pop.
us_census = us_census.fillna(value={"Women":us_census['TotalPop']-us_census['Men']})

print(us_census['Women'])

# find duplicate values
print(us_census.duplicated())

# drop duplicates
us_census = us_census.drop_duplicates()

# now do another scatter of the results 
plt.scatter(us_census.Women, us_census.Income)
plt.show()
plt.close()

# check columns again to see what race categories there are
print(us_census.columns)

# convert race columns into numeric types (and getting rid of '%')
races = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']

# could use:
# us_census[races] = us_census[races].replace('[\%]', '', regex=True).apply(pd.to_numeric)

for col in us_census.columns:
  if col in races:
    us_census[col] = us_census[col].replace('[\%]', '', regex=True)
    us_census[col] = pd.to_numeric(us_census[col])
    # eliminate any nan values
    us_census = us_census.fillna(value={col:us_census[col].mean()})
    # plot histogram
    plt.hist(us_census[col])
    plt.xlabel(f'{col} pop. %')
    plt.show()
    plt.close()

# check
print(us_census.dtypes)
print(us_census.head())
