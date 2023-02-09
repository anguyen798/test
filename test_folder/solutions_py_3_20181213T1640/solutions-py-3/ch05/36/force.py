##
#   Compute the power needed to overcome the drag force of a vehicle.
#

# Define constant variables.
PROJECTED_AREA = 2.5
DRAG_COEFFICIENT = 0.2
AIR_DENSITY = 1.23

WATTS_TO_HP = 1 / 746
MPH_TO_MPS = 0.447

def main() :
   # Gather input from the user.
   mph = float(input("Enter the speed in mph: "))
   v = mph * MPH_TO_MPS

   # Compute the power in Watts and horse power.
   p = power(v)
   hp = p * WATTS_TO_HP

   # Display the result.
   print("The car requires %.2f Watts or %.1f horse power." % (p, hp))

## Compute the drag force at a given velocity.
#  @param v the velocity of the vehicle
#  @return the drag force
#
def dragForce(v) :
   return 0.5 * AIR_DENSITY * v * v * PROJECTED_AREA * DRAG_COEFFICIENT

## COmpute the power needed to overcome the drag force at a given velocity.
#  @param v the velocity of the vehicle
#  @return the power in Watts
#
def power(v) :
   return dragForce(v) * v

# Call the main function.
main()

