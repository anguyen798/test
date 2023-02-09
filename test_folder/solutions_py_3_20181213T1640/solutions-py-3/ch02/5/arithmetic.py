##
#  Read two integers and display the result of several calculations involving
#  them.
#

# Read the integers from the user.
a = int(input("Enter an integer: "))
b = int(input("Enter another integer: "))

# Compute and display the sum, difference, product, average, distance, 
# minimum and maximum.
print("%-12s%6d" % ("Sum:", a + b))
print("%-12s%6d" % ("Difference:", a - b))
print("%-12s%6d" % ("Product:", a * b))
print("%-12s%9.2f" % ("Average:", (a + b) / 2))
print("%-12s%6d" % ("Distance:", abs(a - b)))
print("%-12s%6d" % ("Minimum:", min(a, b)))
print("%-12s%6d" % ("Maximum:", max(a, b)))

