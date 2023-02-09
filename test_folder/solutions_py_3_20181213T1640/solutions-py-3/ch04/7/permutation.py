##
#  Construct and display a random permutation of a word.
#
from random import randint

# Read input from the user.
word = input("Enter a word: ")

# For each character in the word, swap two characters at random.
for count in range(len(word)) :
   i = randint(0, len(word) - 2)
   j = randint(i + 1, len(word) - 1)

   first = word[ : i]
   middle = word[i+1 : j]
   last = word[j+1 : ]

   word = first + word[j] + middle + word[i] + last

# Display the result.
print("The random permuation is", word)

