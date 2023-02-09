##
#  This program tests several of the geometric shape classes.
#

from graphics import GraphicsWindow
from shapes import Rectangle, Line, Group

# Create the window.
win = GraphicsWindow()
canvas = win.canvas()

# Draw a rectangle.
rect = Rectangle(10, 10, 90, 60)
rect.setFill("light yellow")
rect.draw(canvas)
print("%d %d" % (rect.getX(), rect.getY()))
print("Expected: 10 10")

# Draw another rectangle.
rect.moveBy(rect.getWidth(), rect.getHeight())
rect.draw(canvas)
print("%d %d" % (rect.getX(), rect.getY()))
print("Expected: 100 70")

# Draw six lines of different colors.
colors = ["red", "green", "blue", "yellow", "magenta", "cyan"]

line = Line(10, 150, 300, 150)

for i in range(6) :
   line.setColor(colors[i])
   line.draw(canvas)
   line.moveBy(10, 10)
   print("%d %d" % (line.getX(), line.getY()))
   print("Expected: %d %d" % (i * 10 + 20, i * 10 + 160))
   
win.wait()

