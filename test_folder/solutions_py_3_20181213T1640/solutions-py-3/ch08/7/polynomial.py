## Create a new polynomial.
#  @param coeff the coefficient for the term
#  @param power the power for the term
#  @return a newly construct polynomial
#
def newPolynomial(coeff, power) :
   return [(coeff, power)]

## Add a term to an existing polynomial.
#  @param poly the polynomial to add the term to
#  @param coeff the coefficient for the term to add
#  @param power the power for the term to add
#
def addTerm(poly, coeff, power) :
   poly.append((coeff, power))

## Add two polynomials together, returning a new polynomial as the result.
#  @param p the first polynomial to add
#  @param q the second polynomial to add
#  @return a new polynomial which is the sum of p and q
#
def add(p, q) :
   return collapseLike(p + q)

## Multiply two polynomials together, returns a new polynomial as the result.
#  @param p the first polynomial to multiply
#  @param q the second polynomial to add
#  @return a new polynimal which is the product of p and q
#
def multiply(p, q) :
   result = []
   for i in p :
      for j in q :
         result.append((i[0] * j[0], i[1] + j[1]))

   return collapseLike(result)

## Print a polynomial with nice formatting.
#  @param poly the polynomial to print
#
def printPolynomial(poly) :
   first = True
   for term in poly :
      if not first :
         if term[0] < 0 :
            print("- ", end="")
         else :
            print("+ ", end="")
      elif term[0] < 0 :
         print("- ", end="")
      first = False

      if abs(term[0]) != 1 or term[1] == 0 :
         print(abs(term[0]), end="")

      if term[1] == 1 :
         print("x", end="")
      elif term[1] > 1 :
         print("x^%d" % term[1], end="")
      print(" ", end="")

## Collapse all terms with the same power into an equivalent single term.
#  @param poly the polynomial that may contain terms with the same power
#  @return a new polynomial where each power is unique
#
def collapseLike(poly) :
   result = []
   temp = list(poly)
   i = 0
   while i < len(temp) :
      j = i + 1
      total = temp[i][0]
      while j < len(temp) :
         if temp[i][1] == temp[j][1] :
            total = total + temp[j][0]
            temp.pop(j)
         else :
            j = j + 1
      result.append((total, temp[0][1]))
      temp.pop(i)
   return result

