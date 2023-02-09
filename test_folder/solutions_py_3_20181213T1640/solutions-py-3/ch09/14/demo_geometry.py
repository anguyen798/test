##
#  Demonstrate functions for computing the volume and surface area of spheres,
#  cylinders and cones.
#
from math import pi, sqrt
from geometry import sphereVolume, sphereSurface, cylinderVolume, cylinderSurface, coneVolume, coneSurface

def main() :
   r = float(input("Enter the radius: "))
   h = float(input("Enter the height: "))

   print("A sphere has volume:", sphereVolume(r))
   print("A sphere has surface area:", sphereSurface(r))
   print("A cylinder has volume:", cylinderVolume(r, h))
   print("A cylinder has surface area:", cylinderSurface(r, h))
   print("A cone has volume:", coneVolume(r, h))
   print("A cone has surface area:", coneSurface(r, h))

# Call the main function.
main()

