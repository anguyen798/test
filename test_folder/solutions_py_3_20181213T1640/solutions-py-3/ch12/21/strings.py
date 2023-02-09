##
#  Sort a bunch of strings by their lengths.
#

def main() :
   # Read some data from the user.
   data = []
   s = input("Enter a string (empty to quit): ")
   while s != "" :
      data.append(s)
      s = input("Enter a string (empty to quit): ")
   
   # Sort the string by comparing their lengths.
   data = sorted(data, key=stringKey)
   
   # Display the result.
   print("Sorting the strings by length gives:")
   print(data)
   
## Generate a key that can be used to compare strings by length, and then by
#  lexicographic order.
#  @param s the string to generate the key for
#  @return a tuple, with the length as the first value and the string, s, as the second value
def stringKey(s) :
   return (len(s), s)

# Call the main function.
main()

