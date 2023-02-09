##
#  Compute the sum of all odd integers between a and b.
#

# Gather input from the user.
a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

# If a is even, then the first number we want to include in the total is a + 1.
# If a is odd, then the first number we want to include in the total is a.
if a % 2 == 0 :
   first_num = a + 1
else :
   first_num = a

# Use a loop to generate the odd numbers from a to b (inclusive), adding each
# to the total.
total = 0
for i in range(first_num, b + 1, 2) :
   total = total + i

# Display the result.
print("The total of the odd numbers from", a, "to", b, "is", total)

