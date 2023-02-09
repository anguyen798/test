##
#  Determine which of three values is largest.
#

# Read the numbers from the user.
num1 = float(input("Enter a number: "))
num2 = float(input("Enter a number: "))
num3 = float(input("Enter a number: "))

# Find the largest number.
if num1 >= num2 and num1 >= num3 :
   largest = num1
elif num2 >= num1 and num2 >= num3 :
   largest = num2
else :
   largest = num3

# Display the largest value.
print("The largest number is", largest)
  

