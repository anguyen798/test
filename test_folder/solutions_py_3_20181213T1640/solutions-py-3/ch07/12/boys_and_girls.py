##
#  Identify names that are used for both boys and girls.
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

# Print all of the names that are common to both lists.
print("The names used for both boys and girls are: ")
for name in boys :
   if name in girls :
      print(name)

