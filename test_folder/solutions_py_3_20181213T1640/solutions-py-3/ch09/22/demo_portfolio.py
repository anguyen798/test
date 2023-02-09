##
#  Demonstrate the portfolio class.
#
from portfolio import Portfolio

# Create a portfolio.
p = Portfolio()

# Perform several transactions.
p.deposit(500, "S")
p.deposit(1100, "C")
p.withdraw(100, "C")
p.withdraw(100, "S")
p.transfer(500, "C")

# Verify that the balances are as expected.
print("%.2f" % p.getBalance("S"))
print("Expected: 900.00")
print("%.2f" % p.getBalance("C"))
print("Expected: 500.00")

