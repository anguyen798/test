##
#  Display a bar chart using asterisks.
#

# Define constants.
MAX_STARS = 40

# Read the data values from the user.
values = []
inputStr = input("Enter a value (blank to quit): ")
while inputStr != "" :
   values.append(float(inputStr))
   inputStr = input("Enter a value (blank to quit): ")

# Identify the largest value.
largest = max(values)

# Display the bars.
for i in range(0, len(values)) :
   print("*" * round(values[i] / largest * MAX_STARS))

