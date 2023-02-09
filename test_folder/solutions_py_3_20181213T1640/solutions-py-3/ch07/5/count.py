##
#  Count the number of characters, words and lines in a file.
#

# Read the file name from the user and open the file.
filename = input("Enter the input file name: ")
inf = open(filename, "r")

# Count the number of characters, words and lines.
chars = 0
words = 0
lines = 0

for line in inf :
   chars = chars + len(line)
   words = words + len(line.split())
   lines = lines + 1

# Close the file.
inf.close()

# Display the results.
print("The file contains", chars, "characters,", words, "words and", lines, "lines")

