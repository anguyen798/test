##
#  Display all substrings of a word, sorted by length.
#

# Read the word from the user.
word = input("Enter a word: ")

# Generate and display all substrings ordered by increasing length.
for length in range(1, len(word) + 1) :
   for pos in range(0, len(word) - length + 1) :
      print(word[pos : pos + length])

