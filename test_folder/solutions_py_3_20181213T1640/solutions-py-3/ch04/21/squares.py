##
#  Display a filled square and a hollow square.
#

# Read input from the user.
sideLength = int(input("Enter the side length for the square: "))

# Draw a filled square and a solid square.
if sideLength == 1 :
   print("* *")
else :
   # Draw the top.
   print("*" * sideLength, "*" * sideLength)

   # Draw the middle lines.
   for y in range(2, sideLength) :
      print("*" * sideLength, "*%s*" % (" " * (sideLength - 2)))

   # Draw the bottom.
   print("*" * sideLength, "*" * sideLength)

