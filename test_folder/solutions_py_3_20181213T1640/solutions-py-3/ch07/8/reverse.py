##
#  Reverse all of the lines in a file.
#
import sys

# Read the filename from the command line and open the file.
filename = sys.argv[1]
inf = open(filename, "r")

# Read all of the lines from the file and remove the newlines.
lines = inf.readlines()

# Close the file.
inf.close()

# Open the file for writing.
outf = open(filename, "w")

# Write the lines, with each line reversed.
for line in lines :
   for i in range(len(line) - 2, -1, -1) :
      outf.write(line[i])
   outf.write("\n")
      
# Close the file.
outf.close()

