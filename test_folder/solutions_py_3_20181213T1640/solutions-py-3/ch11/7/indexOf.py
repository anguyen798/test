## 
#  Determine the position of a substring in a string.
#

## Determine whether or not text is in string, and the index.
#  @param text the text to search for
#  @param string the string to search for text
#  @param index the current index within the string
#  @return the index at which string appears in text, or -1 if it is not 
#
def indexHelper(text, string, index) :
   if text.startswith(string) :
      return index
   elif len(string) < len(text) :
      return indexHelper(text[1 : ], string, index + 1)
   return -1

## Determine the index at which a substring occurs in a string.
#  @param text the text to search for
#  @param string the string to search for text
#  @return the index at which string appears in text, or -1 if it is not 
#
def indexOf(text, string) :
   return indexHelper(text, string, 0)

def main() :
   # Demonstrate the find function.
   print(indexOf("Mississippi", "sip"))
   print("Expected: 6")

   print(indexOf("Mississippi", "pip"))
   print("Expected: -1")

# Call the main function.
main()

