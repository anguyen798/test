##
#  Determine whether or not a frost alarm will sound at a given temperature.
#
from math import e

# Define constants.
R0 = 33192
T0 = 40 + 273
BETA = 3310
R2 = 156300
R3 = 156300
R4 = 156300

# Read input from the user and convert it to Kelvin.
temp_f = float(input("Enter a temperature in Fahrenheit: "))
temp_k = (temp_f - 32) * 5 / 9 + 273

# Compute the value of R.
r = R0 * e ** (BETA * (1 / temp_k - 1 / T0))

# Determine and display if the alarm will sound.
if R2 / (r + R2) < R4 / (R3 + R4) :
   print("The alarm will sound.")
else :
   print("The alarm will not sound.")

