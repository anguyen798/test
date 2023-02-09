##
#  Compute the standard deviation of a set of values entered by the user.  
#  The sentinel value -1 is used to mark the end of the set.
#
from math import sqrt

# Read the first value from the user.
inputStr = input("Enter a number (blank line to quit): ")

# Read the subseuqent values from the user, computing the sum and the sum of
# the squares.
total = 0
total_squares = 0
n = 0
while inputStr != "" :
   value = float(inputStr)
   total = total + value
   total_squares = total_squares + value * value
   n = n + 1

   inputStr = input("Enter a number (blank line to quit): ")

# Compute the standard deviation.
stddev = sqrt((total_squares - 1 / n * total * total) / (n - 1))
mean = total / n

# Display the result.
print("The mean is", mean)
print("The standard deviation is", stddev)

