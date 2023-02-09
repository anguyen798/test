##
#  Draw a square spiral in a graphics window.
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Draw the horizontal lines extending down from the center.
for i in range(0, 8) :
   canvas.drawLine(190 - i * 20, 200 + i * 20, 210 + i * 20, 200 + i * 20)

# Draw the horizontal lines extending up from the center and the vertical
# lines.
for i in range(0, 7) :
   canvas.drawLine(210 + i * 20, 180 - i * 20, 210 + i * 20, 200 + i * 20)
   canvas.drawLine(170 - i * 20, 180 - i * 20, 210 + i * 20, 180 - i * 20)
   canvas.drawLine(170 - i * 20, 180 - i * 20, 170 - i * 20, 220 + i * 20)

# Handle the last line segment on the right side at the outside of the spiral.
canvas.drawLine(210 + 7 * 20, 180 - 6 * 20, 210 + 7 * 20, 200 + 7 * 20)

win.wait()

