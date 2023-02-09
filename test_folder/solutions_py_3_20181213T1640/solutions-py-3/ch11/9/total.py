##
#  Compute the sum of all the elements in a list.
#

## Compute the sum of the elements in a list.
#  @param data the list of data values to sum
#  @return the sum of all of the elements in the list
# 
def total(data) :
   if len(data) == 1 :
      return data[0]
   return data[0] + total(data[1 : ])

def main() :
   # Demonstrate the total function.
   print(total([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
   print("Expected: 55")

# Call the main function.
main()

