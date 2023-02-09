##
#  Compute the inductance value and range of frequencies for a tuning circuit.
#
from math import sqrt, pi

# Read input from the user.
f = float(input("Enter a frequency in Hz: "))
cmin = float(input("Enter the minimum capacitance in F: "))
cmax = float(input("Enter the maximum capacitance in F: "))

# Compute the inductance value and the frequency range.
c = sqrt(cmin * cmax)
l = (2 * pi / f) ** 2 / c
fmin = 2 * pi / sqrt(l * cmax)
fmax = 2 * pi / sqrt(l * cmin)

# Display the result.
print("The inductance value is %.10f" % l)
print("The minimum frequency is %.2f Hz" % fmin)
print("The maximum frequency is %.2f Hz" % fmax)

