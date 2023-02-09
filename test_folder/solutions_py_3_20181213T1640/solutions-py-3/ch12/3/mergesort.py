##
#  The mergeSort function sorts a list, using the merge sort algorithm.
#

## Sorts a list, using merge sort.
#  @param a the list to sort
#
def mergeSort(a) :
   if len(a) <= 1 : return
   mid = len(a) // 2
   first = a[ : mid]
   second = a[mid : ]
   mergeSort(first)
   mergeSort(second)
   mergeLists(first, second, a)

## Merges two sorted list into a third list.
#  @param first the first sorted list
#  @param second the second sorted list
#  @param a the list into which to merge first and second
#
def mergeLists(first, second, a) :
   iFirst = 0   # Next element to consider in the first list.
   iSecond = 0  # Next element to consider in the second list
   j = 0        # Next open position in a.

   # As long as neither iFirst nor iSecond is past the end, move
   # the smaller element into a.
   while iFirst < len(first) and iSecond < len(second) :
      if first[iFirst] > second[iSecond] :
         a[j] = first[iFirst]
         iFirst = iFirst + 1
      else :
         a[j] = second[iSecond]
         iSecond = iSecond + 1
         
      j = j + 1

   # Note that only one of the two loops below copies entries.
   # Copy any remaining entries of the first list.
   while iFirst < len(first) : 
      a[j] = first[iFirst] 
      iFirst = iFirst + 1
      j = j + 1
         
   # Copy any remaining entries of the second list.
   while iSecond < len(second) :
      a[j] = second[iSecond] 
      iSecond = iSecond + 1
      j = j + 1

