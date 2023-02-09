##
#  Compute the area, perimeter and diagonal length for a rectangle.
#
from math import sqrt

# Read the length and width from the user.
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Compute the area, perimeter and diagonal length.
area = length * width
perimeter = 2 * length + 2 * width
diagonal = sqrt(length * length + width * width)

# Display the result.
print("The area is", area)
print("The perimteger is", perimeter)
print("The diagonal length is %.2f" % diagonal)

