##
#  This program tests several of the geometric shape classes.
#

from graphics import GraphicsWindow
from shapes import Rectangle, Arrow, Group

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

# Draw six arrows of different colors.
colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]

arrow = Arrow(10, 150, 300, 150)

for i in range(6) :
   arrow.setColor(colors[i])
   arrow.draw(canvas)
   arrow.moveBy(10, 10)

# Draw two additional arrows.
arrow = Arrow(50, 350, 100, 300)
arrow.setColor("black")
arrow.draw(canvas)

arrow = Arrow(200, 322, 150, 300)
arrow.setColor("black")
arrow.draw(canvas)

win.wait()

