import re
from collections import Counter
import spacy
word2vec = spacy.load('en')
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))

# takes in (sentence) string and tokenises it. It excises all the stop words from the sentence for deeper and more efficient analysis
def preprocess(input_sentence):
    input_sentence = input_sentence.lower()
    input_sentence = re.sub(r'[^\w\s]','',input_sentence)
    tokens = word_tokenize(input_sentence)
    input_sentence = [i for i in tokens if not i in stop_words]
    return(input_sentence)

# takes in user message and a possivle response that a bot will send the user. It counts the number of similar (shared words) and returns the number of similar words
def compare_overlap(user_message, possible_response):
    similar_words = 0
    for token in user_message:
        if token in possible_response:
              similar_words += 1
    return similar_words

# tags a message, with each word (token) having its part of speech stored in a tuple e.g. ('city', 'NN'). This function appends the nouns in a new list. Nouns are 'entities' and 
# are important to understanding the context of a user's message.
def extract_nouns(tagged_message):
    message_nouns = list()
    for token in tagged_message:
        if token[1].startswith("N"):
            message_nouns.append(token[0])
    return message_nouns

# prints a list with each element containing a word/token in the user message, followed by the category relevant to what the chatbot wants to send, and the similarity, given between 
# 0 and 1. The greater the similarity, the higher this number is. e.g. ['t-shirt', 'clothing', 0.56443543]. The 'category' may be a blank spot in a pre-defined message that is filled by
# an entity.
def compute_similarity(tokens, category):
    output_list = list()
    for token in tokens:
        output_list.append([token.text, category.text, token.similarity(category)])
    return output_list
  
