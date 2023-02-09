##
#  Determine if a person achieves escape velocity.
#
from math import sqrt

# Define constants.
G = 6.67e-11
M = 1.3e22
R = 1.153e6

# Read input from the user.
mph = float(input("Enter the jump velocity in mph: "))

# Convert to m/s so that we can use the provided formula.
v = mph * 0.44704

# Compute the escape velocity in m/s.
vescape = sqrt(2 * G * M / R)

# Determine if the speed is sufficient to escape and display the result.
if v >= vescape :
   print("That was enough to jump off Hayley's Comet and never come back down.")
   mass = R * v * v / (2 * G)
   print("The comet would need a mass of %4g to have enough gravity to" % mass)
   print("bring you back.  (Hayley's Comet has a mass of %4g)" % M)
else :
   print("At that speed, you'll come back down to Hayley's Comet")

