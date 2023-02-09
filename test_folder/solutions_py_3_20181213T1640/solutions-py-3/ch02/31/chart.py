##
#  Draw a bar chart of bridge lengths.
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Set up the scale.
pixels_per_foot = 375 / 4200

# Draw the bars.
canvas.setColor("red")
canvas.drawRect(0, 25, 4200 * pixels_per_foot, 50)
canvas.setColor(150, 150, 255)
canvas.drawRect(0, 125, 1595 * pixels_per_foot, 50)
canvas.setColor("yellow")
canvas.drawRect(0, 225, 2150 * pixels_per_foot, 50)
canvas.setColor("green")
canvas.drawRect(0, 325, 3800 * pixels_per_foot, 50)

# Draw the labels.
canvas.setAnchor("w")
canvas.setColor("black")
canvas.drawText(10, 50, "Golden Gate")
canvas.drawText(10, 150, "Brooklyn")
canvas.drawText(10, 250, "Delaware Memorial")
canvas.drawText(10, 350, "Mackinac")

win.wait()

