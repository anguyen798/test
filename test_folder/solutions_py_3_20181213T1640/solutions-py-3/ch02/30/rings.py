##
#  Draw the Olympic rings.
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Draw the rings.
canvas.setLineWidth(5)
canvas.setOutline("blue")
canvas.drawOval(55, 125, 90, 90)
canvas.setOutline("black")
canvas.drawOval(155, 125, 90, 90)
canvas.setOutline("red")
canvas.drawOval(255, 125, 90, 90)

canvas.setOutline("yellow")
canvas.drawOval(105, 175, 90, 90)
canvas.setOutline("green")
canvas.drawOval(205, 175, 90, 90)

win.wait()

