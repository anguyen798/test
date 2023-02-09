##  
# Replicate each pixel of an image four times, so that the image is
# twice as large and wide as the original, with "blocky" pixels.  
from graphics import GraphicsImage, GraphicsWindow

filename = "arrow.gif"
#filename = input("Enter the name of the image file: ")

# Load the image from the file.
image = GraphicsImage(filename)
width = image.width()
height = image.height()
newimage = GraphicsImage(width*2, height*2)

for row in range(height):
    for col in range(width):
        # Get the current pixel color.
        red = image.getRed(row,col)
        green = image.getGreen(row,col)
        blue = image.getBlue(row,col)

        # set the new image pixels
        newimage.setPixel(2*row,2*col, red, green, blue)
        newimage.setPixel(2*row+1,2*col, red, green, blue)
        newimage.setPixel(2*row, 2*col+1, red, green, blue)
        newimage.setPixel(2*row+1, 2*col+1, red, green, blue)
        
# Save the new image with a new name.
newimage.save("blocky-"+filename)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(newimage)
win.wait()

