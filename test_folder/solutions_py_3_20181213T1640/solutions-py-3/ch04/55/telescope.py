##  
# Add a "telescope" effect to an image, coloring all pixels black that
# are more than half the distance between the center and the closest edge.
from graphics import GraphicsImage, GraphicsWindow
import math

filename = "arrow.gif"
#filename = "jellyfish.gif"
#filename = input("Enter the name of the image file: ")

# Load the image from the file.
image = GraphicsImage(filename)

# Process the image
width = image.width()
height = image.height()
center = width/2
middle = height/2

# calculate minimum distance
if height < width:
    minDist = height/4
else:
    minDist = width/4

   
for row in range(height):
    for col in range(width):
        # calculate distance of point from center
        dist = math.sqrt((row - middle)**2 +(col - center)**2)
        # Set the pixel to the black if further than minDist away
        if dist > minDist:
            image.setPixel(row,col, 0, 0, 0)

# Save the new image with a new name.
image.save("telescope-"+filename)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
win.wait()

