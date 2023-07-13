from matplotlib import pyplot as plt
import pandas as pd

# data not available here
restaurants = pd.read_csv('restaurants.csv')

cuisine_counts = restaurants.groupby('cuisine')\
                            .name.count()\
                            .reset_index()

cuisines = cuisine_counts.cuisine.values

counts = cuisine_counts.name.values

plt.pie(counts, labels=['American', 'Chinese', 'Italian', 'Japanese', 'Korean', 'Pizza', 'Vegetarian'], autopct='%d%%')
plt.title('Most Popular Cuisine Among FoodWheel Partner Restaurants')
plt.axis('equal')
plt.show()

# data for orders
orders = pd.read_csv('orders.csv', delimiter=',')

print(orders.head())

# new column with month
orders['month'] = orders.date.apply(lambda x: x.split('-')[0])

# avg price for each month
avg_order = orders.groupby('month').price.mean().reset_index()

print(avg_order)

# std of price for each month
std_order = orders.groupby('month').price.std().reset_index()
