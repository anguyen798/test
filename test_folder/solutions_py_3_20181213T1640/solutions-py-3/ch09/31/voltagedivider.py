##
#  Define the VoltageDivider class.
#
from resistor import Resistor

## Represent a voltage divider constructor from two resistors.
#
class VoltageDivider :
   ## Construct a new voltage divider from two resistors.
   #  @param r1 the first resistor
   #  @param r2 the second resistor
   #
   def __init__(self, r1, r2) :
      self._r1 = r1
      self._r2 = r2

   ## Get the Nominal gain for the voltage divider.
   #  @return the nominal gain of the voltage divider
   #
   def getNominalGain(self) :
      return self._r2.getNominal() / (self._r1.getNominal() + self._r2.getNominal())

   ## Get the Actual gain for the voltage divider.
   #  @return the actual gain of the voltage divider
   #
   def getActualGain(self) :
      return self._r2.getActual() / (self._r1.getActual() + self._r2.getActual())

