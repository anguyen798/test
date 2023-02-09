##
#  Define the LabeledPoint class.
#

## A basic geometric shape. 
#
class GeometricShape :
   ## Construct a basic geometric shape.
   #  @param x the x-coordinate of the shape
   #  @param y the y-coordinate of the shape
   #
   def __init__(self, x, y) :
      self._x = x
      self._y = y
      self._fill = None
      self._outline = "black"
    
   ## Gets the leftmost x-position of the shape.
   #  @return the x-coordinate
   #
   def getX(self) :
      return self._x

   ## Gets the topmost y-position of the shape.
   #  @return the y-coordinate
   #
   def getY(self) :
      return self._y

   ## Gets the width of the shape.
   #  @return the width
   #
   def getWidth(self) :
      return 0

   ## Gets the height of the shape.
   #  @return the height
   #
   def getHeight(self) :
      return 0

   ## Sets the fill color.
   #  @param color the fill color
   #
   def setFill(self, color = None) :
      self._fill = color
      
   ## Sets the outline color.
   #  @param color the outline color
   #
   def setOutline(self, color = None) :
      self._outline = color
     
   ## Sets both the fill and outline colors to the same color.
   #  @param color the new color
   #
   def setColor(self, color) :
      self._fill = color
      self._outline = color
      
   ## Moves the shape to a new position by adjusting its (x, y) coordinates.
   #  @param dx the amount to move in x-direction
   #  @param dy the amount to move in y-direction
   #
   def moveBy(self, dx, dy) :
      self._x = self._x + dx
      self._y = self._y + dy
      
   ## Draws the shape on a canvas.
   #  @param canvas the graphical canvas on which to draw the shape
   #
   def draw(self, canvas) :
      canvas.setFill(self._fill)
      canvas.setOutline(self._outline)

      

## Represent a point with a label.
#
class LabeledPoint(GeometricShape) :
   ## Construct a new labeled point.
   #  @param x the x position of the point
   #  @param y the y position of the point
   #  @param label the point's label
   #
   def __init__(self, x, y, label) :
      super().__init__(x, y)
      self._label = label

   ## Accessor for the label of the point.
   #  @return the point's label
   def getLabel(self) :
      return self._label

   # Overrides the superclass method to draw the labeled point.
   def draw(self, canvas) :
      super().draw(canvas)
      canvas.drawPoint(self.getX(), self.getY())
      canvas.drawText(self.getX()+5, self.getY()-5, self.getLabel())
      

   ## Generate a string representation of the point.
   #  @param return a string describing the labeled point
   #
   def __repr__(self) :
      return "(%f, %f): %s" % (self._x, self._y, self._label)

