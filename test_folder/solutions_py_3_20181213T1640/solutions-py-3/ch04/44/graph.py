##
#  Plot the curve r = cos(2 * theta) in a graphics window.  Scale the curve
#  so that it is centered in the window and fills it nicely.
#
from graphics import GraphicsWindow
from math import pi, cos, sin

# Create the graphics window and get the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Compute the first point.
theta = 0
r = cos(2 * theta)
prev_x = 200 + 100 * r * cos(theta)
prev_y = 200 + 100 * r * sin(theta)

# Compute the remaining points and connect them.
while theta <= 2 * pi :
   # Compute the current point.
   r = cos(2 * theta)
   x = 200 + 100 * r * cos(theta)
   y = 200 + 100 * r * sin(theta)
   
   # Draw a line connecting the current point to the previous point.
   canvas.drawLine(x, y, prev_x, prev_y)
   prev_x = x
   prev_y = y

   theta = theta + pi / 50

win.wait()

