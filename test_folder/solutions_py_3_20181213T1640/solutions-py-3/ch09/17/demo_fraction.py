##
#  Demonstrate negation and subtraction.
#
from fraction import Fraction

# Create two fractions.
f1 = Fraction(1, 2)
f2 = Fraction(1, 4)

# Negating one of them.
result = -f1

# Display the result.
print("Negating", f1, "gives", result)

# Subtracting them.
result = f1 - f2

# Display the result.
print(f1, "-", f2, "=", result)

