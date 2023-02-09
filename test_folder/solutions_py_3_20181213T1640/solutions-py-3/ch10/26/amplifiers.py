##
#  Classes to represent various types of amplifiers.
#

## A class to represent a generic amplifier.
#
class Amplifier :
   ## Construct a new amplifier.
   #  @param r1 the resistance of the first resistor.
   #  @param r2 the resistance of the second resistor.
   #
   def __init__(self, r1, r2) :
      self._r1 = r1
      self._r2 = r2

   ## Compute and return the amplifier's gain.
   #  @return the gain of the amplifier
   def getGain(self) :
      raise NotImplementedError

   ## Compute and return the description of the amplifier.
   #  @return a string describing the amplifier
   def getDescription(self) :
      return "A generic amplifier"

## Represent a noninverting amplifier.
class Noninverting(Amplifier) :
   ## Construct a new noninverting amplifier.
   #  @param r1 the resistance of the first resistor.
   #  @param r2 the resistance of the second resistor.
   #
   def __init__(self, r1, r2) :
      super().__init__(r1, r2)

   ## Compute and return the amplifier's gain.
   #  @return the gain of the amplifier
   #
   def getGain(self) :
      return 1 + self._r2 / self._r1

   ## Compute and return the description of the amplifier.
   #  @return a string describing the amplifier
   def getDescription(self) :
      return "Noninverting amplifier"

## Represent an inverting amplifier.
class Inverting(Amplifier) :
   ## Construct a new inverting amplifier.
   #  @param r1 the resistance of the first resistor.
   #  @param r2 the resistance of the second resistor.
   #
   def __init__(self, r1, r2) :
      super().__init__(r1, r2)

   ## Compute and return the amplifier's gain.
   #  @return the gain of the amplifier
   #
   def getGain(self) :
      return -self._r2 / self._r1

   ## Compute and return the description of the amplifier.
   #  @return a string describing the amplifier
   def getDescription(self) :
      return "Inverting amplifier"

## Represent a voltage divider amplifier.
class VoltageDivider(Amplifier) :
   ## Construct a new noninverting amplifier.
   #  @param r1 the resistance of the first resistor.
   #  @param r2 the resistance of the second resistor.
   #
   def __init__(self, r1, r2) :
      super().__init__(r1, r2)

   ## Compute and return the amplifier's gain.
   #  @return the gain of the amplifier
   #
   def getGain(self) :
      return self._r2 / (self._r1 + self._r2)

   ## Compute and return the description of the amplifier.
   #  @return a string describing the amplifier
   def getDescription(self) :
      return "Voltage divider amplifier"

