##
#  Generate 10 random permutations of the numbers 1 to 10.
#
from random import randint

# Define constants.
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NUM_PERMUTATIONS = 10

# Generate the desired number of permutations.
for i in range(0, NUM_PERMUTATIONS) :  
   temp = list(ONE_TEN)
   permutation = []

   # Select items out of the temporary list in a random order.
   while len(temp) > 0 :
      permutation.append(temp.pop(randint(0, len(temp) - 1)))

   # Display the permutation.
   print(permutation)

