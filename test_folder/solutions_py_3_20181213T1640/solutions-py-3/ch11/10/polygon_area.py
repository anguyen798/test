##
#  Compute the area of a polygon.
#

## Compute the area of a polygon.
#  @param points a list of tuples represents the points of the polygon
#  @return the area of the polygon
#
def polyArea(points) :
   x1 = points[0][0]
   y1 = points[0][1]
   x2 = points[1][0]
   y2 = points[1][1]
   x3 = points[2][0]
   y3 = points[2][1]

   # Compute the area of the first polygon.
   area = abs(x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1) / 2

   # Collect the points for the remaining polygons.
   remaining = [points[0]] + points[2 : ]
   if len(remaining) >= 3 :
      # Compute the area of the remaining polygons.
      area = area + polyArea(remaining)

   # Return the result.
   return area

def main() :
   # Demonstrate the polyArea function.
   print(polyArea([(0, 0), (1, 0), (1, 1), (0, 1)]))
   print("Expected: 1.0")

# Call the main function.
main()

