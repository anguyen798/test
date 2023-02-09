## Create a new polynomial.
#  @param coeff the coefficient for the term
#  @param power the power for the term
#  @return a newly construct polynomial
#
def newPolynomial(coeff, power) :
   return {power: coeff}

## Add a term to an existing polynomial.
#  @param poly the polynomial to add the term to
#  @param coeff the coefficient for the term to add
#  @param power the power for the term to add
#
def addTerm(poly, coeff, power) :
   if power in poly :
      poly[power] = poly[power] + coeff
   else :
      poly[power] = coeff

## Add two polynomials together, returning a new polynomial as the result.
#  @param p the first polynomial to add
#  @param q the second polynomial to add
#  @return a new polynomial which is the sum of p and q
#
def add(p, q) :
   retval = dict(p)
   for power in q :
      if power in p :
         retval[power] = retval[power] + q[power]
      else :
         retval[power] = q[power]

   return retval

## Multiply two polynomials together, returns a new polynomial as the result.
#  @param p the first polynomial to multiply
#  @param q the second polynomial to add
#  @return a new polynimal which is the product of p and q
#
def multiply(p, q) :
   result = {}
   for i in p :
      for j in q :
         coeff = p[i] * q[j]
         power = i + j
         if power in result :
            result[power] = result[power] + coeff
         else :
            result[power] = coeff
   return result

## Print a polynomial with nice formatting.
#  @param poly the polynomial to print
#
def printPolynomial(poly) :
   first = True
   for power in poly :
      if not first :
         if poly[power] < 0 :
            print("- ", end="")
         else :
            print("+ ", end="")
      elif poly[power] < 0 :
         print("- ", end="")
      first = False

      if abs(poly[power]) != 1 or power == 0 :
         print(abs(poly[power]), end="")

      if power == 1 :
         print("x", end="")
      elif power > 1 :
         print("x^%d" % power, end="")
      print(" ", end="")

