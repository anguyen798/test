##
#  Compute the sum of all of the squares from 1 to 100 (inclusive).
#

# Generate the squares from 1 to 100 using a loop, adding each to the total.
total = 0
for i in range(1, 101) :
   total = total + i * i

# Display the result.
print("The sum of all squares from 1 to 100 is", total)

