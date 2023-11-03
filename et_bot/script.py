# testing an alien bot

"""
Regex patterns used:
r'.*\s*your planet.*' (has to have words 'your planet' in the utterance to trigger the bot's 'describe_planet_intent()' method
r'why are.*' (must start with 'why are')
"""

# importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry", "go away", "go away, please", "kindly go", "scram")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "ciao", "arrivederci")
  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

  def __init__(self):
    
    self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
                        'answer_why_intent': r'why are.*',
                        'cubed_intent': r''
                            }

  # Define .greet() below:
  def greet(self):
    self.name = input("Greetings. What is your name? ")
    # does user want help
    will_help = input(f'Hello {self.name}, I\'m Etcetera. I\'m not from this planet. Will you help me learn about your planet? ')

    # set bot's response to intent
    if will_help in self.negative_responses:
      print("Ok, have a nice Earth day!")
    self.chat()

  # Define .make_exit() here:
  def make_exit(self, reply):
    # check reply is an exit command and act accordingly
    for exit_command in self.exit_commands:
      if reply in exit_command:
        print("Ok, have a nice Earth day!")
        return True

  # Define .chat() next:
  def chat(self):
    # randomly select question for user to answer
    reply = input(random.choice(self.random_questions)).lower()

    # while the make_exit method is False, continue convo
    while not self.make_exit(reply):
      reply = input(self.match_reply(reply))

  # Define .match_reply() below:
  def match_reply(self, reply):
    # match regex pattern with user's reply
    for intent, regex_pattern in self.alienbabble.items():
      found_match = re.match(regex_pattern, reply)

      # match intents and trigger relevant method
      if found_match and intent == 'describe_planet_intent':
        return self.describe_planet_intent()
      elif found_match and intent == 'answer_why_intent':
        return self.answer_why_intent()

  # Define .describe_planet_intent():
  def describe_planet_intent(self):
    responses = ("My planet is a utopia of diverse organisms and species. ", "I am from Opidipus, the capital of the Wayward Galaxies. ")

    # return random choice from tuple
    return random.choice(responses)

  # Define .answer_why_intent():
  def answer_why_intent(self):
    return "Inside .answer_why_intent()"
       
  # Define .cubed_intent():
  def cubed_intent(self, number):
    return "Inside .cubed_intent()"

  # Define .no_match_intent():
  def no_match_intent(self):
    return "Inside .no_match_intent()"

# instance of AlienBot below:
alienBot = AlienBot()

alienBot.greet()
