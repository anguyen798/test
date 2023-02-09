##
#  Demonstrate the Sphere, Cylinder and Cone classes.
#
from math import pi, sqrt
from sphere import Sphere
from cylinder import Cylinder
from cone import Cone

def main() :
   # Gather input from the user.
   r = float(input("Enter the radius: "))
   h = float(input("Enter the height: "))

   # Create a Cone, Sphere and Cylinder.
   co = Cone(r, h)
   s = Sphere(r)
   cy = Cylinder(r, h)

   # Display the volume and surface area of each shape.
   print("A sphere has volume:", s.getVolume())
   print("A sphere has surface area:", s.getSurface())
   print("A cylinder has volume:", cy.getVolume())
   print("A cylinder has surface area:", cy.getSurface())
   print("A cone has volume:", co.getVolume())
   print("A cone has surface area:", co.getSurface())

# Call the main function.
main()

