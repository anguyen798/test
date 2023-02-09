##
#  Display the middle character(s) in a string.
#

def main() :
   inputStr = input("Enter a string: ")
   print("The middle character(s) is/are:", middle(inputStr))

## Identify and return the middle characters in a string, returning the middle
#  character if the length of the string is odd, or the middle 2 characters 
#  if the length of the string is even.
#  @param string the string of characters to process
#  @return the middle character or characters
#
def middle(string) :
   if len(string) == 0 :
      return ""
   elif len(string) % 2 == 0 :
      return string[len(string) // 2 - 1] + string[len(string) // 2]
   else :
      return string[len(string) // 2]

# Call the main function.
main()

