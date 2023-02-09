##
#  This module defines the Counter class.
#

## Models a tally counter whose value can be incremented, viewed, or reset.
#
class Counter :   
   ## Gets the current value of this counter.
   #  @return the current value   
   #
   def getValue(self) :
      return self._value

   ## Advances the value of this counter by 1.
   #
   def click(self) :
      self._value = self._value + 1
      if self._value > self._limit :
         print("Limit Exceeded")

   ## Resets the value of this counter to 0.
   #
   def reset(self) :
      self._value = 0

   ## Set the limit for the counter.
   #
   def setLimit(self, maximum) :
      self._limit = maximum

