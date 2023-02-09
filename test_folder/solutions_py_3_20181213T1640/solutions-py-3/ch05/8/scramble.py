##
#  Use a function to scramble the order of two characters within a string.
#
from random import randint

def main() :
   inputStr = input("Enter a string (blank to quit): ")
   while inputStr != "" :
      print(scramble(inputStr))
      inputStr = input("Enter a string (blank to quit): ")

## Scramble the order of two characters in a string.
#  @param word the string of characters to process
#  @return the scrambled version of the word 
#
def scramble(word) :
   # Handle strings that are too short to scramble.
   if len(word) <= 3 :
      return word 

   # Pick two random positions that aren't the first or last character.
   first = randint(1, len(word) - 3)
   second = randint(first + 1, len(word) - 2)

   # Switch the characters as positions first and last and return the result.
   return word[0 : first] + word[second] + word[first + 1 : second] + \
          word[first] + word[second + 1 : len(word)]

# Call the main function.
main()

