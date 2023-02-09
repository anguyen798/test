##
#  Draw the coordinate system.
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(500, 500)
canvas = win.canvas()

# Draw the coordinate system.
canvas.drawArrow(50, 50, 450, 50)
canvas.drawArrow(50, 50, 50, 450)

canvas.drawLine(45, 150, 55, 150)
canvas.drawLine(45, 250, 55, 250)
canvas.drawLine(45, 350, 55, 350)

canvas.drawLine(150, 45, 150, 55)
canvas.drawLine(250, 45, 250, 55)
canvas.drawLine(350, 45, 350, 55)

# Add the text labels.
canvas.drawText(50, 40, "(0, 0)")
canvas.drawText(435, 40, "x")
canvas.drawText(40, 435, "y")
canvas.drawText(190, 250, "(10, 20)")
canvas.drawText(290, 150, "(20, 10)")

# Draw the red dots.
canvas.setColor("red")
canvas.drawOval(147, 247, 7, 7)
canvas.drawOval(247, 147, 7, 7)

win.wait()

