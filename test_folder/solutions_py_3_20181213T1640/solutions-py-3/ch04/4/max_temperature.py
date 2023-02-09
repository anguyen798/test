##
#  Determine the month with the maximum temperature.
#

# Read the first value from the user.
highestValue = float(input("Enter a temperature: "))
highestMonth = 1

# Read the values for the subsequent months, checking each value to see if it
# is larger than the largest one so far.
for currentMonth in range(2, 13) :
   nextValue = float(input("Enter a temperature: "))
   if nextValue > highestValue :
      highestValue = nextValue
      highestMonth = currentMonth

# Display the result.
print("The month with the highest value is month", highestMonth)

