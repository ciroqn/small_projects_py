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

# If number of items in list is greater than n
def more_than_n(lst, item, n):
  num_of_item = lst.count(item)
  if num_of_item > n:
    return True
  else:
    return False

# Add two lists and sort combined list
def combine_sort(lst1, lst2):
  combine_list = lst1 + lst2
  return sorted(combine_list)

# Removing middle part of list (i.e. between start and end parameters)
def remove_middle(lst, start, end):
  length = end - start
  for i in range(length+1):
    lst.pop(start)
  return lst

#... alternatively
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

# Return item1 if frequency in list is more than (or equal to item2)
def more_frequent_item(lst, item1, item2):
  item1_freq = lst.count(item1)
  item2_freq = lst.count(item2)
  if item1_freq >= item2_freq:
    return item1
  else:
    return item2
  
# Double element at index and return list (if index is valid) - it modifies original list
def double_index(lst, index):
  if index <= len(lst)-1:
    lst[index] *= 2
    return lst
  else:
    return lst
  
# Returning item at middle index. If len(list) is even, then the average of the middle two is taken
def middle_element(lst):
  if len(lst) % 2 != 0:
    middle = int((len(lst)-1)/2)
    return lst[middle] 
  else:
    lower = int((len(lst)/2.0) - 0.5)
    upper = int((len(lst)/2.0) + 0.5)
    return int((lst[lower]+lst[upper])/2)

# counts number of items in list that are divisible by 10 
def divisible_by_ten(nums):
  count = 0
  for num in nums:
    if num % 10 == 0:
      count += 1
    else:
      continue
  return count

# Adds items with odd index to new list:
def odd_indices(lst):
  odd_index_list = []
  for index, item in enumerate(lst):
    if index % 2 != 0:
      odd_index_list.append(item)
  return odd_index_list

# function that takes in two lists. First list has each item a power of each number in the second list
def exponents(bases, powers):
  new_list = []
  for base in bases:
    for power in powers:
      new_list.append(base**power)
  return new_list

# takes two lists of numbers, and returns the list with the larger sum. If sums are equal, 'lst1' is returned
def larger_sum(lst1, lst2):
  lst1_sum = 0
  lst2_sum = 0
  for num in lst1:
    lst1_sum += num
  for num in lst2:
    lst2_sum += num
  if max(lst1_sum, lst2_sum) == lst1_sum:
    return lst1
  else:
    return lst2
  
# Has same functionality as max()
def max_num(nums):
  max_val = nums[0]
  for index, num in enumerate(nums):
    if nums[index] > max_val:
      max_val = nums[index]
  return max_val

# Takes two number lists and returns a list of indices which have matching items
def same_values(lst1, lst2):
  common_index_list = []
  for index1, num1 in enumerate(lst1):
    for index2, num2 in enumerate(lst2):
      if num1 == num2 and index1 == index2:
        common_index_list.append(index1)
  return common_index_list

# Takes two lists and returns True if lst1 is the reverse of lst2 (and vice versa)
def reversed_list(lst1, lst2):
  if len(lst1) == len(lst2):
    for index, num in enumerate(lst1):
      if lst1[index] != lst2[-index-1]:
        return False
    return True
  
# Returns list of common letters in two input strings
def common_letters(string_one, string_two):
  common_letterz = []
  for letter1 in string_one:
    for letter2 in string_two:
      if letter1 == letter2:
        if letter1 not in common_letterz:
          common_letterz.append(letter1)
        else:
          continue
  return common_letterz

# Username and password geenrators example based on first and last names
# Takes first three letters of first name and first four letters of last name and concatenates (with exceptions)
def username_generator(first_name, last_name):
  username = ""
  if len(first_name) < 3 or len(last_name) < 4:
    username = first_name + last_name
  first_str = first_name[:3]
  last_str = last_name[:4]
  username = first_str + last_str
  return username

#takes last letter of username and attaches it to beginning of username
def password_generator(username):
  last_letter_username = username[-1]
  password = last_letter_username + username[:-1]
  return password

#reverses the username
def password_generator(username):
  password = ""
  for index, element in enumerate(username):
    password += username[-index-1]
  return password

# Counts number of unique letters in a given word
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  unique = []
  for letter in word:
    if letter in letters:
      if letter not in unique:
        unique.append(letter)
  return len(unique)

# Variation of above - takes word and 'x' (letter that we want counted in word)
def count_char_x(word, x):
  counter = 0
  for letter in word:
    if letter == x:
      counter += 1
  return counter

# Counts how many instances there are of 'x' (which, in this case is a string with len(string) > 1) in 'word'
def count_multi_char_x(word, x):
  list_split = word.split(x)
  num = len(list_split)
  return num - 1

# Function takes word, and two letters ('start' and 'end'). The substring *between* these two indices is returned. If letter not in word, word is returned
def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)
  if start_index == -1 or end_index == -1:
    return word
  substring = word[start_index+1: end_index]
  return substring
