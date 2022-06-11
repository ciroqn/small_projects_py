# This (basic) program asks the user to input the name of a shape (a circle or triangle). It then calculates the area of that shape.

print "Program is running..."

option = raw_input("Choose a shape: please enter 'C' for circle or 'T' for triangle: ")

if option == 'C':
  radius = float(raw_input('Enter radius in cm: '))
  area = 3.14159 * radius**2
  print area 
elif option == 'T':
  base = float(raw_input('Enter base length in cm: '))
  height = float(raw_input('Enter height in cm: '))
  area = 0.5 * base * height
  print area
else:
  print 'Sorry, this is not a valid shape.'

print 'Exiting program...'


