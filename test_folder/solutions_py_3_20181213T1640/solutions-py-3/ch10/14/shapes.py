##
#  This modules defines a class hierarchy for geometric shapes.
#

import graphics
from math import pi, cos, sin

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
      
## An arbitrary polygon shape.
#
class Polygon(GeometricShape) :
   ## Construct a new polygon from a list of points.
   #  @param vertexList the list of vertices that make up the shape
   #
   def __init__(self, vertexList) :
      # Find the minimum x and y values in the polygon.
      xs = []
      ys = []
      for [a, b] in vertexList :
         xs.append(a)
         ys.append(b)
      mx = min(xs)
      my = min(ys)

      # Use the super class constructor to build a new shape at the (mx, my).
      super().__init__(mx, my)

      # Adjust all of the points in the polygon by (mx, my) so that it draws
      # at the correct location.
      for i in range(len(vertexList)) :
         vertexList[i][0] = vertexList[i][0] - mx
         vertexList[i][1] = vertexList[i][1] - my

      self._points = vertexList

   ## Overrides the superclass method.
   def getWidth(self) :
      # Find the maximum x value in the polygon -- that's the width.
      xs = []
      for [a, b] in self._points :
         xs.append(a)

      return max(xs)

   ## Overrides the superclass method.
   def getHeight(self) :
      # Find the maximum y value in the polygon -- that's the height.
      ys = []
      for [a, b] in self._points :
         ys.append(b)

      return max(ys)

   # Overrides the superclass method to draw the polygon.
   def draw(self, canvas) :
      super().draw(canvas)
      last = len(self._points) - 1
      for i in range(last) :
         start = self._points[i]
         end = self._points[i + 1]
         canvas.drawLine(self._x + start[0], self._y + start[1], \
                          self._x + end[0], self._y + end[1])
      start = self._points[last]
      end = self._points[0]
      canvas.drawLine(self._x + start[0], self._y + start[1], \
                       self._x + end[0], self._y + end[1])

## A regular polygon.
#
class RegularPolygon(Polygon) :
   ## Construct a new regular polygon with the provided number of sides and 
   #  radius, and center position.
   #  @param n the number of sides
   #  @param r the radius of the polygon
   #  @param cx the x position of the center of the polygon
   #  @param cy the y position of the center of the polygon
   #
   def __init__(self, n, r, cx, cy) :
      vertList = []
      for i in range(0, n) :
         x = r * cos(2 * pi / n * i) + cx
         y = r * sin(2 * pi / n * i) + cy
         vertList.append([x, y])

      super().__init__(vertList)

## A Diamon shape.
#
class Diamond(RegularPolygon) :
   ## Construct a new diamond with the provided radius, and center position.
   #  @param r the radius of the polygon
   #  @param cx the x position of the center of the polygon
   #  @param cy the y position of the center of the polygon
   #
   def __init__(self, r, cx, cy) :
      super().__init__(4, r, cx, cy)


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
   ## Constructs the group with its bounding box positioned at (x, y).
   #  @param x the x-coordinate of the upper-left corner of the bounding box
   #  @param y the y-coordinate of the upper-left corner of the bounding box
   #   
   def __init__(self, x = 0, y = 0) :
      super().__init__(x, y)
      self._shapeList = []

   ## Adds a shape to the group.
   #  @param shape the shape to be added
   #
   def add(self, shape) :
      self._shapeList.append(shape)

      # Keep the shape within top and left edges of the bounding box.
      if shape.getX() < 0 : 
         shape.moveBy(-shape.getX(), 0)
      if shape.getY() < 0 : 
         shape.moveBy(0, -shape.getY())                 
         
   ## Draws all of the shapes on the canvas.
   #  @param canvas the graphical canvas on which to draw the shapes
   #
   def draw(self, canvas) :
      for shape in self._shapeList :
         shape.moveBy(self.getX(), self.getY())
         shape.draw(canvas)
         shape.moveBy(-self.getX(), -self.getY())

   ## Gets the rightmost extent of the shapes.
   def getWidth(self) :
      width = 0
      for shape in self._shapeList :
         width = max(width, shape.getX() + shape.getWidth())
      return width

   ## Gets the bottommost extent of the shapes.
   def getHeight(self) :
      height = 0
      for shape in self._shapeList :
         height = max(height, shape.getY() + shape.getHeight())
      return height

