##
#  This program measures how long it takes to sort a list of a 
#  user-specified size with the two variants of the quick sort algorithm.
#

from random import randint
from quicksort import quickSort, partition
from quicksortequal import quickSortEqual, partitionEqual
from time import time

# Prompt the user for the list size.
n = int(input("Enter list size: "))

# Construct random list.
a = []
for i in range(n) :
   a.append(randint(1, 10))   

# Make a second copy of the list so that the second algorithm sorts the s
# same data.
b = list(a)

# Time the standard algorithm.
startTime = time()
quickSort(a, 0, len(a) - 1)
endTime = time()
print("Standard Elapsed time: %.3f seconds" % (endTime - startTime))

# Time the version of the algorithm with special handling for equal elements.
startTime = time()
quickSortEqual(b, 0, len(b) - 1)
endTime = time()
print("Special Equals Handling Elapsed time: %.3f seconds" % (endTime - startTime))

