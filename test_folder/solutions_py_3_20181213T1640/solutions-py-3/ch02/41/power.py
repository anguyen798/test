##
#  Compute the source voltage from the power factor provided by the user.
#
from math import sqrt

# Define constants.
R = 10
VT = 120
P = 260

# Read input from the user.
pf = float(input("Enter a power factor between 0 and 1: "))

# Compute the source voltage.
vs = sqrt((VT + (2 * R * P) / VT) ** 2 + 
          ((2 * R * P) / (pf * VT)) ** 2 * (1 - pf ** 2))

# Display the result.
print("The source voltage is %.2f volts." % vs)

