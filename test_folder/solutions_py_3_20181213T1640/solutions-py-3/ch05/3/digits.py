##
#  Use functions to perform tasks involving digits.
#
from math import ceil, log10

def main() :
   print("firstDigit of 1729 is", firstDigit(1729))
   print("firstDigit of 1 is", firstDigit(1))
   print("firstDigit of 555 is", firstDigit(555))

   print("lastDigit of 1729 is", lastDigit(1729))
   print("lastDigit of 1 is", lastDigit(1))
   print("lastDigit of 555 is", lastDigit(555))

   print("digits of 1729 is", digits(1729))
   print("digits of 1 is", digits(1))
   print("digits of 555 is", digits(555))

## Report the first digit in a number.
#  @param n the number to process
#  @return The left most digit in the number
#
def firstDigit(n) :
   string = str(n)
   first = int(string[0])
   return first

## Report the last digit in a number.
#  @param n the number to process
#  @return The right most digit in the number
#
def lastDigit(n) :
   return n % 10

## Report the number of digits in a number.
#  @param n the number to process
#  @return A count of the number of digits in the number
#
def digits(n) :
   string = str(n)
   return len(string)

# Call the main function.
main()

