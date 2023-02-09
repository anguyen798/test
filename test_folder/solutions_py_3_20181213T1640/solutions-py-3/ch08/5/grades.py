##
#  Manage student grades.
#

# Use a dictionary to track student grades.
grades = {}

# Loop until the user chooses to quit.
choice = ""
while choice != "Q" :
   choice = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ")
   choice = choice.upper()

   # Handle adding a new student.
   if choice == "A" :
      name = input("Enter the name of the student: ")
      if name in grades :
         print("Sorry, that student is already present.")
      else :
         grade = input("Enter the student's grade: ")
         grades[name] = grade

   # Handle removing a student.
   elif choice == "R" :
      name = input("What student do you want to remove? ")
      if name in grades :
         grades.pop(name)
      else :
         print("Sorry, that student doesn't exist and couldn't be removed.")

   # Handle modifying a student grade.
   elif choice == "M" :
      name = input("Enter the name of the student to modify: ")
      if name in grades :
         print("The old grade is", grades[name])
         grade = input("Enter the new grade: ")
         grades[name] = grade
      else :
         print("Sorry, that student doesn't exist and couldn't be modified.")

   # Handle printing all of the students.
   elif choice == "P" :
      for name in sorted(grades) :
         print("%s: %s" % (name, grades[name]))

   # Handle the case for quiting.
   elif choice == "Q" :
      print("Goodbye!")

   # Handle the case of invalid input.
   else :
      print("Sorry, that wasn't a valid choice.")

