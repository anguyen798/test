## 
#  Perform a radix sort.
#
from random import randint
from math import log10, ceil

def main() :
   # Initialize data with some random values.
   data = []
   for i in range(20) :
      data.append(randint(-999999, 999999))
   
   # Display the data before and after sorting.
   print(data)
   radixSort(data)
   print(data)
  
## Sort the list using radix sort.
#  @param a the list to sort containing arbitrary integers
#
def radixSort(a) :
   # Determine how many digits there are in the number with largest magnitude.
   mx = max(a)
   mn = min(a)
   mx = max(mx, abs(mn))
   limit = ceil(log10(mx))
   print("limit is", limit)

   # Process the needed number of digits.
   for i in range(0, limit) :
      # Sort the numbers into 19 buckets.
      values = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

      # Compute the divisor for the current digit.
      divisor = (10 ** i)

      # Place each value in the correct bucket.
      for v in a :
         index = abs(v) // divisor % 10
         if v > 0 :
            index = index + 9
         else :
            index = 9 - index
         values[index].append(v)

      # Move the numbers from the buckets back into the list.
      pos = 0
      for i in range(len(values)) :
         for j in values[i] :
            a[pos] = j
            pos = pos + 1

# Call the main function.
main()

