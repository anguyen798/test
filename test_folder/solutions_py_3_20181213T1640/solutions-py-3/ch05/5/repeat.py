##
#  Repeat a string a number of times with a delimiter between each occurrence.
#

def main() :
   inputStr = input("Enter a string: ")
   count = int(input("How many repetitions? "))
   delimiter = input("Separated by? ")

   print(repeat(inputStr, count, delimiter))

## Repeat a string n times, with each repetition seperated by delim.
#  @param string the string of characters to repeat
#  @param n the number of repetitions
#  @param delim the delimiter between each repetition
#  @return the repeated string with delimiters
#
def repeat(string, n, delim) :
   retval = string
   for i in range(1, n) :
      retval = retval + delim + string

   return retval

# Call the main function.
main()

