# The Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8, where L is the average number of letters per
# 100 words in the text, and S is the average number of sentences per 100 words in the text.

# Get user text
text = input("Text: ")

# Count of letters, sentences, and words
letter_count = 0
sentence_count = 0
word_count = 1

# Sentence checks
end = ['.', '!', '?']

# Count for above
for i in text:
    if i.isalpha():
        letter_count += 1
    elif i in end:
        sentence_count += 1
    elif i == ' ':
        word_count += 1

# Calculate inputs for C-L index
letters_per_100 = (letter_count / word_count) * 100
sentences_per_100 = (sentence_count / word_count) * 100

# C-L index calc
cli = round(0.0588 * letters_per_100 - 0.296 * sentences_per_100 - 15.8)

# Find grade level
if cli < 1:
    print('Before Grade 1')
elif cli == 1:
    print('Grade 1')
elif cli == 2:
    print('Grade 2')
elif cli == 3:
    print('Grade 3')
elif cli == 4:
    print('Grade 4')
elif cli == 5:
    print('Grade 5')
elif cli == 6:
    print('Grade 6')
elif cli == 7:
    print('Grade 7')
elif cli == 8:
    print('Grade 8')
elif cli == 9:
    print('Grade 9')
elif cli == 10:
    print('Grade 10')
else:
    print('Grade 16+')
