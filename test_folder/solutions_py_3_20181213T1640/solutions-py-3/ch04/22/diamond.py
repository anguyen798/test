##
#  Display a diamond with a side length supplied by the user.
#

# Read the side length from the user.
sideLength = int(input("Enter the side length: "))

# Display the diamond.
for y in range(1, sideLength) :
   print(" " * (sideLength - y) + "*" * (y * 2 - 1))
for y in range(sideLength, 0, -1) :
   print(" " * (sideLength - y) + "*" * (y * 2 - 1))

