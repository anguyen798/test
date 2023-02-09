## 
#  The insertSort function sorts a list, using the insertion sort algorithm.
#
from binarysearch import binarySearch

# Sorts a list, using insertion sort.
# @param a the list to sort
#
def insertionSort(a) :
   for i in range(1, len(a)) :
      next = a[i]

      # Find the insertion point, being careful to correctly deal with
      # repeated elements.
      insertionPoint = binarySearch(a, 0, i - 1, next)
      if insertionPoint < 0 :
         insertionPoint = -insertionPoint - 1

      # Move all larger elements up.
      j = i
      while j > insertionPoint :
         a[j] = a[j - 1]
         j = j - 1
         
      # Insert the element.
      a[j] = next

