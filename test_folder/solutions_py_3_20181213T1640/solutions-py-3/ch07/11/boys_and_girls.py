##
#  Separate names from a single file into boys names and girls names.
#

FILENAME = "babynames2000s.txt"

# Read all of the data out of the file and store it in a list.
inf = open(FILENAME, "r")
lines = inf.readlines()
inf.close()

# Extract all the boy and girl names and store them in two lists.
boys = []
girls = []
for line in lines:
   parts = line.split()
   boys.append(parts[1])
   girls.append(parts[3])

# Save the boy list.
outf = open("boynames.txt", "w")
for name in boys:
   outf.write(name + "\n")
outf.close()

# Save the girl list.
outf = open("girlnames.txt", "w")
for name in girls:
   outf.write(name + "\n")
outf.close()

