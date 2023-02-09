## 
#  Determine whether or not a substring is present in a string using recursion.
#

## Determine whether or not text is in string.
#  @param text the text to search for
#  @param string the string to search for text
#  @return True if string is in text, False otherwise
#
def find(text, string) :
   if text.startswith(string) :
      return True
   elif len(string) < len(text) :
      return find(text[1 : ], string)
   return False

def main() :
   # Demonstrate the find function.
   print(find("Mississippi", "sip"))
   print("Expected: True")

   print(find("Mississippi", "pip"))
   print("Expected: False")

# Call the main function.
main()

