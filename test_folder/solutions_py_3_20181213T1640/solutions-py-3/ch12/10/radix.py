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
  
## Sort the list using radix sort.
#  @param a the list to sort, must be integers between 0 and 999
#
def radixSort(a) :
   for i in range(0, 3) :
      # Sort the numbers into 10 buckets.
      values = [[], [], [], [], [], [], [], [], [], []]

      # Compute the divisor for the current digit.
      divisor = (10 ** i)

      # Place each value in the correct bucket.
      for v in a :
         values[(v // divisor) % 10].append(v)

      # Move the numbers from the buckets back into the list.
      pos = 0
      for i in range(10) :
         for j in values[i] :
            a[pos] = j
            pos = pos + 1

# Call the main function.
main()

