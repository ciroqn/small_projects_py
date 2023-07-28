import random
import logging
import sys
from datetime import datetime

# create logger object
logger = logging.getLogger(__name__)

# direct messages to console
stream_handler = logging.StreamHandler(sys.stdout)

# create formatter object
formatter = logging.Formatter("[%(asctime)s] %(levelname)s:%(name)s:%(message)s")

# set format to stream handler object
stream_handler.setFormatter(formatter)

# add stream handler to logger object
logger.addHandler(stream_handler)

# set min level of logger that show messages (i.e. INFO and above)
logger.setLevel(logging.INFO)

# create file handler object
file_handler = logging.FileHandler("formatted.log")

# add file handler to logger object
logger.addHandler(file_handler)

class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    
  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
      if pin != 1234:
        logger.error("Error! Invalid pin.")
        pin = int(input("\nTry again: "))
      else:
        return None
 
  def deposit(self):
    try:
      amount=float(input("Enter amount to be deposited: "))
      if amount < 0:
        logger.warning("Warning! You entered a negative number to deposit.")
      self.balance += amount
      logger.info("Amount Deposited: ${amount}".format(amount=amount))
      logger.info("Transaction Info:")
      logger.info("Status: Successful")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.debug("Timestamp: {timestamp}".format(timestamp=datetime.now()))
    except ValueError:
      logger.error("Error! You entered a non-number value to deposit.")
      logger.info("Transaction Info:")
      logger.info("Status: Failed")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def withdraw(self):
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      if self.balance >= amount:
        self.balance -= amount
        logger.info("You withdrew: ${amount}".format( amount=amount))
        logger.info("Transaction Info:")
        logger.info("Status: Successful")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      else:
        logger.error("Error! Insufficient balance to complete withdraw.")
        logger.info("Transaction Info:")
        logger.info("Status: Failed")
        logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.error("Error! You entered a non-number value to withdraw.")
      logger.info("Transaction Info:")
      logger.info("Status: Failed")
      logger.info("Transaction #{number}".format(number=random.randint(10000, 1000000)))
      logger.info("Timestamp: {timestamp}".format(timestamp=datetime.now()))
 
  def display(self):
    print("Available Balance = ${balance}".format(balance=self.balance))
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()
