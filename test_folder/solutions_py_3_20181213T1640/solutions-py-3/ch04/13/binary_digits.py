##
#  Compute and display the binary digits for an integer.
#

# Read an integer from the user.
value = int(input("Enter an integer: "))

# Generate and display its binary digits.
while value > 0 :
   print(value % 2)
   value = value // 2

