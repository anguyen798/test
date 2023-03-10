##
#  This program prints trace messages that show how often the
#  recursive function for computing Fibonacci numbers calls itself.
#

def main() :
   n = int(input("Enter n: "))
   for i in range(1, n + 1) :
      f = fib(i)
      print("fib(%d) = %d" % (i, f))

## Computes a Fibonacci number.
#  @param n an integer
#  @return the nth Fibonacci number
#
def fib(n) :
   print("Entering fib: n =", n) 
   if n <= 2 :
      f = 1
   else :
      f = fib(n - 1) + fib(n - 2)
   print("Exiting fib: n =", n, "return value =", f)
   return f
      
# Start the program.
main()
