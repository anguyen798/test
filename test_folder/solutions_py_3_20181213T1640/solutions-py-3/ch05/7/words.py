##
#  Use a function to count the number of words in a string.
#

def main() :
   inputStr = input("Enter a string: ")
   print("The string contains", countWords(inputStr), "words")

## Count the number of words in a string.
#  @param string the string of characters to process
#  @return the number of words
#
def countWords(string) :
   # Remove any leading or trailing spaces to make counting easier.
   string = string.strip()

   # Handle the empty string as a special case.
   if string == "" :
      return 0

   # Count the spaces to count the number of words.
   count = 1
   for ch in string :
      if ch == " " :
         count = count + 1
   return count

# Call the main function.
main()

