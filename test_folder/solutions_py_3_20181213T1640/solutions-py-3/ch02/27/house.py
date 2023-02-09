##
#  Draw a house.
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Draw the house.
canvas.setColor("red")
canvas.drawRect(100, 150, 200, 200)
canvas.drawLine(100, 150, 200, 50)
canvas.drawLine(200, 50, 300, 150)
canvas.setColor("brown")
canvas.drawRect(133, 250, 50, 100)
canvas.setColor("pink")
canvas.drawRect(216, 270, 50, 50)

win.wait()

