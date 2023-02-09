##
#  Identify all words in a file that contain all of the letters in a word
#  entered by the user.
#

# Read the file name from the user and open it.
filename = input("Enter the name of the file to open: ")
inf = open(filename, "r")

# Construct the initial dictionary.
words = {}
for ch in "abcdefghijklmnopqrstuvwxyz" :
   words[ch] = set()

# Read all of the lines from the file and add them to the dictionary.
for line in inf:
   parts = line.split()
   for word in parts :
      word = word.lower()
      for ch in words :
         if ch in word :
            words[ch].add(word)

# Read the word from the user.
letters = input("Find words contain the same letters as what word? ")

# Construct a set of words containing all of the letters.
word_set = words[letters[0]]
for ch in letters[1 : len(letters)] :
   word_set = word_set.intersection(words[ch])

# Display the words that contain all of the letters.
print("The following words contain all of the letters in", letters)
for w in sorted(word_set) :
   print(" ", w)

