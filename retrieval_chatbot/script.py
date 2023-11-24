from collections import Counter
from responses import responses, blank_spot
from helper_functions import preprocess, compare_overlap, pos_tag, extract_nouns, compute_similarity
import spacy
word2vec = spacy.load('en')

exit_commands = ("quit", "goodbye", "exit", "no")

class ChatBot:
  
  #define .make_exit() that registers a user's input. if input is exit command, then the program stops:
  def make_exit(self, user_message):
    for exit_command in exit_commands:
      if exit_command in user_message:
        print("Goodbye!")
        return True
    return False

  #define .chat(); if input is not an exit command, the user_message is set to the user's input and it's then passed to another function, repsond(...):
  def chat(self):
    user_message = input("Welcome! What is your question? ")
    while not self.make_exit(user_message):
      user_message = self.respond(user_message)

  #define .find_intent_match():
 
  #define .find_entities():
 
  #define .respond():
  

#initialize ChatBot instance below:
ChatBot = ChatBot()
#call .chat() method below:
ChatBot.chat()
