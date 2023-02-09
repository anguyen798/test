##
#  Compute how much a worker is paid.
#

# Define constants.
OT_LIMIT = 40
OT_FACTOR = 1.5

# Read input from the user.
name = input("Enter employee name: ")
rate = float(input("Enter the hourly rate: "))
hours = float(input("Enter the number of hours worked: "))

# Compute the pay amount.
if hours <= OT_LIMIT :
   pay = rate * hours
else :
   pay = rate * OT_LIMIT + rate * (hours - OT_LIMIT) * OT_FACTOR

# Display the result.
print("Employee: ", name)
print("The pay will be $%.2f for %.1f hours of work." % (pay, hours))

