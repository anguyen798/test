##
#  The selectionSort function sorts a list using the selection sort algorithm.
#

def main() :
   # Demonstrate selectionSort.
   data = [5, 3, 7, 6, 1, 0, 9, 2, 8, 4]
   selectionSort(data)
   print(data)

## Sorts a list, using selection sort.
#  @param a the list to sort
#
def selectionSort(a) :
   for i in range(len(a)) :
      maxPos = maximumPosition(a, i)
      temp = a[maxPos]  # swap the two elements
      a[maxPos] = a[i]
      a[i] = temp

## Finds the smallest element in a tail range of the list.
#  @param a the list to sort
#  @param start the first position in a to compare
#  @return the position of the smallest element in the range a[start] . . . a[len(a) - 1]
#
def maximumPosition(a, start) :
   maxPos = start
   for i in range(start + 1, len(a)) :
      if a[i] > a[maxPos] :
         maxPos = i
         
   return maxPos

# Call the main function.
main()

