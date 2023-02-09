##
#  Copy the lines from one file into another so that they are in reverse
#  order.
#
import sys

# Read the input file name from the command line and open the input file.
inputFile = sys.argv[1]
inf = open(inputFile, "r")

# Read the lines from the input file.
lines = inf.readlines()

# Close the input file.
inf.close()

# Read the output file name from the command line and open the output file.
outputFile = sys.argv[2]
outf = open(outputFile, "w")

# Write the lines in reverse order.
for i in range(len(lines) - 1, -1, -1) :
   outf.write(lines[i])

# Close the output file.
outf.close()

