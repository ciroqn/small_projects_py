# A BankAccount class keeping track of balance, deposits and withdrawals.

class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "%s's balance is %.2f" % (self.name, self.balance)
  def show_balance(self):
    print "Balance: %.2f" % self.balance
  def deposit(self, amount):
    if amount <= 0:
      print "Sorry, you input is invalid."
      return
    else:
      print "Deposit: %.2f" % amount
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount > self.balance:
      print "You cannot withdraw more than you have."
      return
    else:
      print "Amount withdrawn: %.2f" % amount
      self.balance -= amount
      self.show_balance()

# Example tests
my_account = BankAccount("Clint")
print my_account
my_account.show_balance()
my_account.deposit(2500)
my_account.withdraw(1000)
print my_account
