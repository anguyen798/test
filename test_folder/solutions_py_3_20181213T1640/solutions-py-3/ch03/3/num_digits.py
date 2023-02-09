##
#  Compute and display the number of digits in an integer using if statements.
#

# Read the integer from the user.
num = int(input("Enter an integer: "))

# Make a negative number positive, using an if statement.
if num < 0 :
   num = num * -1

# Determine the number of digits.
if num < 10 :
   digits = 1
elif num < 100 :
   digits = 2
elif num < 1000 :
   digits = 3
elif num < 10000 :
   digits = 4
elif num < 100000 :
   digits = 5
elif num < 1000000 :
   digits = 6
elif num < 10000000 :
   digits = 7
elif num < 100000000 :
   digits = 8
elif num < 1000000000 :
   digits = 9
elif num < 10000000000 :
   digits = 10

# Display the result.
print("The number had", digits, "digits.")

