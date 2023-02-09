##
#  Reverse a string.
#

## Reverse the order of the characters.
#  @param s the string to reverse
#  @return a string with the characters from s in reverse order
#
def reverse(s) :
   retval = ""
   for ch in s :
      retval = ch + retval
   return retval

def main() :
   # Demonstrate the reverse function.
   r = reverse("Hello!")
   print(r)
   print("Expected: !olleH")

# Call the main function.
main()

