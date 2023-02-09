##
#  This program measures how long it takes to sort a list of a 
#  user-specified size with the selection sort algorithm.
#

from random import randint
from selectionsort import selectionSort
from time import time

print("%10s%10s" % ("n", "Seconds"))
for n in range(10000, 60001, 10000) :
   # Construct random list.
   a = []
   for i in range(n) :
      a.append(randint(1, 100))   
   
   startTime = time()
   selectionSort(a)
   endTime = time()
         
   print("%10d%10d" % (n, endTime - startTime))

