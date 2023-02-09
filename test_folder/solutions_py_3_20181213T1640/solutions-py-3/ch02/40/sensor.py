##
#  Determine the temperature of a liquid given the resistance of a thermistor.
#
from math import log

# Define constants.
R0 = 1075
T0 = 85 + 273.15
Beta = 3969

# Gather input from the user.
r = float(input("Enter the thermistor resistance: "))

# Compute the temperature in degrees Celsius.
t = (Beta * T0) / (T0 * log(r / R0) + Beta) - 273

# Display the result.
print("The temperature is %.2f degrees Celsius" % t)

