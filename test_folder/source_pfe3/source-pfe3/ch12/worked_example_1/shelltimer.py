##
#  This program measures how long it takes to sort a list of a 
#  user-specified size with the Shell sort algorithm.
#

from random import randint
from time import time
from shellsort import shellSort
from quicksort import quickSort
from insertionsort import insertionSort

# Obtain list size.
n = int(input("Enter list size: "))

# Construct random lists.
values = []
for i in range(n) :
   values.append(randint(1, 100))   
values2 = list(values)
values3 = list(values)

startTime = time()
shellSort(values)
endTime = time()
      
print("Elapsed time with Shell sort: %.3f seconds" 
   % (endTime - startTime))

startTime = time()
quickSort(values2, 0, n - 1)
endTime = time()
      
print("Elapsed time with quicksort: %.3f seconds" 
   % (endTime - startTime))

for i in range(n) :
   if values[i] != values2[i] :
      raise RuntimeError("Incorrect sort result.") 
      
startTime = time()
insertionSort(values3)
endTime = time()

print("Elapsed time with insertion sort: %.3f seconds" 
   % (endTime - startTime))
