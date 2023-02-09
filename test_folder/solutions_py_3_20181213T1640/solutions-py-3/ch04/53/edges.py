##  
# Detect edges in an image, coloring each pixel black or white
# depending on whether it is significantly different from the
# neighboring pixels to the east, south, and southeast.
from graphics import GraphicsImage, GraphicsWindow

filename = "jellyfish.gif"
#filename = "arrow.gif"
#filename = input("Enter the name of the image file: ")

threshold = 30

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

        if col == width-1:
            redE = red
            greenE = green
            blueE = blue
        else:
            redE = image.getRed(row,col+1)
            greenE = image.getGreen(row,col+1)
            blueE = image.getBlue(row,col+1)

        if row == height-1:
            redS = red
            greenS = green
            blueS = blue
        else:
            redS = image.getRed(row+1,col)
            greenS = image.getGreen(row+1,col)
            blueS = image.getBlue(row+1,col)

        if (col == width-1) or (row == height-1):
            redSE = red
            greenSE = green
            blueSE = blue
        else:
            redSE = image.getRed(row+1,col+1)
            greenSE = image.getGreen(row+1,col+1)
            blueSE = image.getBlue(row+1,col+1)

        redNeighbors = (redE + redS + redSE)/3
        greenNeighbors = (greenE + greenS + greenSE)/3
        blueNeighbors = (blueE + blueS + blueSE)/3

        # Calculate distance
        distance = abs(red - redNeighbors) + \
                   abs(green - greenNeighbors) + \
                   abs(blue - blueNeighbors)
        
        # Determine black or white value
        if distance > threshold:
            image.setPixel(row,col, 0, 0, 0)
        else:
            image.setPixel(row,col, 255, 255, 255)

# Save the new image with a new name.
image.save("edges-"+filename)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
win.wait()

