##
#  Find occurrences of a word in several files.
#
import sys

# Extract the target from the command line.
target = sys.argv[1]

# For each filename on the command line.
for i in range(2, len(sys.argv)) :
   # Save the filename and open the file.
   filename = sys.argv[i]
   inf = open(filename, "r")

   # Search each line in the file for the target.
   for line in inf :
      if target in line :
         print("%s: %s" % (filename, line), end="")

   # Close the file.
   inf.close()

