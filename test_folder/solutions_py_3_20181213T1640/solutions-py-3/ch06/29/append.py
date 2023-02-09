##
#  Append one list to another.
#

def main() :
   # Create two sample lists.
   list_1 = [1, 2, 3]
   list_2 = [4, 5, 6]

   # Demonstrate that appendList works correctly.
   print("List 1 is", list_1)
   print("List 2 is", list_2)
   merged = appendList(list_1, list_2)
   print("The merged list is", merged)

## Append one list to another.
#  @param a the first list
#  @param b the second list
#
def appendList(a, b) :
   return a + b

# Call the main function.
main()

