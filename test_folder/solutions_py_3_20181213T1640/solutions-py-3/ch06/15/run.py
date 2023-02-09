##
#  Identify runs in a sequence of die tosses.
#

from random import randint

# Define constants.
NUM_TOSSES = 20

# Generate 20 random values.
values = []
for i in range(0, NUM_TOSSES) :
   values.append(randint(1, 6))

# For each value in the list.
inRun = False
for i in range(0, len(values)) :
   # If we have inRun a bracket and the value is different from the previous
   # one then close the bracket.
   if inRun and i != 0 and values[i] != values[i - 1] :
      print(")", end="")
      inRun = False

   # If we have printed an element previously then put a space after it.
   if i != 0 :
      print(end=" ")

   # If we are not already inside a bracket and the current value is the same
   # as the next then print the open bracket.
   if not inRun and i != len(values) - 1 and values[i] == values[i + 1] :
      print("(", end="")
      inRun = True

   # Display the value.
   print(values[i], end="")

# Print the final closing bracket if the last and second last elements are the
# same.
if inRun :
   print(")", end="")
print()

