##
#  Plot the curve f(x) = 0.00005x^3 - 0.03x^2 + 4x + 200 in a graphics window.
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Draw the curve.
for x in range(0, 400, 4) :
   fx = 0.00005 * x ** 3 - 0.03 * x ** 2 + 4 * x + 200
   fx1 = 0.00005 * (x + 4) ** 3 - 0.03 * (x + 4) ** 2 + 4 * (x + 4) + 200
   canvas.drawLine(x, fx, x+4, fx1)

win.wait()

