##
#  Compute the focal length of a lense.
#

def main() :
   # Gather input from the user.
   thickness = float(input("Enter the thickness: "))
   r1 = float(input("Enter radius of curvature 1: "))
   r2 = float(input("Enter radius of curvature 2: "))
   index = float(input("Enter the refractive index: "))

   # Compute and display the focal length.
   print("The focal length is %.2f" % focalLength(thickness, r1, r2, index))

## Compute the focal length of a lense.
#  @param d the thickness of the lense
#  @param r1 the radii of curvature
#  @param r2 the radii of curvature
#  @param n the refractive index
#  @return the focal length of the lense
#
def focalLength(d, r1, r2, n) :
   return 1 / ((n-1) * (1 / r1 - 1 / r2 + ((n - 1) * d) / (n * r1 * r2)))

# Call the main function.
main()

