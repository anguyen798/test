##
#  Construct a dictionary that maps from letters to sets of words that contain
#  the letter.
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

# Display the contents of the dictionary.
for ch in sorted(words) :
   print("Words containing %s:" % ch.upper())
   for word in sorted(words[ch]) :
      print(" ", word)

