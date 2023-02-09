##
#  Read an integer between 1000 and 999999 from the user and display it
#  with a comma as the thousands separator.
#

# Gather input from the user.
num = int(input("Please enter an integer between 1000 and 999999: "))

# Identify the digits before and after the separator.
before = num // 1000
after = num % 1000

# Display the result.
print("%d,%03d" % (before, after))

