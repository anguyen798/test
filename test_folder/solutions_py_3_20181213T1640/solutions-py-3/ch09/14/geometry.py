##
#  Functions for columputing the volume and surface area of spheres, cylinders
#  and cones.
#
from math import pi, sqrt

## Compute the volume of a sphere.
#  @param r the radius of the sphere
#  @return the volume of the sphere
#
def sphereVolume(r) :
   return 4 / 3 * pi * r ** 3

## Compute the surface area of a sphere.
#  @param r the radius of the sphere
#  @return the surface area of the sphere
#
def sphereSurface(r) :
   return 4 * pi * r ** 2

## Compute the volume of a cylinder.
#  @param r the radius of the cylinder
#  @return the volume of the cylinder
#
def cylinderVolume(r, h) :
   return pi * r ** 2 * h

## Compute the surface area of a cylinder.
#  @param r the radius of the cylinder
#  @return the surface area of the cylinder
#
def cylinderSurface(r, h) :
   return 2 * (pi * r ** 2 + pi * r * h)

## Compute the volume of a cone.
#  @param r the radius of the cone
#  @return the volume of the cone
#
def coneVolume(r, h) :
   return 1 / 3 * pi * r * r * h

## Compute the surface area of a cone.
#  @param r the radius of the cone
#  @return the surface area of the cone
#
def coneSurface(r, h) :
   s = sqrt(h * h + r * r)
   return pi * r * s + pi * r * r

