##
#  Build a list of 10 unique values.
#

# Define constant variables.
NUM_INTEGERS = 10

# Read a collection of values from the user, adding each to the list if it is
# not already present.
values = []
while len(values) < NUM_INTEGERS :
   x = float(input("Enter a number: "))
   if x not in values :
      values.append(x)

# Display the values.
print("The numbers are: ", values)

