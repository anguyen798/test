##
#  Compute Fibonacci numbers using three different strategies.
#
from time import time

## Compute the nth Fibonacci number, using the traditional recursive algorithm.
#  @param n the Fibonacci number to compute
#  @return the nth Fibonacci number
#
def traditionalFib(n) :
   if n <= 2 :
      return 1
   else :
      return traditionalFib(n - 1) + traditionalFib(n - 2)

## Compute the nth Fibonacci number, using recursion and a cache of previously
#  computed values.
#  @param n the Fibonacci number to compute
#  @return the nth Fibonacci number
#
def fibHelper(n, cache) :
   if n < len(cache) and cache[n] != None:
      return cache[n]
   else :
      while len(cache) < n + 1 :
         cache.append(None)

      cache[n] = fibHelper(n - 1, cache) + fibHelper(n - 2, cache)
      return cache[n]
      
## Compute the nth Fibonacci number, using recursion and a cache of previously
#  computed values.
#  @param n the Fibonacci number to compute
#  @return the nth Fibonacci number
#
def fastRecFib(n) :
   return fibHelper(n, [0, 1, 1])

## Compute the nth Fibonacci number, using a loop.
#  @param n the Fibonacci number to compute
#  @return the nth Fibonacci number
#
def itFib(n) :
   if n <= 2 :
      return 1
   else :
      olderValue = 1
      oldValue = 1
      newValue = 1
      for i in range(3, n + 1) :
         newValue = oldValue + olderValue
         olderValue = oldValue
         oldValue = newValue

      return newValue

def main() :
   # Demonstrate the three functions, noting that traditionalFib is far
   # slower than the other two.
   start = time()
   print("traditionalFib(33) is", traditionalFib(33))
   end = time()
   print("traditionalFib(33) elapsed time: %.3f seconds" % (end-start))
   start = time()
   print("fastRecFib(33) is", fastRecFib(33))
   end = time()
   print("fastRecFib(33) elapsed time: %.3f seconds" % (end-start))
   start = time()
   print("itFib(33) is", itFib(33))
   end = time()
   print("itFib(33) elapsed time: %.3f seconds" % (end-start))

# Call the main function.
main()

