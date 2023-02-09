##
#  Read parameters for a capacitor from a file, and save its voltage over
#  time to a new file.
#
from math import e

# Define constant variables.
NUM_STEPS = 100

# Open the parameter file and read its values.
inf = open("params.txt", "r")
b = float(inf.readline())
r = float(inf.readline())
c = float(inf.readline())
start = float(inf.readline())
end = float(inf.readline())
inf.close()

# Compute the step size.
step = (end - start) / (NUM_STEPS)

# Open the output file for writing.
outf = open("rc.txt", "w")

# Save 100 steps from start up to end.
t = start
while t < end :
   vt = b * (1 - e ** (-t / (r * c)))
   outf.write("%4d  %.5f\n" % (t, vt))
   t = t + step

# Close the file.
outf.close()

