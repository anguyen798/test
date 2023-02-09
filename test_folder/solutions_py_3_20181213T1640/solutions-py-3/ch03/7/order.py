##
#  Determine whether or not 3 numbers are in order.
#

# Read three numbers from the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Determine and display their status.
if num1 <= num2 and num2 <= num3 or num1 >= num2 and num2 >= num3 :
   print(num1, num2, num3, "  in order")
else :
   print(num1, num2, num3, "  not in order")

