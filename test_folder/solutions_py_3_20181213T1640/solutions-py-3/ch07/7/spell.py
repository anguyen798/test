## 
#  Check the spelling of words in a file.
#

# Load the list of legal words.
inf = open("words", "r")
legal_words = inf.readlines()
inf.close()

# Strip the newlines from the words in the legal word list.
for i in range(0, len(legal_words)) :
   legal_words[i] = legal_words[i].rstrip()

# Read the filename from the user and open it.
filename = input("Enter the input file name: ")
inf = open(filename, "r")

# Read the lines from the file and check them.  Display any words that are 
# not legal.
print("The following words are not legal:")
for line in inf :
   for word in line.rstrip().split() :
      if word not in legal_words :
         print(word)

# Close the file.
inf.close()

