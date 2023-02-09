##  
# Add black diagonal stripes to an image, each spaced five pixels from the next.
from graphics import GraphicsImage, GraphicsWindow

filename = "jellyfish.gif"
#filename = input("Enter the name of the image file: ")

# Load the image from the file.
image = GraphicsImage(filename)

# Define variables
stripeDist = 10
stripeWidth = 3

# Process the image
width = image.width()
height = image.height()
for row in range(height):
    for col in range(width):
        # set pixel to black if part of diagonal stripe
        if (row + (width-col)) % stripeDist < stripeWidth:
            image.setPixel(row,col,0,0,0)

# Save the new image with a new name.
image.save("diagonalstripes-"+filename)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
win.wait()

