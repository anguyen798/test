##
#  Reverse a list of values.
#

def main() :
   # Demonstrate the reverse function.
   data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
   print("The original data is", data)
   reverse(data)
   print("The reversed data is", data)

## Reverse the elements in a list.
#  @param data the list of elements to reverse
#
def reverse(data) :
   for i in range(0, len(data) // 2) :
      temp = data[i]
      data[i] = data[len(data) - 1 - i]
      data[len(data) - 1 - i] = temp

# Call the main function.
main()

