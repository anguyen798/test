##  
# Write a program that creates and saves a 200x200 pixel image
# of four triangles (green and red), with a black border, ten
# pixels wide, around the square formed by the triangles.
from graphics import GraphicsImage, GraphicsWindow

filename = "triangles2.gif"
size = 200
borderWidth = 10

# Create new image
newimage = GraphicsImage(size, size)

for row in range(size):
    for col in range(size):
        x = col
        y = row
        if x < borderWidth or x > size-borderWidth or \
           y < borderWidth or y > size-borderWidth:
            newimage.setPixel(row,col, 0, 0, 0)
        elif ( y < x and y < size-x ) or ( y > x and y > size-x ):
            newimage.setPixel(row,col, 0, 255, 0)
        else:
            newimage.setPixel(row,col, 255, 0, 0)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(newimage)


# Save the new image with a new name.
newimage.save(filename)
win.wait()

