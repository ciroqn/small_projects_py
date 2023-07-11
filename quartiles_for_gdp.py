
# quartiles for life expectancy in low- and high-gdp countries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# not available here...
data = pd.read_csv("country_data.csv")

print(data.head())

# isolate life exp. col.
life_expectancy = data["Life Expectancy"]

# quantiles of life exp.
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])

print(life_expectancy_quartiles)

# histogram of life exp.
# plt.hist(life_expectancy)
# plt.show()

# isolate GDP col.
gdp = data["GDP"]

# second quartile or median of GDP
median_gdp = np.median(gdp)

print(median_gdp)

# the rows/countries that have GDP less than or equal to median and greater than the median
low_gdp = data[data["GDP"] <= median_gdp]
high_gdp = data[data["GDP"] > median_gdp]

# quartiles of life exp. in low_gdp countries
low_gdp_quartiles = np.quantile(low_gdp["Life Expectancy"], [0.25, 0.5, 0.75])

print(low_gdp_quartiles)

# quartiles of life exp. in high_gdp countries
high_gdp_quartiles = np.quantile(high_gdp["Life Expectancy"], [0.25, 0.5, 0.75])

print(high_gdp_quartiles)

# histogram comparing life expectancies in low and high gdp countries
plt.hist(high_gdp["Life Expectancy"], alpha=0.2, label="High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha=0.2, label="Low GDP")
plt.legend()
plt.show()
