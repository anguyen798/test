##
#  Draw a pink square and a purple square.
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Draw the squares.
canvas.setColor("purple")
canvas.drawRect(50, 50, 200, 200)
canvas.setColor(255, 115, 150)
canvas.drawRect(150, 150, 200, 200)

win.wait()

