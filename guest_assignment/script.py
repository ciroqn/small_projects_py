# Reading from file and returning guest name and age. Creating menus, table #s and seat #s and assign a guest to each one using generators

guests = {}
def read_guestlist(file_name):
  text_file = open(file_name,'r')
  n = None
  while True:
    if n is not None:
      line_data = n.strip().split(",")
    else:
      line_data = text_file.readline().strip().split(",")
    if len(line_data) < 2:
    # If no more lines, close file
      text_file.close()
      break
    name = line_data[0]
    age = int(line_data[1])
    guests[name] = age
    n = yield name, age

# Insantiating generator
guestlist = read_guestlist("guest_list.txt")

# Printing first 10 guests
for i in range(10):
  print(next(guestlist))

# Adding Jane,35 to guestlist
print(guestlist.send("Jane,35"))

# Getting rest of guests
print(next(guestlist))
print(next(guestlist))
print(next(guestlist))
print(next(guestlist))

# Getting all guests who are 21 and over
over_21 = (name for name, age in guests.items() if age >= 21)

# Let's see if names are correct
print(list(over_21))

def Table1(meal):
  for i in range(1,6):
    yield meal, 'Table 1', "Seat " + str(i)

def Table2(meal):
  for i in range(1,6):
    yield meal, 'Table 2', "Seat " + str(i)

def Table3(meal):
  for i in range(1,6):
    yield meal, 'Table 3', "Seat " + str(i)

# Insantiating menus to create iterator
table1 = Table1("Chicken")
table2 = Table2("Beef")
table3 = Table3("Fish")

for seat in table1:
  print(seat)

for seat in table2:
  print(seat)

for seat in table3:
  print(seat)
  
# Connector generator
def Table():
  yield from Table1("Chicken")
  yield from Table2("Beef")
  yield from Table3("Fish")

# Assign table and seat to each guest
def assign_table(guest_list, table):
  yield list(zip(guest_list, table))

assign = assign_table(guests, Table())

for assignment in assign:
  print(assignment)
  print('\n')
