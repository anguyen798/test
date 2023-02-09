##
#  Read a file and save it to a new file with line numbers.
#
import sys

# Read the input file name from the user if it wasn't provided as a command
# line argument.
if len(sys.argv) < 2 :
   inputName = input("Enter the input file name: ")
else :
   inputName = sys.argv[1]

# Read the output file name from the user if it wasn't provided as a command
# line argument.
if len(sys.argv) < 3 :
   outputName = input("Enter the ouput file name: ")
else :
   outputName = sys.argv[2]

# Open the input and output file names.
inf = open(inputName, "r")
outf = open(outputName, "w")

# Read lines from the file and save them to a new file with line numbers.
number = 1
for line in inf :
   outf.write("/* " + str(number) + " */ " + line)
   number = number + 1

# Close the files.
inf.close()
outf.close()

