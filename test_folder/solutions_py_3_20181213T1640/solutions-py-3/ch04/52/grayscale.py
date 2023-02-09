##  
# Convert an image to grayscale by changing each pixel to a gray one.
from graphics import GraphicsImage, GraphicsWindow

filename = "arrow.gif"
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

        # Calculate grey value
        grey = 0.2126*red + 0.7152*green + 0.0722*blue
        # Set the pixel to the new color.
        image.setPixel(row,col, grey, grey, grey)

# Save the new image with a new name.
image.save("grayscale-"+filename)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
win.wait()

