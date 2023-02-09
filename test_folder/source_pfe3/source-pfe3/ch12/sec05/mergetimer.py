##
#  This program measures how long it takes to sort a list of a 
#  user-specified size with the merge sort algorithm.
#

from random import randint
from mergesort import mergeSort
from time import time

# Prompt the user for the list size.
n = int(input("Enter list size: "))

# Construct random list.
values = []
for i in range(n) :
   values.append(randint(1, 100))   

startTime = time()
mergeSort(values)
endTime = time()
      
print("Elapsed time: %.3f seconds" % (endTime - startTime))
