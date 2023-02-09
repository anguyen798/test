##
#  Compute the area of a rectangle recursively.
#

## A class to represent a rectangle.
#  
class Rectangle :
   ## Construct a new rectangle.
   #  @param w the widht of the rectangle
   #  @param h the height of the rectangle
   #
   def __init__(self, w, h) :
      self._width = w
      self._height = h

   ## Compute the area of the rectangle recursively.
   #  @return the area of the rectangle
   #
   def area(self) :
      if self._width == 1 :
         return self._height
      return Rectangle(self._width - 1, self._height).area() + self._height

def main() :
   # Demonstrate that the area is computed correctly.
   r = Rectangle(20, 25)
   print(r.area())
   print("Expected: 500")

# Call the main function.
main()

