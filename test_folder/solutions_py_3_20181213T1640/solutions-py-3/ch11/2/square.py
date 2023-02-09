##
#  Compute the area of a square recursively.
#

## A class to represent a square.
#  
class Square :
   ## Construct a new square.
   #  @param w the widht of the square
   #
   def __init__(self, w) :
      self._width = w

   ## Compute the area of the square recursively.
   #  @return the area of the square
   #
   def area(self) :
      if self._width == 1 :
         return 1 
      return Square(self._width - 1).area() + 2 * self._width - 1

def main() :
   # Demonstrate that the area is computed correctly.
   r = Square(20)
   print(r.area())
   print("Expected: 400")

# Call the main function.
main()

