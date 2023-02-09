##
#  The sort function sorts a list, using the quick sort algorithm with special
#  handling of elements equal to the pivot.
#

## Sorts a portion of a list, using quick sort with special handling of
#  equal elements.
#  @param a the list to sort
#  @param start the first index of the portion to be sorted
#  @param to the last index of the portion to be sorted
#
def quickSortEqual(a, start, to) :
   if start >= to : return
   p = partitionEqual(a, start, to)
   quickSortEqual(a, start, p)
   quickSortEqual(a, p + 1, to)

## Partitions a portion of a list, with special handling of equal elements.
#  @param a the list to partition
#  @param start the first index of the portion to be partitioned
#  @param to the last index of the portion to be partitioned
#  @return the last index of the first partition
#
def partitionEqual(a, start, to) :
   pivot = a[start]
   i = start - 1
   j = to + 1
   ei = start - 1
   ej = to + 1
   while i < j :
      i = i + 1
      while a[i] < pivot :
         i = i + 1

      j = j - 1
      while a[j] > pivot :
         j = j - 1

      if i < j :
         a[i], a[j] = a[j], a[i]
         if a[i] == pivot :
            ei = ei + 1
            a[ei], a[i] = a[i], a[ei]
         if a[j] == pivot :   
            ej = ej - 1
            a[ej], a[j] = a[j], a[ej]
         
   old_j = j
         
   # Swap elements equal to the pivot from the ends into the middle.
   ei = 0
   while a[ei] == pivot and ei < i :
      a[ei], a[i - 1] = a[i - 1], a[ei]
      ei = ei + 1
      i = i - 1

   ej = len(a) - 1
   while a[ej] == pivot and ej > j :
      a[ej], a[j + 1] = a[j + 1], a[ej]
      ej = ej - 1
      j = j + 1

   return old_j

