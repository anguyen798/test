##
#  Define a sphere class.
#
from math import pi, sqrt

## A class that stores the radius and height of a sphere.
#
class Sphere :
   ## Construct a new cone.
   #  @param r the radius of the cone
   def __init__(self, r) :
      self._r = r

   ## Compute the volume of a sphere.
   #  @return the volume of the sphere
   #
   def getVolume(self) :
      return 4 / 3 * pi * self._r ** 3
   
   ## Compute the surface area of a sphere.
   #  @return the surface area of the sphere
   #
   def getSurface(self) :
      return 4 * pi * self._r ** 2

