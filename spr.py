"""This program allows a user to play "scissors, paper, rock" with the computer."""

from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]

# dictionary with messages
message = {
  "tie": "Zzz, it's a tie!",
  "won": "Flip, you won!",
  "lost": "Dang, you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "Your choice is %s" % user_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]

# function that plays the game
def play_RPS():
  user_choice = raw_input("Enter 'Rock', 'Paper' or 'Scissors': ")
  user_choice = user_choice.upper()
  rand_int = randint(0, 2)
  computer_choice = options[rand_int]
  decide_winner(user_choice, computer_choice)

play_RPS()
