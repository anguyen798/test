##
#  Produce an index of all identifiers in a file.
#

def main() :
   # Read the filename from the user and open it, and read all of the lines.
   filename = input("Enter the name of a Python file: ")
   inf = open(filename, "r")
   lines = inf.readlines()
   
   # Create a dictionary to hold the line numbers for each identifier.
   positions = {}

   # Process each line, adding the line number for every identifier found.
   for i in range(0, len(lines)) :
      parts = lines[i].split()
      for p in parts :
         if isIdentifier(p) :
            if p in positions :
               positions[p].append(i + 1)
            else :
               positions[p] = [i + 1]

   # Print out all of the identifiers and their line numbers.
   for ident in sorted(positions) :
      print("%s:" % ident, positions[ident])

## Determines whether or not a string is only letters, numbers and underscores.
#  @param s the string to check
#  @return True if s is only letters, numbers and underscores, False otherwise
def isIdentifier(s) :
   for ch in s :
      if not(ch >= "A" and ch <= "Z" or ch >= "a" and ch <= "z" or ch >= "0" and ch <= "9" or ch == "_") :
         return False

   return True

# Call the main function.
main()

