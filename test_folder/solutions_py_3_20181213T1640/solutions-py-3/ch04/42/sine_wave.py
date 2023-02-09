##
#  Draw a sine wave in a graphics window.
#
from graphics import GraphicsWindow
from math import radians, sin

# Create constant variables.
SIZE = 400

# Create the graphics window and get the canvas.
win = GraphicsWindow(SIZE, SIZE)
canvas = win.canvas()

# Draw the sine wave.
canvas.setLineWidth(3)
for angle in range(0, 360, 5) :
   canvas.drawLine(SIZE / 360 * angle, SIZE / 2, SIZE / 360 * angle, SIZE / 2 + sin(radians(angle)) * SIZE / 2)

win.wait()

