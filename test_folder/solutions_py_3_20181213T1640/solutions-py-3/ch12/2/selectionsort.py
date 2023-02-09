##
#  The selectionSort function sorts a list using the selection sort algorithm.
#

## Sorts a list, using selection sort.
#  @param a the list to sort
#
def selectionSort(a) :
   for i in range(len(a)) :
      minPos = minimumPosition(a, i)
      temp = a[minPos]  # swap the two elements
      a[minPos] = a[i]
      a[i] = temp

## Finds the smallest element in a tail range of the list.
#  @param a the list to sort
#  @param start the first position in a to compare
#  @return the position of the smallest element in the range a[start] . . . a[len(a) - 1]
#
def minimumPosition(a, start) :
   minPos = start
   for i in range(start + 1, len(a)) :
      if a[i] < a[minPos] :
         minPos = i
         
   return minPos

