##
#  Read two integers and display the result of several calculations involving
#  them.
#

# Read the integers from the user.
a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

# Compute and display the sum, difference, product, average, distance, 
# minimum and maximum.
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Average:", (a + b) / 2)
print("Distance:", abs(a - b))
print("Minimum:", min(a, b))
print("Maximum:", max(a, b))

