##
#  Compute a square root using recursion.
#

## Compute the square root of x.
#  @param x the number to compute the square root of
#  @param g the initial guess of the square root
#  @return the square root of x, within 1e-14
#
def squareRootGuess(x, g) :
   if abs(g * g - x) < 1e-14 :
      return g
   return squareRootGuess(x, (g + x/g) / 2)

## Compute the square root of x.
#  @param x the number to compute the square root of
#  @return the square root of x, within 1e-14
#
def squareRoot(x) :
   return squareRootGuess(x, x)

def main() :
   print("sqrt(2) is", squareRoot(2))
   print("sqrt(4) is", squareRoot(4))

# Call the main function.
main()

