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
