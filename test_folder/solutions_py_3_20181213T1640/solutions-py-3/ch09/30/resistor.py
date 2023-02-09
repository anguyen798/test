##
#  Define the resistor class.
#
from random import random
from math import log10

## Represent a resistor nominal and actual values.
#
class Resistor :
   ## Construct a new resistor with the provided nominal value.
   #  @param nominal the nominal value of the resistor
   #  @param tolerance the tolerance of the resistor
   #
   def __init__(self, nominal, tolerance) :
      self._tolerance = tolerance
      self._nominal = nominal
      self._actual = self._nominal * (1 - tolerance / 100)  + \
                     self._nominal * (2 * tolerance / 100) * random()

   ## Get the actual resistance of the resistor.
   #  @return the actual resistance of the resistor
   #
   def getActual(self) :
      return self._actual

   ## Get the nominal resistance of the resistor.
   #  @return the nominal ressitance of the resistor
   def getNominal(self) :
      return self._nominal

   ## Get the tolerance of the resistor.
   #  @return the tolerance of the resistor
   def getTolerance(self) :
      return self._tolerance

   ## Get the color bands for the resistor.
   #  @return a tuple of 4 band colors
   #
   def getBands(self) :
      COLORS = ["Black", "Brown", "Red", "Orange", "Yellow", "Green", "Blue", 
                  "Violet", "Gray", "White"]
      TOLERANCES = {20: "None", 10: "Silver", 5: "Gold", 0.05: "Gray", 
                     0.1: "Violet", 0.25: "Blue", 0.5: "Green", 2: "Red", 
                     1: "Brown"}

      first = COLORS[int(str(self._nominal)[0])]
      second = COLORS[int(str(self._nominal)[1])]
      third = COLORS[int(log10(self._nominal) - 1)]
      fourth = TOLERANCES[self._tolerance]

      return (first, second, third, fourth)

