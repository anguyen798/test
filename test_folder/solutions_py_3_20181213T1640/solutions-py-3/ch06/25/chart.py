##
#  Display a bar chart using asterisks.
#

# Define constants.
MAX_STARS = 40
MIN_STARS = 5

# Read the data values from the user.
values = []
inputStr = input("Enter a value (blank to quit): ")
while inputStr != "" :
   values.append(float(inputStr))
   inputStr = input("Enter a value (blank to quit): ")

# Identify the largest value, smallest value, and spread.
largest = max(values)
smallest = min(values)
spread = largest - smallest

# Display the bars.
for i in range(0, len(values)) :
   print("*" * (MIN_STARS + round((values[i] - smallest) / spread * (MAX_STARS - MIN_STARS))))

