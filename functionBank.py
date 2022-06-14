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
