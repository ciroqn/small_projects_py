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
