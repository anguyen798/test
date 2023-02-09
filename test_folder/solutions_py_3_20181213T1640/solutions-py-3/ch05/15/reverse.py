##
#  Display the characters in a string in reverse order.
#

def main() :
   inputStr = input("Enter a string: ")
   print(reverse(inputStr))

## Reverse the characters in a string.
#  @param string the string to reverse
#  @returns a string holding the characters in the reverse order
#
def reverse(string) :
   if string != "":
      return string[len(string) - 1] + reverse(string[0 : len(string) - 1])
   return ""

# Call the main function.
main()

