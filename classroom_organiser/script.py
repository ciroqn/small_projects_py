from roster import student_roster
from classroom_organiser import ClassroomOrganizer
import itertools

student_roster_iter = iter(student_roster)

# for student in student_roster_iter:
#   print(student)

# instantiate class
classroom = ClassroomOrganizer()

# print(classroom.student_combinations())

students_maths = classroom.get_students_with_subject('Math')
students_science = classroom.get_students_with_subject('Science')

# combine above lists
chain_scimath = itertools.chain(students_maths, students_science)

# get only names from list of tuples
chain_scimath_names = [el[0] for el in list(chain_scimath)]

# print(chain_scimath_names)

# get all combos [of 4] 
combos_4 = classroom.student_combinations_4(chain_scimath_names)

print(combos_4)
