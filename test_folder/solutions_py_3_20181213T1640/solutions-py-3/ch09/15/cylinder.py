##
#  Define a cylinder class.
#
from math import pi, sqrt

## A class that stores the radius and height of a cylinder.
#
class Cylinder :
   ## Construct a new cylinder.
   #  @param r the radius of the cylinder
   #  @param h the height of the cylinder
   def __init__(self, r, h) :
      self._r = r
      self._h = h

   ## Compute the volume of a cylinder.
   #  @param r the radius of the cylinder
   #  @return the volume of the cylinder
   #
   def getVolume(self) :
      return pi * self._r ** 2 * self._h
   
   ## Compute the surface area of a cylinder.
   #  @param r the radius of the cylinder
   #  @return the surface area of the cylinder
   #
   def getSurface(self) :
      return 2 * (pi * self._r ** 2 + pi * self._r * self._h)

