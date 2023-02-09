##
#  Demonstrate the address class.
#
from address import Address

# Construct two address.
a = Address(2500, "University Drive", "Some City", "Some State", "12345")
b = Address(1200, "College Blvd", "Other City", "Other State", "99102", "12")

# Demonstrate the print method.
print("Address a is:")
a.print()
print()

print("Address b is:")
b.print()
print()

# Demonstrate teh comesBefore method.
print("a comes before b is", a.comesBefore(b))

