##  
# Implement a "sunset" effect by increasing the red level of each pixel
# of an image by 30 percent (up to a value of 255).
from graphics import GraphicsImage, GraphicsWindow

filename = "jellyfish.gif"
#filename = input("Enter the name of the image file: ")

# Load the image from the file.
image = GraphicsImage(filename)

# Process the image
width = image.width()
height = image.height()
for row in range(height):
    for col in range(width):
        # Get the current pixel color.
        red = image.getRed(row,col)
        green = image.getGreen(row,col)
        blue = image.getBlue(row,col)

        # Filter the pixel.
        newRed = red + .3*(255-red)
        if newRed > 255:
            newRed = 255
        newGreen = green
        newBlue = blue

        # Set the pixel to the new color.
        image.setPixel(row,col, newRed, newGreen, newBlue)

# Save the new image with a new name.
image.save("sunset-"+filename)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
win.wait()

