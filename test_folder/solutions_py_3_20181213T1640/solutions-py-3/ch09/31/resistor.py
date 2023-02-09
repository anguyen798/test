##
#  Define the resistor class.
#
from random import random

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

