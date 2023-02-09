##
#  Compute the interest earned during the first 3 months of an investment.
#

# Read input from the user.
balance = float(input("Initial balance: "))
rate = float(input("Annual interest rate in percent: "))

# Compute and display the interest.
monthly_rate = rate / 12 / 100

balance = balance + balance * monthly_rate
print("After first month:  %10.2f" % balance)

balance = balance + balance * monthly_rate
print("After second month: %10.2f" % balance)

balance = balance + balance * monthly_rate
print("After third month:  %10.2f" % balance)

