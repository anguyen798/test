##
#  Copy a file, with the file names provided on the command line.
#

import sys

# Collect the file names from the command line.
input_name = sys.argv[1]
output_name = sys.argv[2]

# Open the files.
inf = open(input_name, "r")
outf = open(output_name, "w")

# Read the data from the input file and save it in the output file.
data = inf.read()
outf.write(data)

# Close the files.
inf.close()
outf.close()

