##
#  Simulate the motion of a projectile.
#

# Define constant variables.
DELTA_T = 0.01

# Read the initial velocity from the user.
v = float(input("Enter the initial velocity: "))
v0 = v

# While the canon ball hasn't returned to the ground.
count = 1
s = v * DELTA_T
while s > 0 :
   # Display the position and velocity every second.
   if count % 100 == 0 :
      t = count // 100
      exact = -0.5 * 9.81 * t * t + v0 * t 
      print("At time %d position is %.2f and velocity is %.2f. (Exact formula position is %.2f)" % 
            (count // 100, s, v, exact))

   # Update the position and velocity.
   s = s + v * DELTA_T
   v = v - 9.81 * DELTA_T
   count = count + 1

