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

## Reverse a substring of the characters in s.
#  @param s the string to reverse
#  @param start the index of first character to reverse
#  @param end the index of the first character after the reversed portion
#  @return a string with the characters from s in reverse order
#
def reverseSubstring(s, start, end) :
   return s[0 : start] + reverse(s[start : end]) + s[end : ]

def main() :
   # Demonstrate the reverse function.
   r = reverseSubstring("Hello, World!", 2, 8)
   print(r)
   print("Expected: HeW ,ollorld!")

# Call the main function.
main()

