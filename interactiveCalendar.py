"""A calendar that can be edited via the command line. The user can add, update, view and delete events. The basic structure is a 'dictionary'.

Two modules are imported: 1) sleep and 2) strftime. 'sleep' pauses the program for the time indicated in the brackets (in seconds), and 'strftime' allows
one to input all aspects of time (e.g. '%Y' for year, '%S' for seconds etc. using shortcut notation - see docs)."""


from time import sleep, strftime

USER_FIRST_NAME = "John"

# dictionary
calendar = {}

def welcome():
  print 'Welcome ' + USER_FIRST_NAME + "!"
  print 'Calendar is opening...'
  sleep(1)
  print strftime("%a, %b %d %Y")
  print strftime("%H : %M : %S")
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input('Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ')
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "The calendar is empty"
      else:
        print calendar
    elif user_choice == 'U':
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "The update was successful."
      print calendar
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print "Sorry, input is invalid."
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "The update was successful."
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print "The calendar is empty."
      else:
        event = "What event? "
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "Event was successfully deleted."
          else:
            print "You have entered an incorrect event."
    elif user_choice == 'X':
      start = False
    else:
      print "You entered an invalid command."
      start = False

       
start_calendar()
