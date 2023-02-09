##
#  Demonstrate the resistor class.
#
from resistor import Resistor

# Create ten 330 ohm resistors, display the nominal and actual values.
for i in range(0, 10) :
   r = Resistor(330, 10)
   print("Nominal: %.1f   Actual: %.1f" % (r.getNominal(), r.getActual()))

