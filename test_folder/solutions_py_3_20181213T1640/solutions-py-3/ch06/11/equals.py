##
#  Determine if 2 lists are equal.
#

# Define constants.
LIST_1 = [1, 2, 3]
LIST_2 = [1, 2, 3]

def main() :
   print("List 1 is", LIST_1)
   print("List 2 is", LIST_2)
   print("List 1 and List 2 are equal: ", equals(LIST_1, LIST_2))

## Determine if two lists have the same elements in the same order.
#  @param l1 the first list to consider
#  @param l2 the second list to consider
#  @return True if the lists are the same, otherwise False
#
def equals(l1, l2) :
   return l1 == l2

# Call the main function.
main()

