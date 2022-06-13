"""User gets four guesses at where the battelship might be hidden on a board of 5x5"""


from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))

# Sort guesses into allowed and not allowed etc.
if guess_row == ship_row and guess_col == ship_col:
  print "Congratulations! You sank my battleship!"
else:
  if guess_row not in range(6) or guess_col not in range(6):
    print "Oops, that's not even in the ocean."
  elif board[guess_col-1][guess_row-1] == "X":
    print "You guessed that one already."
  else:
    board[guess_col-1][guess_row-1] = "X"
    print_board(board)
    print "You missed my battelship!"
  
