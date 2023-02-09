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
   # Use the middle element of a short list as the pivot.
   if len(a) <= 7 :
      pivot = a[start + (to - start) // 2]
   # Use the median of the first, middle and last elements of a medium length
   # list as the pivot.
   elif len(a) <= 40 :
      pivot = med(a[start], a[start + (to - start) // 2], a[to])
   # Use the pseudomedian of nine values for long lists as the pivot.
   else :
      factor = to - start
      pivot = med(med(a[0 * factor // 8 + start], \
                      a[1 * factor // 8 + start], \
                      a[2 * factor // 8 + start]), \
                  med(a[3 * factor // 8 + start], \
                      a[4 * factor // 8 + start], \
                      a[5 * factor // 8 + start]), \
                  med(a[6 * factor // 8 + start], \
                      a[7 * factor // 8 + start], \
                      a[8 * factor // 8 + start]))
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

## Compute the median of three values.
#  @param a the first value
#  @param b the second value
#  @param c the third value
#  @return the middle of the three values
#
def med(a, b, c) :
   mn = min(a, b, c)
   mx = max(a, b, c)
   md = a + b + c - mn - mx
   return md

