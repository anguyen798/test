##
#  Print all of the words that are common to two files.
#

def main() :
   # Read the words out of two files.
   words1 = fileWords()
   words2 = fileWords()
   
   # Construct a set containing the words common to both files.
   common = words1.intersection(words2)
   
   # Display the words in alphabetical order.
   print("The words that are common to both files.")
   for word in sorted(common) :
      print(" ", word)
   
## Read all of the words in a file (name provided by the user) into a set.
#  @return the set of all words in a file
def fileWords() :
   # Read the filename and open the file.
   filename = input("Enter the name of a file: ")
   inf = open(filename, "r")

   # Add all of the words to a dictionary.
   words = set()
   for line in inf :
      parts = line.split()
      for word in parts :
         words.add(word)

   return words
   
# Call the main function.
main()

