##
#  Convert a number between 1 and 12 to its month name.
#

# Define constants.
NAMES = "January  February March    April    May      June     July     August   SeptemberOctober  November December "

# Gather input from the user.
num = int(input("Enter a number between 1 and 12: "))

# Generate the month name.
name = NAMES[(num - 1) * 9 : num * 9]
name = name.strip()

# Display the result.
print("Month", num, "is", name)

