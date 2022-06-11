# Pig Latin translator

pyg = 'ay'

original = raw_input('Enter a word:')

# Checks input is actually a word (no non-alphabet characters, which is what .isalpha() check for)
if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word[1:len(word)] + first + pyg
  print new_word
else:
  print 'empty'
  
# for example 'Crayfish' becomes 'rayfishcay'
