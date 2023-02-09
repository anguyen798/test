##
#  Simulate the Buffon Needle Experiment.
#

from random import random
from math import pi, sin

# Define constant variables.
LIMIT = 10000

# Drop the needle, checking to see if it touched the line each time.
hits = 0
for i in range(0, LIMIT) :
   ylow = random() * 2
   angle = random() * pi
   yhigh = ylow + sin(angle)

   # It touched the line if yhigh is at least 2.
   if yhigh >= 2 :
      hits = hits + 1

# Display the result.
print("Using the experiment, we approximated pi as", LIMIT / hits)

