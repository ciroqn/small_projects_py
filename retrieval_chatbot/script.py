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

  #define .find_intent_match(), which creates a BoW (tokenised) message and creates a dictionary of word frequency. This is done, too, 
  # for the pre-defined messages. Now this is ready for comparing similarities:
  def find_intent_match(self, responses, user_message):
    bow_user_message = Counter(preprocess(user_message))
    processed_responses = [Counter(preprocess(response)) for response in responses]

    # similarity comparison
    similarity_list = [compare_overlap(bow_user_message, processed_response) for processed_response in processed_responses]
    # get index of best-fit response
    response_index = similarity_list.index(max(similarity_list))
    # get response from imported file, which contains pre-defined responses
    return responses[response_index]
 
  #define .find_entities():
  def find_entities(self, user_message):
    # get tags (parts of speech)
    tagged_user_message = pos_tag(preprocess(user_message))
    # get nouns from tagged message (i.e. entities)
    message_nouns = extract_nouns(tagged_user_message)

    # get word2vec model on nouns by calling word2vec on concatenated nouns
    tokens = word2vec(" ".join(message_nouns))
    # get category of blank spot (defined in responses.py)
    category = word2vec(blank_spot)
    # get largest similarity
    word2vec_result = compute_similarity(tokens, category)
    # sort result by score (note: score is at index 2) in ascending order
    word2vec_result.sort(key=lambda x: x[2])
    
    if len(word2vec_result) > 0:
      # return first element of last item
      return word2vec_result[-1][0]
    return blank_spot
 
  #define .respond():
  def respond(self, user_message):
    # get best-fit response from above method
    best_response = self.find_intent_match(responses, user_message)
    print(best_response)
    input_message = input("Do you have another question, mate? ")
    return input_message
  

#initialize ChatBot instance below:
ChatBot = ChatBot()
#call .chat() method below:
ChatBot.chat()
