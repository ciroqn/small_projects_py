"""This program prompts the user to guess the total number of a dice rule. If the guess is correct, the user wins! If it's incorrect, the computer wins!"""

from random import randint
from time import sleep

def get_user_guess():
  # get integer guess
  guess = int(raw_input("What's your guess?"))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum value is %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "This value is not allowed..."
  else:
    print "Rolling..."
    # sleep function 'pauses' program for two seconds to simulate rolling dice
    sleep(2)
  print "The first roll is ... %d" % first_roll
  # sleep for one second:
  sleep(1)
  print "The second roll is ... %d" % second_roll
  total_roll = first_roll + second_roll
  print "Result..."
  # sleep for one second:
  sleep(1)
  if guess == total_roll:
    return "Blimey! You won!"
  else:
    return "Ah, crap! You lost!"
    
# Example
print(roll_dice(6))
