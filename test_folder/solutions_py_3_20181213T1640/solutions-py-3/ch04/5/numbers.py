##
#  Compute the average, smallest, largest and range for a series of values
#  entered by the user.  0.0 will be used to mark the end of the input.
#

# Read the first value.
value = float(input("Enter a number (0 to quit): "))

# Initialize the largest and smallest values using the first input.
largest = value
smallest = value
count = 0
total = 0

# Process each value entered, until 0 is read from the user.
while value != 0.0 :
   count = count + 1
   total = total + value

   if value > largest :
      largest = value
   if value < smallest :
      smallest = value

   value = float(input("Enter a number (0 to quit): "))

# Compute and display the results.
if count == 0 :
   print("No values were entered.")
else :
   print("The largest value is:", largest)
   print("The smallest value is:", smallest)
   print("The average of the values is", total / count)
   print("The range of the values is", largest - smallest)

