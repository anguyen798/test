##
#  This program tests several of the geometric shape classes.
#

from graphics import GraphicsWindow
from shapes import Rectangle, DashedLine, Group

# Create the window.
win = GraphicsWindow()
canvas = win.canvas()

# Draw a rectangle.
rect = Rectangle(10, 10, 90, 60)
rect.setFill("light yellow")
rect.draw(canvas)

# Draw another rectangle.
rect.moveBy(rect.getWidth(), rect.getHeight())
rect.draw(canvas)

# Draw six lines of different colors.
colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]

line = DashedLine(10, 150, 300, 250, 4, 8)

for i in range(6) :
   line.setColor(colors[i])
   line.draw(canvas)
   line.moveBy(10, 10)

win.wait()

