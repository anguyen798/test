##
#  Draw a bull's eye.
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Draw the bull's eye.
canvas.setColor("black")
canvas.drawOval(75, 75, 250, 250)
canvas.setColor("white")
canvas.drawOval(100, 100, 200, 200)
canvas.setColor("black")
canvas.drawOval(125, 125, 150, 150)
canvas.setColor("white")
canvas.drawOval(150, 150, 100, 100)
canvas.setColor("black")
canvas.drawOval(175, 175, 50, 50)

win.wait()

