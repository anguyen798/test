##
#  Compare two numbers and see if they match up to two decimal places.
#

# Read the numbers from the user.
num1 = float(input("Enter a floating-point number: "))
num2 = float(input("Enter a floating-point number: "))

# Compare the numbers.
if round(num1, 2) == round(num2, 2) :
   print("They are the same up to two decimal places.")
else :
   print("They are different.")

