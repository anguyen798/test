## 
# Write a program that creates and saves a 200x200 pixel image
# of four triangles (green and red).
from graphics import GraphicsImage, GraphicsWindow

filename = "triangles.gif"

# Create new image
size = 200
newimage = GraphicsImage(size, size)

for row in range(size):
    for col in range(size):
        x = col
        y = row
        if ( y < x and y < size-x ) or ( y > x and y > size-x ):
            newimage.setPixel(row,col, 0, 255, 0)
        else:
            newimage.setPixel(row,col, 255, 0, 0)

# Save the new image with a new name.
newimage.save(filename)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(newimage)
win.wait()

