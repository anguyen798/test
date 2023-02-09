##
#  Generate all substrings of a string.
#

def substrings(string) :
   # Handle the base case.  The empty string only has itself as a substring.
   if string == "" :
      return [""]
   
   # Generate all substrings beginning with the first letter of string.
   retval = []
   for i in range(1, len(string) + 1) :
      retval.append(string[0 : i])

   # Generate all of the remaining substrings using recursion.
   retval = retval + substrings(string[1 : ])

   # Return the result.
   return retval

def main() :
   print(substrings("rum"))

# Call the main function.
main()

