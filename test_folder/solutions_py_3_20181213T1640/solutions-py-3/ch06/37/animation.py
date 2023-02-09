##
# This program draws a moving sine wave.
#

from graphics import GraphicsWindow
from time import sleep
from math import sin, pi, radians

def main() :
   # Do not look at the code in the main function.
   # Your code will go into the draw function below.
   
   WIN_WIDTH = 400
   WIN_HEIGHT = 400   
   
   win = GraphicsWindow(WIN_WIDTH, WIN_HEIGHT)
   canvas = win.canvas()
   canvas.setFill("black")
   canvas.clear()
   
   DELAY = 0.01   # 10 milliseconds between frames

   for frame in range(WIN_WIDTH + 1) :
      draw(canvas, frame)
      sleep(DELAY)

   win.wait()
   
## Draws a frame on the canvas.
#  @param canvas the canvas on which to draw the frame
#  @param frame which frame as a number
#
def draw(canvas, frame) :
   canvas.clear()

   # Compute the amount of angle change per pixel.
   angle_step = (2 * pi) / canvas.width()
   
   # Set the starting angle based on the current frame number.
   angle = radians(5 * frame % 720)

   # Draw the sine wave as a collection of short line segments.
   for i in range(0, canvas.width(), 5) :
      y1 = 200 + sin(angle) * 100
      y2 = 200 + sin(angle + 5 * angle_step) * 100
      canvas.drawLine(i, y1, i + 5, y2)
      angle = angle + 5 * angle_step

# Start the program.
main()

