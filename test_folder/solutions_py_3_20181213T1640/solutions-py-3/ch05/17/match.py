##
#  Use recursion to determine if one string is within another.
#

def main() :
   print("find(\"Mississippi\", \"sip\") returned", find("Mississippi", "sip"))
   print("find(\"Mississippi\", \"sips\") returned", find("Mississippi", "sips"))
   print("find(\"Mississippi\", \"p\") returned", find("Mississippi", "p"))
   print("find(\"Mississippi\", \"q\") returned", find("Mississippi", "q"))

## Determine if match occurs anywhere in the string.
#  @param string the string to search
#  @param match the string that we are looking for
#  @return True if match occurs anywhere in string, otherwise False
#
def find(string, match) :
   if string.startswith(match) == True :
      return True
   elif len(string) >= len(match) :
      return find(string[1 : len(string)], match)
   else :
      return False

# Call the main function.
main()

