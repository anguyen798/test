##
#  Compute the angle at which a viewer sees the screen.
#
from math import radians, sqrt, acos, tan, degrees

def main() :
   print(computeAngle(24, 6, radians(8), 12))
   print(computeAngle(24, 6, radians(8), 24))
   print(computeAngle(24, 6, radians(8), 36))

## Compute the viewing angle for a specific theatre with floor angle 8 degrees,
#  a screen bottom of 6 feet, and a screen height of 24 feet.
#  @param x the horizontal distance from the viewer to the screen
#  @return the viewing angle at distance x
#
def computeAngleSpecificTheatre(x) :
   # Compute the height, y, above the bottom of the floor for the viewer.
   y = x * tan(radians(8))

   # Form a vector a,b from the viewer to the bottom the screen.
   a = -x
   b = 6 - y

   # Form a vector c,d from the viewer to the top of the screen.
   c = -x
   d = (6 + 24) - y

   # Compute the viewing angle.
   angle = acos(dot(a, b, c, d) / (length(a, b) * length(c, d)))

   # Return the result.
   return angle

## Compute the viewing angle for an arbitrary theatre.
#  @param screenHeight the height of the screen
#  @param aboveFloor the distance from the floor to the bottom of the screen
#  @param floorAngle the floor angle in radians
#  @param x the horizontal distance from the viewer to the screen
#  @return the viewing angle at distance x
#
def computeAngle(screenHeight, aboveFloor, floorAngle, x) :
   # Compute the height, y, above the bottom of the floor for the viewer.
   y = x * tan(floorAngle)

   # Form a vector a,b from the viewer to the bottom the screen.
   a = -x
   b = aboveFloor - y

   # Form a vector c,d from the viewer to the top of the screen.
   c = -x
   d = (aboveFloor + screenHeight) - y

   # Compute the viewing angle.
   angle = acos(dot(a, b, c, d) / (length(a, b) * length(c, d)))

   # Return the result.
   return angle

## Compute the dot product of vectors (x1, y1) and (x2, y2).
#  @param x1 the x component of vector 1
#  @param y1 the y component of vector 1
#  @param x2 the x component of vector 2
#  @param y2 the y component of vector 2
#  @return the dot product of the vectors
#
def dot(x1, y1, x2, y2) :
   return x1 * x2 + y1 * y2

## Compute the length of the hypoteneuse of a right triangle.
#  @param a the length of one side
#  @param b the length of the other side
#  @return the length of the third side
#
def length(a, b) :
   return sqrt(a * a + b * b)

# Call the main function.
main()

