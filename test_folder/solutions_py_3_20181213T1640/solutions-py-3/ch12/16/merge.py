##
#  Implement merge sort without recursion.
#
from random import randint

def main() :
   # Generate some random data.  The number of elements is a power of 2.
   data = []
   for i in range(16):
      data.append(randint(1, 100))
   
   # Demonstrate mergeSort.
   print(data)
   mergeSort(data)
   print(data)

## Merge two regions of a list, each of which must be sorted.
#  @param a the list of elements to process
#  @param s1 the index of the beginning of the first region
#  @param s2 the index of the beginning of the second region (and as a 
#         consequence, one element beyond the end of the first region.
#  @param end the index of the last element in the second region
#
def merge(a, s1, s2, end) :
   temp = []
   i = s1
   j = s2
   while i < s2 and j <= end :
      if a[i] <= a[j] :
         temp.append(a[i])
         i = i + 1
      elif a[j] < a[i] :
         temp.append(a[j])
         j = j + 1

   while i < s2:
      temp.append(a[i])
      i = i + 1

   while j <= end :
      temp.append(a[j])
      j = j + 1

   for i in range(s1, end + 1) :
      a[i] = temp[i - s1]

## Sort elements using a non-recursive merge sort.
#  @param a the list to sort
def mergeSort(a) :
   size = 1
   while size < len(a):
      for i in range(0, len(a), size * 2) :
         merge(a, i, i + size, i + 2*size - 1)
      size = size * 2

# Call the main function.
main()

