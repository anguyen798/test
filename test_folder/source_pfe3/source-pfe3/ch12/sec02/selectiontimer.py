##
#  This program measures how long it takes to sort a list of a 
#  user-specified size with the selection sort algorithm.
#

from random import randint
from selectionsort import selectionSort
from time import time

# Prompt the user for the list size.
n = int(input("Enter list size: "))

# Construct random list.
values = []
for i in range(n) :
   values.append(randint(1, 100))   

startTime = time()
selectionSort(values)
endTime = time()
      
print("Elapsed time: %.3f seconds" % (endTime - startTime))
