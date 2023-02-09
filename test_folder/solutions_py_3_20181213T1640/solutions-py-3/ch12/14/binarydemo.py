##
#  This program demonstrates the binary search algorithm.
#

from random import randint
from binarysearch import binarySearch

# Construct a random sorted list.
n = 20
a = [1]
for i in range(1, n) :
   a.append(a[i - 1] + randint(1, 10))   
print(a)

done = False
while not done :
   n = int(input("Enter number to search for, -1 to quit: "))
   if n == -1 :
      done = True
   else :
      pos = binarySearch(a, 0, len(a) - 1, n)
      if pos == -1 :
         print("Not found")
      else :
         print("Found in position ", pos) 

