##
#  This program draws a house with a given number of stories.
#
import turtle
import math

def main() :
   turtle.reset()
   turtle.speed(0)

   # Draw 5 different houses.
   drawHouse(0, 0, 2, 2)
   drawHouse(-400, 25, 4, 3)
   drawHouse(-300, -375, 3, 3)
   drawHouse(200, -300, 2, 5)
   drawHouse(225, 250, 1, 2)

   response = input("Press ENTER to quit.")

## Draw one window.
# @param x the position of the left edge of the house
# @param width the width of the window
# @param y the position of the bottom edge of the house
def drawWindow(x, width, y) :
   # Draw the window outline.
   turtle.left(90)
   turtle.penup()
   turtle.goto(x, y)
   turtle.pendown()
   turtle.forward(40) 
   turtle.right(90)
   turtle.forward(width) 
   turtle.right(90)
   turtle.forward(40) 
   turtle.right(90)
   turtle.forward(width) 
   turtle.right(90)

   # Draw the crossing lines through the window.
   turtle.goto(x + width / 2, y)
   turtle.forward(40)
   turtle.right(90)

   turtle.penup()
   turtle.goto(x, y + 20)
   turtle.pendown()
   turtle.forward(width)

## Draws one story of a house.
# @param x the position of the left edge of the house
# @param y the position of the bottom edge of the house
# @param w an integer number of windows per story
def drawStory(x, y, w) :
   turtle.left(90)
   turtle.penup()

   # Draw the sides of the story.
   turtle.goto(x, y)
   turtle.pendown()
   turtle.forward(80) 
   turtle.penup()

   turtle.goto(x+200, y)
   turtle.pendown()
   turtle.forward(80)
   turtle.right(90)

   # Draw the windows for the story.
   for i in range(w) :
      drawWindow(x + i * 200 / w + 200 / w / 4, 200 / w / 2, y + 20)

## Draws a house with a given numberof stories and windows per story.
# @param x the position of the left edge of the house
# @param y the position of the bottom edge of the house
# @param s an integer number of stories
# @param w an integer number of windows per story
#
def drawHouse(x, y, s, w) :
   # Draw the bottom story of the house.
   turtle.penup()
   turtle.goto(x, y)

   # Draw the outline.
   turtle.pendown()
   turtle.left(90)
   turtle.forward(80)

   turtle.goto(x, y)
   turtle.right(90)
   turtle.forward(200)
   turtle.left(90)
   turtle.forward(80)

   # Draw the door.
   turtle.penup()
   turtle.goto(x + 200 / w / 4, y)
   turtle.pendown()
   turtle.forward(80)
   turtle.right(90)
   turtle.forward(200 / w / 2)
   turtle.right(90)
   turtle.forward(80)
   turtle.left(90)

   # Draw the windows for the first story.
   for i in range(1, w) :
      drawWindow(x + i * 200 / w + 200 / w / 4, 200 / w / 2, y + 20)

   # Draw the stories above the first.
   for i in range(1, s) :
      drawStory(x, y + i * 80, w)

   # Draw the roof.
   turtle.penup()
   turtle.goto(x, y + s * 80)
   turtle.pendown()
   turtle.left(45)
   turtle.forward(math.sqrt(20000))
   turtle.right(90)
   turtle.forward(math.sqrt(20000))
   turtle.left(45)

main()
