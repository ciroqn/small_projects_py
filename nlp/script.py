"""
This script opens a text (text file not in this repo), and the text is tokenised in each sentence (see other file for function).
The part-of-speech tagging 'tags' each word/token (i.e. the grammatical structure), and these tagged words are stored in a list called 'pos_tagged_text'.
Print statements are for checks only. The chunk grammar is defined: here, we look for noun phrases (a determiner, adjective(s), and a noun, in that order) and verb phrases,
which has a noun phrase, verb and adverb. These 'chunk grammars' are parsed using the object's method `.parse()` and the text is looped through to get the grammar
structures.

"""


from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize
from chunk_counters import np_chunk_counter, vp_chunk_counter

# import text 
text = open("text_file.txt", encoding="utf-8").read().lower()

# sentence and word tokenise text here
word_tokenized_text = word_sentence_tokenize(text)

# store and print any word tokenised sentence here
single_word_tokenized_sentence = word_tokenized_text[100]

# visual check
print(single_word_tokenized_sentence)

"""
prints something like:

['he', 'appears', 'as', 'the', 'enunciator', 'of', 'opinions', 'as', 'different', 'in', 'their', 'tone', 'as', 'those', 'of', 'the', 'writers', 'who', 'have', 'handed', 'them', 'down', '.']

"""

# -------- PART-OF-SPEECH TAGGING ---------

# create a list to hold part-of-speech tagged sentences here
pos_tagged_text = list()

# create a for loop through each word tokenised sentence here
for word_token in word_tokenized_text:
  # part-of-speech tag each sentence and append to list of pos-tagged sentences here
  pos_tagged_text.append(pos_tag(word_token))
  
# store and print any part-of-speech tagged sentence here
single_pos_sentence = pos_tagged_text[100]

# visual check
print(single_pos_sentence)

"""
prints something like:

[('he', 'PRP'), ('appears', 'VBZ'), ('as', 'IN'), ('the', 'DT'), ('enunciator', 'NN'), ('of', 'IN'), ('opinions', 'NNS'), ('as', 'IN'), ('different', 'JJ'), ('in', 'IN'), ('their', 'PRP$'), ('tone', 'NN'), ('as', 'IN'), ('those', 'DT'), ('of', 'IN'), ('the', 'DT'), ('writers', 'NNS'), ('who', 'WP'), ('have', 'VBP'), ('handed', 'VBN'), ('them', 'PRP'), ('down', 'RP'), ('.', '.')]

"""


# ----------- CHUNK SENTENCES --------------

# define noun phrase chunk grammar here
np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

# create noun phrase RegexpParser object here
np_chunk_parser = RegexpParser(np_chunk_grammar)

# define verb phrase chunk grammar here
vp_chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"

# create verb phrase RegexpParser object here
vp_chunk_parser = RegexpParser(vp_chunk_grammar)

# create a list to hold noun phrase chunked sentences and a list to hold verb phrase chunked sentences here
np_chunked_text = list()
vp_chunked_text = list()

# create a for loop through each pos-tagged sentence here
for pos_tagged_sentence in pos_tagged_text:
  # chunk each sentence and append to lists here
  np_chunked_text.append(np_chunk_parser.parse(pos_tagged_sentence))
  vp_chunked_text.append(vp_chunk_parser.parse(pos_tagged_sentence))
