##
#  This program demonstrates the insertion sort algorithm.
#

from random import randint
from insertionsort import insertionSort
from time import time

n = int(input("How many elements? "))
a = []
for i in range(n) :
   a.append(randint(1, 100))   

startTime = time()
insertionSort(a)
endTime = time()

print("Elapsed time: %.3f seconds" % (endTime - startTime))

