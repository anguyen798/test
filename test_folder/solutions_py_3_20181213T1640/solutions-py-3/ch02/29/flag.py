##
#  Draw a German flag. 
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(300, 300)
canvas = win.canvas()

# Define variables for the upper-left position and the size.
xLeft = 10
yTop = 10
width = 90
height = width * 2 / 3

# Draw the flag.
canvas.setColor("black")
canvas.drawRect(xLeft, yTop, width, height / 3)
canvas.setColor("red")
canvas.drawRect(xLeft, yTop + height / 3, width, height / 3)
canvas.setColor("yellow")
canvas.drawRect(xLeft, yTop + 2 * height / 3, width, height / 3)

win.wait()

