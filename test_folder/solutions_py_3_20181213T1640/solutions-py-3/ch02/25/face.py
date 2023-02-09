##
#  Draw a face in a graphics window.
#
from graphics import GraphicsWindow

# Create the graphics window and get the canvas.
win = GraphicsWindow(400, 400)
canvas = win.canvas()

# Draw the face.
canvas.drawOval(100, 100, 200, 200)
canvas.drawOval(140, 160, 20, 20)
canvas.drawOval(240, 160, 20, 20)
canvas.drawLine(140, 250, 260, 250)

win.wait()

