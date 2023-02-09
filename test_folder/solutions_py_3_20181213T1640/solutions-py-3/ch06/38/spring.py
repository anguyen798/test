##
#  Simulate a spring.
#
from graphics import GraphicsWindow

# Define constant variables.
INIT_DISPLACEMENT = 0.5
INIT_VELOCITY = 0
MASS = 1
K = 10
TIMESTEP = 0.01
WIDTH = 400
YOFFSET = 100

# Create the graphics window and get the canvas.
win = GraphicsWindow(WIDTH, 400)
canvas = win.canvas()

# Set up initial values for the draw position in the window, the spring
# displacement and the velocity.
win_pos = 0
x = INIT_DISPLACEMENT
v = INIT_VELOCITY

# Plot the position of the spring until we have moved all the way across the
# window.
canvas.setColor("black")
while win_pos < WIDTH :
   # Update the spring speed and displacement 10 times between each time its
   # position is plotted.
   for i in range(0, 10) :
      a = -K * x / MASS
      v = v + a * TIMESTEP
      x = x + v * TIMESTEP

   # Plot the position in the window.
   canvas.drawLine(win_pos, 0, win_pos, YOFFSET + x * 100)
   win_pos = win_pos + 1

win.wait()

