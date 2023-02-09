##
#  Define a cone class.
#
from math import pi, sqrt

## A class that stores the radius and height of a cone.
#
class Cone :
   ## Construct a new cone.
   #  @param r the radius of the cone
   #  @param h the height of the cone
   def __init__(self, r, h) :
      self._r = r
      self._h = h

   ## Compute the volume of a cone.
   #  @return the volume of the cone
   #
   def getVolume(self) :
      return 1 / 3 * pi * self._r * self._r * self._h
   
   ## Compute the surface area of a cone.
   #  @return the surface area of the cone
   #
   def getSurface(self) :
      s = sqrt(self._h * self._h + self._r * self._r)
      return pi * self._r * s + pi * self._r * self._r

