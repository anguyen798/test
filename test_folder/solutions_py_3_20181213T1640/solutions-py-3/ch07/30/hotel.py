##
#  Separate the lines of a file into different files for each service
#  category.
#
from sys import exit

# Read the filename from the user.
filename = input("Enter the name of the file to process: ")

# Open the file.
try :
   inf = open(filename, "r")
except :
   exit("That file couldn't be opened.")

# Read the lines, copying each into the approrpiate file.
for line in inf :
   # Construct the output file name.
   parts = line.split(";")
   filename = parts[1] + ".txt"

   # Open the output file and add the line to the end of it.
   outf = open(filename, "a")
   outf.write(line)
   outf.close()

# Close the file.
inf.close()

