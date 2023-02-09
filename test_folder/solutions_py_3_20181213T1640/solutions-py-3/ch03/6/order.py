##
#  Determine if 3 numbers are in increasing order, decreasing order, or 
#  neither.
#
from sys import exit

# Read the mode from the user.
mode = input("Do you want strict or lenient? ")

# Handle an invalid mode in a reasonable way.
if mode != "strict" and mode != "lenient" :
   exit("That wasn't a valid mode!")

# Read three numbers from the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Determine and display their status.
if mode == "strict" :
   # Handle the strict cases.
   if num1 < num2 and num2 < num3 :
      print("They are in increasing order.")
   elif num1 > num2 and num2 > num3 :
      print("They are in decreasing order.")
   else :
      print("They are neither in increasing order nor decreasing order.")
elif mode == "lenient" :
   # Handle the lenient cases.
   if num1 == num2 and num2 == num3 :
      print("They are in both increasing order and decreasing order.")
   elif num1 <= num2 and num2 <= num3 :
      print("They are in increasing order.")
   elif num1 >= num2 and num2 >= num3 :
      print("They are in decreasing order.")
   else :
      print("They are neither in increasing order nor decreasing order.")

