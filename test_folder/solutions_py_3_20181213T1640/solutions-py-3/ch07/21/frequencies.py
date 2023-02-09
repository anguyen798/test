##
#  Compute the letter frequencies for a file.
#

# Get the file name from the user and open the file.
filename = input("Enter the name of a file: ")
inf = open(filename, "r")

# Process every character in the file, recording the counts.
counts = [0] * 26
for line in inf :
   for ch in line :
      if ch >= "A" and ch <= "Z" :
         counts[ord(ch) - ord("A")] = counts[ord(ch) - ord("A")] + 1
      if ch >= "a" and ch <= "z" :
         counts[ord(ch) - ord("a")] = counts[ord(ch) - ord("a")] + 1
         
# Display the table of percentages.
for i in range(7) :
   for j in range(5) :
      index = j * 7 + i
      if index < 26 :
         print("%s: %4.1f" % (chr(index + ord("A")), counts[index] / sum(counts) * 100), end="   ")
   print()

