##
#  Display a multiplication table up to 10 times 10.
#

# Define constant variables.
LIMIT = 10

# Display the table using nested for loops.
for y in range(1, LIMIT + 1) :
   for x in range(1, LIMIT + 1) :
      print("%4d" % (y * x), end="")
   print()

