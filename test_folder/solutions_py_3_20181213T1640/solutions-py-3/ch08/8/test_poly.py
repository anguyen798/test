##
#  Test the polynomial operations.
#
from polynomial import *

# Create new polynomials p and q.
p = newPolynomial(2, 2)
addTerm(p, 1, 1)
addTerm(p, 1, 0)

q = newPolynomial(3, 1)
addTerm(q, 2, 0)

# Display p and q.
print("p is ", end="")
printPolynomial(p)
print()

print("q is ", end="")
printPolynomial(q)
print()

# Compute and display the sum of p and q.
total = add(p, q)
print("The sum of p and q is ", end="")
printPolynomial(total)
print()

# Compute and display the product of p and q.
product = multiply(p, q)
print("The product of p and q is ", end="")
printPolynomial(product)
print()

