## 
#  This module implements a function for executing binary searches in a list.
#

## Finds a value in a range of a sorted list, using the binary search algorithm.
#  @param a the list in which to search
#  @param low the low index of the range
#  @param high the high index of the range
#  @param value the value to find
#  @return the index at which the value occurs, or -1 if it does not occur in the list
#
def binarySearch(a, low, high, value) :
   while high >= low :
      mid = (low + high) // 2

      if a[mid] < value :
         low = mid + 1
      elif a[mid] > value :
         high = mid - 1
      else :
         return mid

   return -1

