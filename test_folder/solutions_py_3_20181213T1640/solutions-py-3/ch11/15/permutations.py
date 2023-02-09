## 
#  Generate all permutations of a string without using recursion.
#

def main() :
   # Demonstrate the iterative permutations function.
   for s in permutations("eat"):
      print(s)

## Collect all of the characters at given indices into a new string.
#  @param string the string to collect the characters from
#  @param indices the indices of the characters to collect
#  @return all of the characters from string at the indicated indices 
#
def collectCharacters(string, indices) :
   temp = ""
   for i in indices :
      temp = temp + string[i]
   return temp

## Generate all permutations of a string.
#  @param s the string to generate the permutations of
#  @return a list of all permutations of s
#
def permutations(s) :
   a = list(range(len(s)))
   retval = []
   retval.append(collectCharacters(s, a))
   while nextPermutation(a) :
      retval.append(collectCharacters(s, a))
   return retval

#
# The remaining code is from the question without any changes (except for the
# call to main, which is at the end of the file).
#

def nextPermutation(a) :
   i = len(a) - 1
   while i > 0 :
      if a[i - 1] < a[i] :
         j = len(a) - 1
         while a[i - 1] > a[j] :
            j = j - 1
         swap(a, i - 1, j)
         reverse(a, i, len(a) - 1)
         return True
      i = i - 1
   return False

def reverse(a, i, j) :
   while i < j :
      swap(a, i, j)
      i = i + 1
      j = j - 1

def swap(a, i, j) :
   temp = a[i]
   a[i] = a[j]
   a[j] = temp

# Call the main function.
main()

