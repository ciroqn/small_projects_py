# Miscellaneous functions in Python

# Reverse text
def reverse(text):
  reverse = []
  count = len(text)
  while count > 0:
    index = text[count-1]
    reverse.append(index)
    count -= 1
  return ''.join(reverse)

# Excise vowels from text
def anti_vowel(text):
  vowels = 'aeiouAEIOU'
  result = ''
  for char in text:
    if char not in vowels:
      result += char   
  return result

# Scrabble scores - matches letter to correpsonding letter in 'scores' and adds up points. E.g. 'zebra' will return 16.
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
  sum = 0
  lower = word.lower()
  print lower
  for char in lower:
    for key in score:
      if char == key:
        sum += score[key]
  return sum

# Censor word from text (does not account for puncutation). 
def censor(text, word):
  list = text.split(" ")
  for indx, x in enumerate(list):
    if x == word:
      list[indx] = '*'*len(word)
  return " ".join(list)
  print " ".join(list)

censor("this is absolute baloney", "baloney") # prints: 'this is absolute *******'

# Counts how many times a number occurs in a sequence
def count(sequence, item):
  count = 0
  for num in sequence:
    if num == item:
      count += 1
  return count

# Returns product of all the numbers in a list
def product(list):
  product = 1
  for num in list:
    product *= num
  return product

# Removes odd numbers from sequence
def purify(numbers_list):
  pure_list = []
  for num in numbers_list:
    if num % 2 == 0:
      pure_list.append(num)
  return pure_list

# Remove duplicate numbers in number list
def remove_duplicates(list):
  new_list = []
  for num in list:
    if num not in new_list:
      new_list.append(num)
  return new_list

# Finding median of list (note to self: divide by 2.0 to give a float)
import math
def median(list):
  sort = sorted(list)
  print sort
  length = len(sort)
  if length % 2 != 0:
    indx_num = (length-1)/2
    return sort[indx_num]
  else:
    indx_higher = (length)/2 
    indx_lower = indx_higher - 1
    avg = (sort[indx_lower]+sort[indx_higher]) / 2.0
    return avg

# Add last two numbers in list and append to list and repeat three times
def append_sum(lst):
  for i in range(3):
    add_last_two = lst[-1]+lst[-2]
    lst.append(add_last_two)
  return lst
