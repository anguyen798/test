##
#  Determine if two lists contain the same values in any order.
#

# Define constants.
LIST_1 = [1, 2, 1, 1, 2]
LIST_2 = [1, 1, 1, 2, 2]

def main() :
   print("List 1 is", LIST_1)
   print("List 2 is", LIST_2)
   print("The lists contain the same elements: ", sameElements(LIST_1, LIST_2))

## Determine if two lists contain the same elements in any order.
#  @param l1 the first list to consider
#  @param l2 the second list to consider
#  @return True if the lists contain the same elements, False otherwise
#
def sameElements(l1, l2) :
   if len(l1) != len(l2) :
      return False

   for value in l1 :
      if count(l1, value) != count(l2, value) :
         return False
   return True

## Count the number of times that value appears in data.
#  @param data the list of values to check
#  @param value the value to count the number of occurrences of
#  @return the number of times value appears in data
#
def count(data, value) :
   total = 0
   for v in data :
      if value == v :
         total = total + 1
   return total

# Call the main function.
main()

