# simple chatbot for coffee orders

# Define functions
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def iced_or_hot():
  res = input("How would you like your coffee? \n [a] Iced \n [b] Chilled \n [c] Hot \n> ")
  if res == 'a':
    return 'iced'
  elif res == 'b':
    return 'chilled'
  elif res == 'c':
    return 'hot'
  else:
    print_message()
    return iced_or_hot()

def order_latte():
  res = input("And what kind of milk for your latte? \n [a] 2% milk \n [b] Non-fat milk \n [c] Soy milk \n> ")
  if res == 'a':
    return 'latte'
  elif res == 'b': 
    return 'non-fat latte'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()

def get_drink_type():
  res = input("What type of drink would you like?\n [a] Brewed Coffee \n [b] Mocha \n [c] Latte \n> ")
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def get_size():
  res = input("What size drink can I get for you? \n [a] Small \n [b] Medium \n [c] Large \n> ")
  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()

def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  ice_hot = iced_or_hot()
  print("Alright, that's a " + size + " " + drink_type + " and you want it " + ice_hot + "!")
  name = input("Can I get your name please?\n> ")
  print("Thanks, " + name + "! Your drink will be ready shortly.")


# Call coffee_bot()
coffee_bot()
