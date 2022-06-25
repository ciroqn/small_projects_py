# Creating relevant classes for restaurant business and instantiating classes for individual object manipulation

# *still working...


class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  def __repr__(self):
    return "You are looking at the {} menu. The menu is available from {} to {}.".format(self.name, self.start_time, self.end_time)
  def calculate_bill(self, purchased_items):
    total_price = 0
    for item in purchased_items:
      total_price += self.items[item]
    return total_price

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return "The address of our restaurant is: {}".format(self.address)
  def available_menus(self, time):
    # Define list into which results from below are stored
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu.name)
    # Return result based on available_menu list
    if len(available_menu) == None:
      return "Sorry, we're closed"
    else:
      return "The available menus are: \n" + "\n".join(available_menu)

class Business:
  pass

# Instantiate Menu Class - brunch
brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 1100, 1600)

early_bird = Menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 1500, 1800)

dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 1700, 2300)

kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100, 2100)

# Create instance variables for Franchise Class
flagship_store = Franchise("1232 West End Road",[brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# Test __repr__ constructor
#print(kids)

# test calculate_bill method. Note input should have names of items in relevant menu
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

# Test available_menus method in Franchise class
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))
