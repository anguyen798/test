##
#  Implement a Moth class.
#

##  Model a moth that flies in a straight line.
#
class Moth :
   ## Construct a new moth with an initial position.
   #  @param initialPosition the initial position of the moth
   #
   def __init__(self, initialPosition) :
      self._pos = initialPosition

   ## Move the moth toward a light source.
   #  @param lightPosition the position of the light
   #
   def moveToLight(self, lightPosition) :
      distance = lightPosition - self._pos
      distance = distance / 2
      self._pos = self._pos + distance

   ## Get the position of the moth.
   #  @return the position of the moth
   def getPosition(self) :
      return self._pos

