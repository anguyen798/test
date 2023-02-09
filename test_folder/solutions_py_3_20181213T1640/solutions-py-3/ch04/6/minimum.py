##
#  Compute the minimum of a set of inputs.
#

# Read the first value from the user.
first = True
inputStr = input("Enter a value (blank line to quit): ")

# Read and process the subseuqent values.
while inputStr != "" :
   value = float(inputStr)
   if first :
      minimum = value
      first = False
   elif value < minimum :
      minimum = value

   inputStr = input("Enter a value (blank line to quit): ")

# If no values were entered then display an appropriate error message.
# Otherwise the minimum value is displayed.
if first :
   print("No values were entered.")
else :
   print("The minimum value is", minimum)

