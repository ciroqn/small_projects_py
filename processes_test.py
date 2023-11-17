"""
Finding the average of lists using four different processes: sequential, async, threading, and multiprocessing. It's expected sequential will take the longest. The `time.sleep(...)` is
used in the cal_average() function to make the timings easier to discern. The average function is different for async because it uses the .sleep() method from asyncio. Output at end of 
file.
"""

import time
import threading
import asyncio
from multiprocessing import Process


def cal_average(num):  # Average function used for sequential programming, threading, and multiprocessing
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  time.sleep(1)
  return avg

def main_sequential(list1, list2, list3):  # Main wrapper for sequential example
  s = time.perf_counter()
  
  # sequential programming calls
  cal_average(list1)
  cal_average(list2)
  cal_average(list3)

  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

async def cal_average_async(num):  # Average function used for asynchronous programming only ( needs await asyncio.sleep() )
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  await asyncio.sleep(1)
  return avg

async def main_async(list1, list2, list3):  # Main wrapper for asynchronous example
  s = time.perf_counter()
  # async programming
  tasks = [cal_average_async(list1), cal_average_async(list2), cal_average_async(list3)]
  await asyncio.gather(*tasks)

  elapsed = time.perf_counter() - s
  print("Asynchronous Programming Elapsed Time: " + str(elapsed) + " seconds")

def main_threading(list1, list2, list3):  # Main wrapper for threading example
  s = time.perf_counter()
  # threading
  lists = [list1, list2, list3]
  threads = []
  for i in range(len(lists)):
    x = threading.Thread(target=cal_average, args=(lists[i],))
    threads.append(x)
    x.start()
  for t in threads:
    t.join()

  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

def main_multiprocessing(list1, list2, list3):  # Main wrapper for multiprocessing example
  s = time.perf_counter()
  # multiprocessing
  lists = [list1, list2, list3]
  processes = [Process(target=cal_average, args=(lists[i],)) for i in range(len(lists))]

  for p in processes:
    p.start()

  for p in processes:
    p.join()

  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")

""" 
EXAMPLE OUTPUT
Sequential Programming Elapsed Time: 3.002541341993492 seconds
Asynchronous Programming Elapsed Time: 1.0012725550041068 seconds
Threading Elapsed Time: 1.0015706840058556 seconds
Multiprocessing Elapsed Time: 1.0041735120030353 seconds
"""

# ------- defining lists for examples and calling functions ----------
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Three lists we are trying to calculate average on
l2 = [2, 4, 6, 8, 10]
l3 = [1, 3, 5, 7, 9, 11]
main_sequential(l1, l2, l3)

# calling async
loop = asyncio.get_event_loop()
loop.run_until_complete(main_async(l1, l2, l3))

# calling other processes
main_threading(l1, l2, l3)
main_multiprocessing(l1, l2, l3)
