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

# bar chart of avg. prices per month

# create axis object
ax = plt.subplot()

# bar height and errs
bar_heights = avg_order.price
bar_errors = std_order.price


plt.bar(range(len(bar_heights)), bar_heights, yerr=bar_errors, capsize=5)
ax.set_xticks(range(len(bar_heights)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.title('Avg. Prices / Month')
plt.xlabel('Month')
plt.ylabel('Avg. Price')
plt.show()
