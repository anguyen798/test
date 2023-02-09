## 
#  The insertSort function sorts a list, using the insertion sort algorithm.
#

# Sorts a list, using insertion sort.
# @param a the list to sort
#
def insertionSort(a) :
   for i in range(1, len(a)) :
      next = a[i]

      # Move all larger elements up.
      j = i
      while j > 0 and a[j - 1] > next :
         a[j] = a[j - 1]
         j = j - 1
         
      # Insert the element.
      a[j] = next

