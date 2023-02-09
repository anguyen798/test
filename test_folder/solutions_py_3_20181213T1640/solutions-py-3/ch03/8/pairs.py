##
#  Determine if four numbers contain two pairs.
#

# Read four numbers from the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))

print(num1, num2, num3, num4, end="")

# Count the pairs.
if num1 == num2 and num3 == num4 :
   print("   two pairs")
elif num1 == num3 and num2 == num4 :
   print("   two pairs")
elif num1 == num4 and num2 == num3 :
   print("   two pairs")
else :
   print("   not two pairs")

