##
#  Determine which one of several speeds is the maximum that can be used
#  without breaking a rope.
#

# Define constants.
R = 3
T_MAX = 60

# Read input from the user.
m = float(input("Enter the mass: "))

# Compute the tensions at various speeds.
t1 = m * 1 * 1 / R
t10 = m * 10 * 10 / R
t20 = m * 20 * 20 / R
t40 = m * 40 * 40 / R

# Display the result.
if t40 < T_MAX :
   print("The mass can be whirled at 40m/s.")
elif t20 < T_MAX :
   print("The mass can be whirled at 20m/s.")
elif t10 < T_MAX :
   print("The mass can be whirled at 10m/s.")
elif t1 < T_MAX :
   print("The mass can be whirled at 1m/s.")
else :
   print("The mass cannot be whirled at any of the allowed speeds.")

