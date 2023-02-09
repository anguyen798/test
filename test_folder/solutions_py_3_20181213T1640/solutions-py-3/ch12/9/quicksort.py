##
#  The sort function sorts a list, using the quick sort algorithm.
#

## Sorts a portion of a list, using quick sort.
#  @param a the list to sort
#  @param start the first index of the portion to be sorted
#  @param to the last index of the portion to be sorted
#
def quickSort(a, start, to) :
   if start >= to : return
   p = partition(a, start, to)
   quickSort(a, start, p)
   quickSort(a, p + 1, to)

## Partitions a portion of a list.
#  @param a the list to partition
#  @param start the first index of the portion to be partitioned
#  @param to the last index of the portion to be partitioned
#  @return the last index of the first partition
#
def partition(a, start, to) :
   pivot = a[start]
   i = start - 1
   j = to + 1
   while i < j :
      i = i + 1
      while a[i] < pivot :
         i = i + 1
      j = j - 1
      while a[j] > pivot :
         j = j - 1
      if i < j :
         a[i], a[j] = a[j], a[i]
   return j

