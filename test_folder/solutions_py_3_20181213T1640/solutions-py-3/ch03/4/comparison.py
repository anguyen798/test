##
#  Determine if 3 numers are all the same, all different, or neither.
#

# Read three integers from the user.
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Check if they are all the same, all different, or neither, and display the
# result.
if num1 == num2 and num2 == num3 :
   print("They are all the same.")
elif num1 != num2 and num1 != num3 and num2 != num3 :
   print("They are all different.")
else :
   print("They are neither all the same nor all different.")

