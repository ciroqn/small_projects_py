letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = {key:value for key, value in zip(letters, points)}

letters_to_points[" "] = 0

#print(letters_to_points)

# How many points does the 'word' get?
def score_word(word):
  point_total = 0
  for letter1 in word:
    for letter2 in letters_to_points.keys():
      if letter1 == letter2:
        point_total += letters_to_points[letter1]
      else:
        point_total += 0
  return point_total

brownie_points = score_word("BROWNIE")

#print(brownie_points)
# prints 15

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNERD": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

# Adds points to relevant player in 'player_to_points' dict
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
  player_to_points[player] = player_points

print(player_to_points)

# prints, for e.g.: {'player1': 29, 'wordNERD': 32, 'Lexi Con': 31, 'Prof Reader': 31}

