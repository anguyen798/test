##
#  Compute the sums of two columns of numbers stored in a file.
#

# Read the filename from the user and open the file.
filename = input("Enter the input file name: ")
inf = open(filename, "r")

# Read the lines from the file and average them.
total_1 = 0
total_2 = 0
count = 0
for line in inf :
   parts = line.split()
   total_1 = total_1 + float(parts[0])
   total_2 = total_2 + float(parts[1])
   count = count + 1

# Close the file.
inf.close()

# Display the result.
print("The averages are %.2f and %.2f." % (total_1 / count, total_2 / count))

