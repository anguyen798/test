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
   if low <= high :
      mid = (low + high) // 2
      
      if a[mid] == value :
         return mid
      elif a[mid] < value :
         return binarySearch(a, mid + 1, high, value)
      else :
         return binarySearch(a, low, mid - 1, value)
         
   else :
      return -1

