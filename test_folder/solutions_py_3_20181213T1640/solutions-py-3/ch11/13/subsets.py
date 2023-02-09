##
#  Compute the subsets of a string.
#

## Generate all subsets of a string.
#  @param string the string to compute the subset of
#  @return a list of all subsets of the provided string
#
def subsets(string) :
   # Handle the simplest case, which is the empty string.
   if len(string) == 0 :
      return [string]
   
   # Get all the subsets of the tail.
   shorter = subsets(string[1 : ])

   # Generate a new copy of the tail subsets and append the first
   # character to all of them.
   longer = list(shorter)
   for i in range(len(longer)) :
      longer[i] = string[0] + longer[i]

   # Return the tail subset and the subset including the first character.
   return shorter + longer

def main() :
   # Demonstrate the subsets function.
   print(sorted(subsets("rum"), key=len, reverse=True))

# Call the main function.
main()

