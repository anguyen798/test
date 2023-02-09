##
#  Draw the Koch Snowflake.
#
from math import atan2, cos, sin, pi, sqrt
from graphics import GraphicsWindow

def main() :
   # Create the graphics window and get the canvas.
   win = GraphicsWindow(400, 400)
   canvas = win.canvas()
   
   # Draw 4 levels of the fractal.
   length = 4
   for i in range(0, 4) :
      canvas.clear()
      length = length * 3
      xpos = 200 - length / 3 * sin(pi / 6)
      x1 = xpos - length / 2 * cos(pi / 6)
      y1 = 200
      x2 = xpos + length / 2 * cos(pi / 6)
      y2 = 200 - length * sin(pi / 6)
      x3 = xpos + length / 2 * cos(pi / 6)
      y3 = 200 + length * sin(pi / 6)
      fractalLine(canvas, x1, y1, x2, y2, i + 1)
      fractalLine(canvas, x2, y2, x3, y3, i + 1)
      fractalLine(canvas, x3, y3, x1, y1, i + 1)
      input()

## Get the points along a fractal line.
#  @param x1 the x part of the first point
#  @param y1 the y part of the first point
#  @param x2 the x part of the second point
#  @param y2 the y part of the second point
#  @return a list of points along the fractal line
#
def fractalPoints(x1, y1, x2, y2) :
   rise = y2 - y1
   run = x2 - x1
   angle = atan2(rise, run)
   length = sqrt(rise * rise + run * run)

   x3rd = x1 + length / 3 * cos(angle)
   y3rd = y1 + length / 3 * sin(angle)

   x23rd = x1 + length * 2 / 3 * cos(angle)
   y23rd = y1 + length * 2 / 3 * sin(angle)

   xhalf = x3rd + length / 3 * cos(angle - pi / 3)
   yhalf = y3rd + length / 3 * sin(angle - pi / 3)

   return [x1, y1, x3rd, y3rd, xhalf, yhalf, x23rd, y23rd, x2, y2]

## Draw a fractal line on the canvas.
#  @param canvas the canvas to draw onto
#  @param x1 the x part of the start of the line
#  @param y1 the y part of the start of the line
#  @param x2 the x part of the end of the line
#  @param y2 the y part of the end of the line
#  @param level the number of recursion levels used to draw the line segment
#
def fractalLine(canvas, x1, y1, x2, y2, level) :
   if level == 1 :
      canvas.drawLine(x1, y1, x2, y2)
   else :
      points = fractalPoints(x1, y1, x2, y2)
      for i in range(0, len(points) - 2, 2) :
         fractalLine(canvas, points[i], points[i+1], points[i+2], points[i+3], level-1)

# Call the main function.
main()

