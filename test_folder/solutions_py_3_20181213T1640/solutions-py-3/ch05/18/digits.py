##
#  Use recursion to count the number of digits in an integer.
#

def main() :
   print("The number of digits in 7 is", digits(7))
   print("The number of digits in 12 is", digits(12))
   print("The number of digits in 2345 is", digits(2345))

## Count the number of digits in an integer.
#  @param n the integer whose digits will be counted
#  @return the number of digits in n
#
def digits(n) :
   if n < 10 :
      return 1
   return 1 + digits(n // 10)

# Call the main function.
main()

