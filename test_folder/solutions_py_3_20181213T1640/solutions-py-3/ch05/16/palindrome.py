##
#  Display whether or not a string is a palidrome.
#

def main() :
   inputStr = input("Enter a string: ")
   if isPalindrome(inputStr) :
      print("That's a palindrome.")
   else:
      print("That isn't a palindrome.")

## Determine whether or not a string is a palindrome.
#  @param string the characters to check 
#  @return True if the string is a palindrome, False otherwise
#
def isPalindrome(string) :
   if len(string) <= 1 :
      return True
   if string[0] == string[len(string) - 1] :
      return isPalindrome(string[1:len(string) - 1])
   else :
      return False

# Call the main function.
main()

