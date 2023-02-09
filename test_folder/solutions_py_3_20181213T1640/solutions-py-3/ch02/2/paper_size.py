##
#  Compute and display the perimeter of a letter size sheet of paper, and
#  the length of its diagonal.
#
from math import sqrt

WIDTH = 8.5
HEIGHT = 11

# Compute the perimeter and the length of the diagonal.
perimeter = 2 * WIDTH + 2 * HEIGHT
diagonal = sqrt(WIDTH * WIDTH + HEIGHT * HEIGHT)

# Display the result.
print("The perimeter is", perimeter, "inches.")
print("The length of the diagonal is %.2f inches." % diagonal)

