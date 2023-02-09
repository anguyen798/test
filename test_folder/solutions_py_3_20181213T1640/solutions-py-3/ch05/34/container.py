##
#  Compute the volume and surface area of a container.
#
from math import pi, sqrt

def main() :
   # Gather input from the user.
   bot = float(input("Enter the bottom radius: "))
   top = float(input("Enter the top radius: "))
   height = float(input("Enter the height: "))

   # Compute and display the results.
   print("The volume is: %.2f" % volume(bot, top, height))
   print("The surface area is: %.2f" % surfaceArea(bot, top, height))

## Compute the volume of a frustum of a cone.
#  @param r1 the bottom radius of the frustum
#  @param r2 the top radius of the frustum
#  @param the height of the frustum
#  @return the volume of the frustum
#
def volume(r1, r2, h) :
   return 1 / 3 * pi * h * (r1 * r1 + r2 * r2 + r1 * r2)

## Compute the surface area of a frustum of a cone.
#  @param r1 the bottom radius of the frustum
#  @param r2 the top radius of the frustum
#  @param the height of the frustum
#  @return the surface area of the frustum
#
def surfaceArea(r1, r2, h) :
   return pi * (r1 + r2) * sqrt((r1 - r2) ** 2 + h * h) + pi * r1 * r1

# Call the main function.
main()

