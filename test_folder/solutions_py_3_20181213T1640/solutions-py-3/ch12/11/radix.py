## 
#  Perform a radix sort.
#
from random import randint

def main() :
   # Initialize data with some random values.
   data = []
   for i in range(20) :
      data.append(randint(0, 999))
   
   # Display the data before and after sorting.
   print(data)
   radixSort(data)
   print(data)

## Sort the list using radix sort and only a single auxiliary list.
#  @param a the list to sort, must be integers between 0 and 999
#
def radixSort(a) :
   for i in range(0, 10) :
      # Sort the numbers into 2 buckets but adding at the correct location.
      values = []

      # Compute the divisor for the current digit.
      divisor = (2 ** i)

      # Place each value at the correct position in the bucket.
      pos = 0
      for v in a :
         if (v // divisor) % 2 == 0:
            values.insert(pos, v)
            pos = pos + 1
         else :
            values.append(v)

      # Move the numbers from the buckets back into the list.
      for i in range(len(values)) :
         a[i] = values[i]
         
# Call the main function.
main()

