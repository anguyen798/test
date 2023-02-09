##
#  Compute the resistance of a piece of wire.
#
from math import pi

# Define constant variables.
COPPER_RESISTIVITY = 1.678e-8
ALUMINUM_RESISTIVITY = 2.82e-8

def main() :
   length = float(input("Enter the length of a piece of wire: "))
   gauge = float(input("Enter its gauge: "))

   print("For copper wire, the resistance is", \
         copperWireResistance(length, gauge))
   print("For aluminum wire, the resistance is", \
         aluminumWireResistance(length, gauge))

## Compute the diameter of a piece of wire from its gauge.
#  @param wireGauge the gauge of the wire
#  @return the diameter of the wire
#
def diameter(wireGauge) :
   return 0.127 * 92 ** ((36 - wireGauge) / 39)

## Compute the resistence of a length of copper wire.
#  @param length the length of the wire
#  @param wireGauge the gauge of the wire
#
def copperWireResistance(length, wireGauge) :
   r = 4 * COPPER_RESISTIVITY * length / (pi * diameter(wireGauge) ** 2)
   return r

## Compute the resistence of a length of aluminum wire.
#  @param length the length of the wire
#  @param wireGauge the gauge of the wire
#
def aluminumWireResistance(length, wireGauge) :
   r = 4 * ALUMINUM_RESISTIVITY * length / (pi * diameter(wireGauge) ** 2)
   return r

# Call the main function.
main()

