# Get credit card number
number = ''

# Ask question till user inputs a number
while not number.isnumeric():
    number = input("Number: ")

# Convert number to list
number = list(number)

# Convert each element in list to int type
for i in range(len(number)):
    number[i] = int(number[i])

# Get copy of number list for later calcs
original_list = number.copy()

# Set up vars for algo
doubled_sum = 0
non_doubled_sum = 0

# Double every other number, starting from the penultimate num
# and add doubled nums together
for i in range(len(number) - 2, -1, -2):
    number[i] *= 2
    if number[i] > 9:
        doubled_sum += (number[i] - 9)
    else:
        doubled_sum += number[i]

# Add nums that were not doubled
for i in range(len(number) - 1, -1, -2):
    non_doubled_sum += number[i]

# Get sum of these to see if card if valid (superficially)
total_sum = doubled_sum + non_doubled_sum

# Convert list of nums to string [of numbers]
original_list = ''.join([str(i) for i in original_list])

# Check card company
if total_sum % 10 == 0:
    if len(number) == 15 and (original_list[:2] == '34' or original_list[:2] == '37'):
        print("AMEX")
    elif len(number) == 16 and (original_list[:2] == '51' or original_list[:2] == '52' or original_list[:2] == '53' or original_list[:2] == '54' or original_list[:2] == '55'):
        print("MASTERCARD")
    elif (len(number) == 13 or len(number) == 16) and (original_list[0] == '4'):
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")
