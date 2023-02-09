##
#  Swap the first and second half of a list.
#

def main() :
   # Demonstrate the swapHalves function.
   values = [9, 13, 21, 4, 11, 7, 1, 3]
   print("Before the swap, the values are: ", values)
   swapHalves(values)
   print("After the swap, the values are: ", values)

## Swap the first half of a list and the second half of a list.
#  @param values the list of values to process
#
def swapHalves(values) :
   i = 0
   j = len(values) // 2
   while i < len(values) // 2 :
      swap(values, i, j)
      i = i + 1
      j = j + 1

## Swaps the elements of a list at given positions.
#  @param a the list
#  @param i the first position
#  @param j the second position
#
def swap(a, i, j) :
   temp = a[i]
   a[i] = a[j]
   a[j] = temp

# Call the main function.
main()

