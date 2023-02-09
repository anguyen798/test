##
#  Find the largest element in a list.
#

## Find the largest element in the provided list.
#  @param data the list of elements to process
#  @return the largest element in data
#
def largest(data) :
   if len(data) == 1 :
      return data[0]
   
   largestRest = largest(data[0 : -2])
   if largestRest < data[-1] :
      return data[-1]
   else :
      return largestRest

def main() :
   # Demonstrate the largest function.
   print(largest([1, 2, 3, 4, 5, 4, 3, 2, 1]))
   print("Expected: 5")

# Call the main function.
main()

