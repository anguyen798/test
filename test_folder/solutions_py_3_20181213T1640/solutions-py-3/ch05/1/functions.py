##
#  Use a function to find the smallest of 3 values and the average of 3 values.
#

def main() :
   print("The smallest of 1, 2, and 3 is", smallest(1, 2, 3))
   print("The smallest of 3, 2, and 1 is", smallest(3, 2, 1))
   print("The smallest of 1, 3, and 2 is", smallest(1, 3, 2))
   print("The smallest of 2, 2, and 2 is", smallest(2, 2, 2))

   print("The average of 1, 2, and 3 is", average(1, 2, 3))
   print("The average of 10, 10, and 10 is", average(10, 10, 10))

## Identifies the smallest of 3 values.
#  @param x the first value
#  @param y the second value
#  @param z the final value
#  @return the smallest of the 3 values
#
def smallest(x, y, z) :
   if x <= y and x <= z :
      return x
   if y <= x and y <= z :
      return y
   return z

## Compute the average of 3 values.
#  @param x the first value
#  @param y the second value
#  @param z the final value
#  @return the average of the 3 values
#
def average(x, y, z) :
   avg = (x + y + z) / 3
   return avg

# Call the main function.
main()

