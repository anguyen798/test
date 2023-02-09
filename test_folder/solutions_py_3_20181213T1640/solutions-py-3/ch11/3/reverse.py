##
#  Reverse a string using recursion.
#

## Reverse the order of the characters.
#  @param s the string to reverse
#  @return a string with the characters from s in reverse order
#
def reverse(s) :
   if len(s) == 0 :
      return s
   return s[-1] + reverse(s[0 : -1])

def main() :
   # Demonstrate the reverse function.
   r = reverse("Hello!")
   print(r)
   print("Expected: !olleH")

# Call the main function.
main()

