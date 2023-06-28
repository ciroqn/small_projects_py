# csvs not on GH

# four separate dfs to merge for useful data extraction

import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])


# combine visits and cart using left merge
visits_cart = pd.merge(visits, cart, how='left')

# print(visits_cart)

length_visits_cart = visits_cart.user_id.count()

# print(length_visits_cart)

# number of null value in cart_time
number_null = visits_cart[visits_cart.cart_time.isnull()]

print(number_null.user_id.count())

percentage_nocart = number_null.user_id.count() / float(visits_cart.user_id.count())

print(percentage_nocart)

# left merge for cart and checkout

cart_checkout = pd.merge(cart, checkout, how='left')

# print(cart_checkout)

# percentage who put items in cart but did not checkout
percentage_cart_no_checkout = cart_checkout[cart_checkout.checkout_time.isnull()].user_id.count() / float(cart_checkout.user_id.count())

print(percentage_cart_no_checkout)

# chain all data
all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')

print(all_data.head())

# find percentage of users who proceed to checkout but do not purchase

all_data_checkout_number = all_data[~all_data.checkout_time.isnull()].user_id.count()

all_data_no_purchase_number = all_data[all_data.purchase_time.isnull()].user_id.count()

#print(all_data_checkout_number)
#print(all_data_no_purchase_number)

percentage_did_not_purchase = all_data_checkout_number / all_data_no_purchase_number

# print(percentage_did_not_purchase)

# time from intial visit to final purchase
all_data['avg time'] = all_data.purchase_time - all_data.visit_time

# avg time to purchase
# print(all_data['avg time'].mean())
