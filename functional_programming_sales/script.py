# creating count() and average() functions to use on dataset

# See CSV for title entries


import csv
from functools import reduce

def count(predicate, iterable):
  # filter iterable according to predicate
  count_filter = filter(predicate, iterable)

  # increase accumulator by 1 if count_filter returns True (initial value is 0)
  count_reduce = reduce(lambda x, y: x+1, count_filter, 0)

  return count_reduce

def avg_helper(curr_count, itr, curr_sum):
  # get next value in iterable; 'null' is default value if not more iterables
  next_num = next(itr, "null")

  # when the iteration is over, next_num will return 'null'. In this case, return average
  if next_num == "null":
    return curr_sum/curr_count

  # add next_num to the current sum
  curr_sum += next_num

  # increment current count by 1
  curr_count += 1

  # recursively call avg_helper with new values if next_num is NOT 'null'
  return avg_helper(curr_count, itr, curr_sum)

def average(itr):
  # If itr is not iterable, this will generate an iterator.  
  iterable = iter(itr) 
  
  # call avg_helper with initial count and initial sum at zero
  return avg_helper(0, iterable, 0)
  

with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  # skips to nxt line in file
  fields = next(reader)
  # get number of entries from Belgium
  count_belgium = count(lambda x: x[1] == "Belgium", reader)
  print(count_belgium)
  csvfile.seek(0)
  # get average total profit from Portugal
  avg_portugal = average(map(lambda x: float(x[13]), filter(lambda x: x[1] == "Portugal", reader)))
  print(avg_portugal)
