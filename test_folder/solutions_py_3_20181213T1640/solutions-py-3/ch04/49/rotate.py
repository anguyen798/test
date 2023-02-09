##  
# Rotate an image 90 degrees clockwise
from graphics import GraphicsImage, GraphicsWindow

filename = "arrow.gif"
#filename = input("Enter the name of the image file: ")

# Load the image from the file.
image = GraphicsImage(filename)
width = image.width()
height = image.height()
newimage = GraphicsImage(height, width)

for row in range(height):
    for col in range(width):
        # Get the current pixel color.
        red = image.getRed(row,col)
        green = image.getGreen(row,col)
        blue = image.getBlue(row,col)

        # set the new image
        newimage.setPixel(col,height-row, red, green, blue)

# Save the new image with a new name.
newimage.save("rotate-"+filename)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(newimage)
win.wait()

