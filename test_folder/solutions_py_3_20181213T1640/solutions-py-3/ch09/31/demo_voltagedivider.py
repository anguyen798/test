##
#  Demonstrate the VoltageDivder class.
#
from resistor import Resistor
from voltagedivider import VoltageDivider

for i in range(0, 10) :
   r1 = Resistor(250, 5)
   r2 = Resistor(750, 5)
   v = VoltageDivider(r1, r2)

   print("Nominal: %.3f   Actual: %.3f" % (v.getNominalGain(), v.getActualGain()))

