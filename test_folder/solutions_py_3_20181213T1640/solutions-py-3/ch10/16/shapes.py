##
#  This modules defines a class hierarchy for geometric shapes.
#

import graphics

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
      
## A rectangle shape.
#
class Rectangle(GeometricShape) :
   ## Constructs a width x height rectangle with the upper-left corner at (x, y).
   #  @param x the x-coordinate of the upper-left corner
   #  @param y the y-coordinate of the upper-left corner
   #  @param width the horizontal size
   #  @param height the vertical size
   #
   def __init__(self, x, y, width, height) :
      super().__init__(x, y)
      self._width = width
      self._height = height
      
   # Overrides the superclass method to draw the rectangle.
   def draw(self, canvas) :
      super().draw(canvas)
      canvas.drawRect(self.getX(), self.getY(), self._width, self._height)

   ## Overrides the superclass method.
   def getWidth(self) :
      return self._width

   ## Overrides the superclass method.
   def getHeight(self) :
      return self._height
    
## A square shape - a rectangle with equal sides.
#
class Square(Rectangle) :
   ## Constructs a square of the given size positioned at (x, y).
   #  @param x the x-coordinate of the upper-left corner
   #  @param y the y-coordinate of the upper-left corner
   #  @param size the length of a side
   #
   def __init__(self, x, y, size) :
      super().__init__(x, y, size, size)
      
       
## A line segment.
#
class Line(GeometricShape) :
   ## Constructs a line segment.
   #  @param x1 the x-coordinate of the starting point
   #  @param y1 the y-coordinate of the starting point
   #  @param x2 the x-coordinate of the ending point
   #  @param y2 the y-coordinate of the ending point
   #
   def __init__(self, x1, y1, x2, y2) :
      super().__init__(min(x1, x2), min(y1, y2))
      self._startX = x1
      self._startY = y1
      self._endX = x2
      self._endY = y2
   
   ## Overrides the superclass method to draw the line on the canvas.     
   def draw(self, canvas) :
      super().draw(canvas)      
      canvas.drawLine(self._startX, self._startY, self._endX, self._endY)

   ## Overrides the superclass method.
   def getWidth(self) :
      return abs(self._endX - self._startX)

   ## Overrides the superclass method.
   def getHeight(self) :
      return abs(self._endY - self._startY)

   ## Overrides the superclass method.
   def moveBy(self, dx, dy) :
      super().moveBy(dx, dy)
      self._startX = self._startX + dx
      self._startY = self._startY + dy
      self._endX = self._endX + dx
      self._endY = self._endY + dy
   
## A container of geometric shapes in which the shapes are positioned 
#  relative to the upper-left corner of a bounding box.
#
class Group(GeometricShape) : 
   ## Constructs the group with its anchor point at (ax, ay).
   #  @param ax the x-coordinate of the anchor point
   #  @param ay the y-coordinate of the anchor point
   #   
   def __init__(self, ax = 0, ay = 0) :
      super().__init__(0, 0)
      self._shapeList = []
      self._ax = ax
      self._ay = ay

   ## Adds a shape to the group.
   #  @param shape the shape to be added
   #
   def add(self, shape) :
      self._shapeList.append(shape)

      # Update the upper left corner position after adding the shape.
      xs = []
      ys = []
      for shape in self._shapeList :
         xs.append(self._ax + shape.getX())
         ys.append(self._ay + shape.getY())

      self._x = min(xs)
      self._y = min(ys)
         
   ## Draws all of the shapes on the canvas.
   #  @param canvas the graphical canvas on which to draw the shapes
   #
   def draw(self, canvas) :
      for shape in self._shapeList :
         shape.moveBy(self._ax, self._ay)
         shape.draw(canvas)
         shape.moveBy(-self._ax, -self._ay)

   ## Gets width from the left most edge of the left most shape to the right
   #  most edge of the right most shape.
   def getWidth(self) :
      lefts = []
      rights = []

      for shape in self._shapeList :
         left = self._ax + shape.getX()
         right = self._ax + shape.getX() + shape.getWidth()
         lefts.append(left)
         rights.append(right)

      return max(rights) - min(lefts)

   ## Gets height from the top of the top shape to the bottom of the bottom
   #  shape.
   def getHeight(self) :
      tops = []
      bottoms = []

      for shape in self._shapeList :
         top = self._ay + shape.getY()
         bottom = self._ay + shape.getY() + shape.getHeight()
         tops.append(top)
         bottoms.append(bottom)

      return max(bottoms) - min(tops)

   ## Moves the shape to a new position by adjusting its anchor coordinates.
   #  @param dx the amount to move in x-direction
   #  @param dy the amount to move in y-direction
   #
   def moveBy(self, dx, dy) :
      self._ax = self._ax + dx
      self._ay = self._ay + dy

      # Update the upper left corner position after performing the move.
      xs = []
      ys = []
      for shape in self._shapeList :
         xs.append(self._ax + shape.getX())
         ys.append(self._ay + shape.getY())

      self._x = min(xs)
      self._y = min(ys)

