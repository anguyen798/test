##
#  Display a description of a number.
#

# Read the number from the user.
num = float(input("Enter a number: "))

# Display the result.
if num == 0.0 :
   print("zero")
else :
   # Display the prefix, if needed.
   if abs(num) > 1000000 :
      print("large ", end="")
   elif abs(num) < 1 :
      print("small ", end="")
   
   # Display positive or negative.
   if num > 0 :
      print("positive")
   else :
      print("negative")

