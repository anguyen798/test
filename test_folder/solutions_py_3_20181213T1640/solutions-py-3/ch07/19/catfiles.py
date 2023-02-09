##
#  Concatenate several input files into a single output file.
#
import sys
from sys import exit

# Verify the number of command line arguments and get the output file name.
if len(sys.argv) < 3 :
   exit("Usage: catfiles <inputfile> [inputfile] ... [inputfile] <outputfile>")
out_filename = sys.argv[len(sys.argv) - 1]

# Open the output file.
outf = open(out_filename, "w")

# Process the input files.
for filename in sys.argv[1 : len(sys.argv) - 1] :
   # Open the current file, read its contents, save its contents to the output
   # file, and close the input file.
   inf = open(filename, "r")
   content = inf.read()
   outf.write(content)
   inf.close()

# Close the output file.
outf.close()

