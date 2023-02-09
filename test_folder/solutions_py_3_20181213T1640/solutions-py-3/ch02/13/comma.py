##
#  Read a number between 10,000 and 99,999.  Display it without the comma.
#

# Gather input from the user.
numStr = input("Please enter a number between 10,000 and 99,999: ")

# Create a new string without the comma.
result = numStr[0] + numStr[1] + numStr[3] + numStr[4] + numStr[5]

# Display the result.
print(result)

