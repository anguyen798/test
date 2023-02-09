##
#  Demonstrate equality testing.
#
from fraction import Fraction

# Create three fractions.
f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
f3 = Fraction(2, 4)

# Perform three equality tests and display the result.
print(f1, "==", f2, "=", f1 == f2)
print(f1, "==", f3, "=", f1 == f3)
print(f2, "==", f3, "=", f2 == f3)

