##
#  Draw a checkerboard in a graphics window.
#
from graphics import GraphicsWindow

# Create constant variables.
SIZE = 400

# Create the graphics window and get the canvas.
win = GraphicsWindow(SIZE, SIZE)
canvas = win.canvas()

# Draw the board.
canvas.setColor("black")
for y in range(0, SIZE, SIZE // 8) :
   for x in range(0, SIZE, SIZE // 8) :
      if (x + y) // (SIZE // 8) % 2 == 0 :
         canvas.drawRect(x, y, SIZE // 8, SIZE // 8)

win.wait()

