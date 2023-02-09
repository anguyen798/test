##
#  Model radioactive decay.
#
from math import e, log

# Define constant variables.
HALF_LIFE = 6

# Read the initial amount from the user.
a0 = float(input("Enter the initial amount to Technetium-99: "))

# For each of 24 hours.
for t in range(1, 25) :
   amount = a0 * e ** (-t * log(2) / HALF_LIFE)
   print("After", t, "hour(s), the amount is %.2f" % amount)

