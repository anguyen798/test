##
#  Compute the sum of the odd digits in an integer.
#

# Read the input from the user as a string.
digits = input("Enter an integer: ")

# Check each character in the string.  Begin by converting it to an integer.
# If it is an odd digit, then add it to the total.
total = 0
for ch in digits :
   n = int(ch)
   if n % 2 == 1 :
      total = total + n

# Display the result.
print("The total of the odd digits in", digits, "is", total)

