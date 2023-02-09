##
#  Determine whether a rope will snap when whirling a mass.
#

# Define constants.
M = 2
R = 3
MAX_T = 60

# Read input from the user.
v = float(input("Enter the rotation speed: "))

# Compute the tension.
t = M * v * v / R

# Display the result.
if t < MAX_T :
   print("The rope does not break.")
else :
   print("The rope breaks.")

