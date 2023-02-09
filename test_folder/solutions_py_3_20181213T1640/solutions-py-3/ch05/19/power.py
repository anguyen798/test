##
#  Use recursion to compute a^n.
#

def main() :
   print("3 ** 3 is", power(3, 3))
   print("2 ** 4 is", power(2, 4))
   print("2 ** 8 is", power(2, 8))
   print("2 ** 20 is", power(2, 20))

## Compute a number raised to an integer power.
#  @param a the number to raise to a power
#  @param n the power to raise the number to
#  @returns a raised to the nth power
#
def power(a, n) :
   if n == 1 :
      return a
   elif n % 2 == 0 :
      return power(a, n // 2) ** 2
   else :
      return a * power(a, n - 1)

# Call the main function.
main()

