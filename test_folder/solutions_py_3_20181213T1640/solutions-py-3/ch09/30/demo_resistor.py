##
#  Demonstrate the resistor class.
#
from resistor import Resistor

r = Resistor(330, 5)
print(r.getBands())
print("Expected: Orange Orange Brown Gold")

r = Resistor(420000, 1)
print(r.getBands())
print("Expected: Yellow Red Yellow Brown")

