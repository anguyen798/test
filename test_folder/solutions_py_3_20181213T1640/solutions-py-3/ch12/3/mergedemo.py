##
#  This program demonstrates the merge sort algorithm by
#  sorting a list that is filled with random numbers.
#

from random import randint
from mergesort import mergeSort

n = 20
a = []
for i in range(n) :
   a.append(randint(1, 100))   
print(a)
mergeSort(a)
print(a)

