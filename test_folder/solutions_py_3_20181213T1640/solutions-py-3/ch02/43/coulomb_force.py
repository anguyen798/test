##
#  Calculate the force on a pair of charged particles.
#
from math import pi

# Define constants.
EPSILON = 8.854e-12

# Gather input from the user.
q1 = float(input("Enter the charge for particle 1: "))
q2 = float(input("Enter the charge for particle 2: "))
r = float(input("Enter the distance between them in meters: "))

# Compute the force.
f = (q1 * q2) / (4 * pi * EPSILON * r ** 2)

# Display the result.
print("The force is %.5f Newtons." % f)

