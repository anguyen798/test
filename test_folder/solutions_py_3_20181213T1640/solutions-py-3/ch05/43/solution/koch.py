##
#  Draw the Koch snowflake.
#
import turtle

def main() :
   turtle.reset()
   turtle.penup()
   n = 3
   distance = 10 * 3 ** n
   turtle.goto(-distance / 2, distance / 6)
   turtle.pendown()
   koch(distance, n)
   response = input("Press ENTER to quit.")

## Draw the Koch curve 
#  @param distance the total forward distance travelled
#  @param n the order of the curve
def koch(distance, n) :
   kochLine(distance, n)
   turtle.right(120)
   kochLine(distance, n)
   turtle.right(120)
   kochLine(distance, n)
   turtle.right(120)
   
## Draw a line of the Koch curve 
#  @param distance the total forward distance travelled
#  @param n the order of the curve
def kochLine(distance, n) :
   if n == 0 :
      # The fractal line segment is just a straight segment.
      turtle.forward(distance)
   else :
      # The line segment is drawn using four line segments of lower order.
      kochLine(distance / 3, n - 1)
      turtle.left(60)
      kochLine(distance / 3, n - 1)
      turtle.right(120)
      kochLine(distance / 3, n - 1)
      turtle.left(60)
      kochLine(distance / 3, n - 1)

main()
