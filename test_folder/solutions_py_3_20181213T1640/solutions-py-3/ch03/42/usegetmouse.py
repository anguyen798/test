## getMouse method 
# Modify the program in Worked Example 3.2 to use the getMouse method to
# obtain the center coordinates of the two circles.
#
from graphics import GraphicsWindow
from math import sqrt
from sys import exit

# Define constant variables.
MIN_RADIUS = 5
WIN_WIDTH = 500
WIN_HEIGHT = 500

# Create the graphics window and get the canvas.
win = GraphicsWindow(WIN_WIDTH, WIN_HEIGHT)
canvas = win.canvas()

# Obtain the parameters of the first circle.
print("Click on the canvas for center of first circle:")
point = win.getMouse()
x0 = point[0]
y0 = point[1]
if x0 < 0 or x0 >= WIN_WIDTH or y0 < 0 or y0 >= WIN_HEIGHT :
    exit("Error: the center of the circle must be within the area of the window.")

r0 = int(input(" radius: "))
if r0 <= MIN_RADIUS :
    exit("Error: the radius must be >", MIN_RADIUS)

# Draw the first circle.
canvas.setOutline("blue")
canvas.drawOval(x0 - r0, y0 - r0, 2 * r0, 2 * r0)

# Obtain the parameters of the second circle.
print("Click on the canvas for center of second circle:")
point = win.getMouse()
x1 = point[0]
y1 = point[1]
if x1 < 0 or x1 >= WIN_WIDTH or y1 < 0 or y1 >= WIN_HEIGHT :
    exit("Error: the center of the circle must be within the area of the window.")

r1 = int(input(" radius: "))
if r1 <= MIN_RADIUS :
    exit("Error: the radius must be >", MIN_RADIUS)

# Draw the second circle.
canvas.setOutline("red")
canvas.drawOval(x1 - r1, y1 - r1, 2 * r1, 2 * r1)

# Determine if the two circles intersect and select appropriate message.
dist = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

if dist > r0 + r1 :
    message = "The circles are completely separate."
elif dist < abs(r0 - r1) :
    message = "One circle is contained within the other."
elif dist == r0 + r1 :
    message = "The circles intersect at a single point."
elif dist == 0 and r0 == r1 :
    message = "The circles are coincident."
else :
    message = "The circles intersect at two points."

# Display the result at the bottom of the graphics window.
canvas.setOutline("black")
canvas.drawText(15, WIN_HEIGHT - 15, message)

# Wait until the user closes the window.
win.wait()

