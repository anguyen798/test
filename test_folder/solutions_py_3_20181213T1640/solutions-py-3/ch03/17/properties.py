##
#  Check several properties of a string.
#

# Read input from the user.
string = input("Enter a string: ")

# Check each property and display a message if that property is present.
if string.isalpha() :
   print("The string contains only letters.")

if string.isupper() :
   print("All letters in the string are uppercase letters.")

if string.islower() :
   print("All letters in the string are lowercase letters.")

if string.isdigit() :
   print("The string contains only digits.")

if string.isalnum() :
   print("The string contains only letters and digits.")

if string[0] >= "A" and string[0] <= "Z" :
   print("The string starts with an uppercase letter.")

if string.endswith(".") :
   print("The string ends with a period.")

