##
#  Define a class for a bug.
#

## Implement a bug that moves along a line.
class Bug :
   ## Initialize the bug at a specific position.
   #  @param initialPosition to starting position of the bug
   def __init__(self, initialPosition) :
      self._pos = initialPosition
      self._dir = 1

   ## Change the direction of the bug.
   #
   def turn(self) :
      self._dir = self._dir * -1

   ## Move the bug to a new position.
   #
   def move(self) :
      self._pos = self._pos + self._dir

   ## Get the position of the bug on the line.
   #  @return the position of the bug
   def getPosition(self) :
      return self._pos

