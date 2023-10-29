# This takes in text and tokenises by sentence. The imported object has a method called '.tokenize()' that does just this.
# The loop goes through each sentence and isolates the words in the sentence. This prepares for the next stage of 'chunking' i.e. finding word structures useful for analyses.
# Note American spelling

from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

def word_sentence_tokenize(text):
  
  # create a PunktSentenceTokenizer
  sentence_tokenizer = PunktSentenceTokenizer(text)
  
  # sentence tokenise text
  sentence_tokenized = sentence_tokenizer.tokenize(text)
  
  # create a list to hold word tokenised sentences
  word_tokenized = list()
  
  # for-loop through each tokenised sentence in sentence_tokenized
  for tokenized_sentence in sentence_tokenized:
    # word tokenize each sentence and append to word_tokenized
    word_tokenized.append(word_tokenize(tokenized_sentence))
    
  return word_tokenized
