##
#  Compute the due point for a provided relative humidity and temperature.
#
from math import log

# Define constants.
A = 17.27
B = 237.7

# Read input from the user.
rh = float(input("Enter the relative humidity (between 0 and 1): "))
t = float(input("Enter the actual temperature in degrees Celsius: "))

# Compute the due point.
f_t_rh = (A * t) / (B + t) + log(rh)
td = (B * f_t_rh) / (A - f_t_rh)

# Display the result.
print("The due point is", td)

