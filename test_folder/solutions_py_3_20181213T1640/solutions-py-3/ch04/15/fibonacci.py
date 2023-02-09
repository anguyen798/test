##
#  Compute and display the Fibonacci number requested by the user.
#

# Read input from the user.
n = int(input("Enter an integer: "))

# Handle the special cases for the first two Fibonacci numbers.
if n == 1 :
   fnew = 1
elif n == 2 :
   fnew = 1
else :
   # Compute the Fibonacci number.
   fold1 = 1
   fold2 = 1
   for i in range(2, n) :
      fnew = fold1 + fold2
      fold1 = fold2
      fold2 = fnew
   
# Display the result.
print("Fibonacci number", n, "is", fnew)

