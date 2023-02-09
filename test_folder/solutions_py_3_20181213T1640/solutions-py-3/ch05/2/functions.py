##
#  Use a function to determine if 3 values are all the same, all different
#  or sorted in increasing order.
#

def main() :
   print("allTheSame of 1, 2, and 3 is", allTheSame(1, 2, 3))
   print("allTheSame of 3, 2, and 1 is", allTheSame(3, 2, 1))
   print("allTheSame of 1, 3, and 2 is", allTheSame(1, 3, 2))
   print("allTheSame of 2, 2, and 2 is", allTheSame(2, 2, 2))

   print("allDifferent of 1, 2, and 3 is", allDifferent(1, 2, 3))
   print("allDifferent of 3, 2, and 1 is", allDifferent(3, 2, 1))
   print("allDifferent of 1, 3, and 2 is", allDifferent(1, 3, 2))
   print("allDifferent of 2, 2, and 2 is", allDifferent(2, 2, 2))

   print("sorted of 1, 2, and 3 is", sorted(1, 2, 3))
   print("sorted of 3, 2, and 1 is", sorted(3, 2, 1))
   print("sorted of 1, 3, and 2 is", sorted(1, 3, 2))
   print("sorted of 2, 2, and 2 is", sorted(2, 2, 2))

## Determine if 3 values are all the same.
#  @param x the first value
#  @param y the second value
#  @param z the final value
#  @return True if all the values are the same, False otherwise
#
def allTheSame(x, y, z) :
   if x == y and x == z :
      return True
   return False

## Determine if 3 values are all different.
#  @param x the first value
#  @param y the second value
#  @param z the final value
#  @return True if all the values are different, False otherwise
#
def allDifferent(x, y, z) :
   if x != y and x != z and y != z :
      return True
   return False

## Determine if 3 values are in increasing order.
#  @param x the first value
#  @param y the second value
#  @param z the final value
#  @return True if the values are in increasing order, False otherwise
#
def sorted(x, y, z) :
   if x <= y and y <= z :
      return True
   return False

# Call the main function.
main()

