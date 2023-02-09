##
#  This program computes permutations of a string.
#

class PermutationIterator :
   ## Create a new permutation iterator.
   #  @param s the string to generate permutations of
   #
   def __init__(self, s) :
      self._s = s
      self._tailIterator = None
      self._currentPos = 0

   ## Generate the next permutation of the string.
   #  @return the next permutation as a string
   #
   def nextPermutation(self) :
      # The empty string has no permutations.
      if self._s == "":
         return ""

      # If we don't currently have a tail iterator then create it.
      if self._tailIterator == None :
         self._tailIterator = PermutationIterator(self._s[ : self._currentPos] + self._s[self._currentPos + 1 : ])

      # Get the next permutation.
      retval = self._s[self._currentPos] + self._tailIterator.nextPermutation()

      # Move to the next character if the tail iterator is out of permutations.
      if not self._tailIterator.hasMorePermutations() :
         self._tailIterator = None
         self._currentPos = self._currentPos + 1

      # Return the result.
      return retval

   ## Determine whether or not more permutations are available.
   #  @return True if more permutations are available, False otherwise.
   #
   def hasMorePermutations(self) :
      return self._currentPos < len(self._s)
      
def main() :
   # Demonstrate the PermutationIterator.
   p = PermutationIterator("eat")
   while p.hasMorePermutations() :
      print(p.nextPermutation())

# Start the program.
main()

