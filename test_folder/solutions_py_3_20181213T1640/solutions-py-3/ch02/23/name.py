##
#  Draw a name inside a blue rectangle.
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Draw the box and text.
canvas.setOutline("blue")
canvas.setFill()
canvas.drawRect(100, 150, 200, 100)

canvas.setColor("red")
canvas.drawText(200, 200, "Harry")

win.wait()

