##
#  Implement bubblesort.
#

def main() :
   data = [1, 5, 7, 8, 4, 2, 3, 0, 9, 6]

   print(data)
   bubbleSort(data)
   print(data)

## Sorts a list, using bubble sort.
# @param a the list to sort
#
def bubbleSort(a) :
   sorted = False
   while not sorted :
      sorted = True
      for i in range(0, len(a) - 1) :
         if a[i] > a[i + 1] :
            swapElements(a, i, i + 1)
            sorted = False

## Swap two elements in a list.
# @param a the list to modify
# @param i the index of the first element
# @param j the index of the second element
#
def swapElements(a, i, j) :
   temp = a[j]
   a[j] = a[i]
   a[i] = temp

# Call the main function.
main()

