##
#  Demonstrate the customer class.
#
from customer import Customer

# Create the customer.
bob = Customer()

# Make some purchases and check the discount status.
bob.makePurchase(50, 1)
bob.makePurchase(45, 9)
print(bob.discountReached())
print("Expected: False")

# Make an additional purchase and check the discount status.
bob.makePurchase(45, 9)
print(bob.discountReached())
print("Expected: False")

# Make an additional purchase and check the discount status.
bob.makePurchase(10, 20)
print(bob.discountReached())
print("Expected: True")

