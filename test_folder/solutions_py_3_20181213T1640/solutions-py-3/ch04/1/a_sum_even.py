##
#  Use a loop to sum the even numbers from 2 to 100 (inclusive).
#

# Generate the even number from 2 to 100 inclusive, and add each to the total.
total = 0
for i in range(2, 101, 2) :
   total = total + i

# Display the result.
print("The total of the even numbers from 2 to 100 is", total)

