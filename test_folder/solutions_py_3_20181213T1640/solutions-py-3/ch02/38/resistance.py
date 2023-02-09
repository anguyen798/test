##
#  Compute the resistance of a circuit.
#

# Read input from the user.
r1 = float(input("Enter the value for R1: "))
r2 = float(input("Enter the value for R2: "))
r3 = float(input("Enter the value for R3: "))

# Compute the resistance of the resistors in parallel and the total resistance.
r23 = r2 * r3 / (r2 + r3)
total = r1 + r23

# Display the result.
print("The total resistance is %.2f ohms" % total)

