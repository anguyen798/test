##  
# Repeat Exercise P4.53, but now use the neighbors of
# each pixel in all eight compass directions. 
from graphics import GraphicsImage, GraphicsWindow

#filename = "jellyfish.gif"
filename = "arrow.gif"
#filename = input("Enter the name of the image file: ")

threshold = 30

# Load the image from the file.
image = GraphicsImage(filename)
width = image.width()
height = image.height()
newimage = GraphicsImage(width=width, height=height)

# Process the image
for row in range(height):
    for col in range(width):
        # Get the current pixel color.
        red = image.getRed(row,col)
        green = image.getGreen(row,col)
        blue = image.getBlue(row,col)

        # East
        if col == width-1:
            redE = red
            greenE = green
            blueE = blue
        else:
            redE = image.getRed(row,col+1)
            greenE = image.getGreen(row,col+1)
            blueE = image.getBlue(row,col+1)

        # South
        if row == height-1:
            redS = red
            greenS = green
            blueS = blue
        else:
            redS = image.getRed(row+1,col)
            greenS = image.getGreen(row+1,col)
            blueS = image.getBlue(row+1,col)

        # West
        if col == 0:
            redW = red
            greenW = green
            blueW = blue
        else:
            redW = image.getRed(row,col-1)
            greenW = image.getGreen(row,col-1)
            blueW = image.getBlue(row,col-1)

        # North
        if row == 0:
            redN = red
            greenN = green
            blueN = blue
        else:
            redN = image.getRed(row-1,col)
            greenN = image.getGreen(row-1,col)
            blueN = image.getBlue(row-1,col)

        # SouthEast
        if (col == width-1) or (row == height-1):
            redSE = red
            greenSE = green
            blueSE = blue
        else:
            redSE = image.getRed(row+1,col+1)
            greenSE = image.getGreen(row+1,col+1)
            blueSE = image.getBlue(row+1,col+1)

        # SouthWest
        if (col == 0) or (row == height-1):
            redSW = red
            greenSW = green
            blueSW = blue
        else:
            redSW = image.getRed(row+1,col-1)
            greenSW = image.getGreen(row+1,col-1)
            blueSW = image.getBlue(row+1,col-1)

        # NorthWest
        if (col == 0) or (row == 0):
            redNW = red
            greenNW = green
            blueNW = blue
        else:
            redNW = image.getRed(row-1,col-1)
            greenNW = image.getGreen(row-1,col-1)
            blueNW = image.getBlue(row-1,col-1)

        # NorthEast
        if (col == width-1) or (row == 0):
            redNE = red
            greenNE = green
            blueNE = blue
        else:
            redNE = image.getRed(row-1,col+1)
            greenNE = image.getGreen(row-1,col+1)
            blueNE = image.getBlue(row-1,col+1)

        redNeighbors = (redE + redS + redW + redN + \
                        redSE + redSW + redNW + redNE)/8
        greenNeighbors = (greenE + greenS + greenW + greenN + \
                          greenSE + greenSW + greenNW + greenNE)/8
        blueNeighbors = (blueE + blueS + blueW + blueN + \
                         blueSE + blueSW + greenNW + greenNE)/8

        # Calculate distance
        distance = abs(red - redNeighbors) + \
                   abs(green - greenNeighbors) + \
                   abs(blue - blueNeighbors)
        
        # Determine black or white value
        if distance > threshold:
            newimage.setPixel(row,col, 0, 0, 0)
        else:
            newimage.setPixel(row,col, 255, 255, 255)

# Save the new image with a new name.
newimage.save("edges2-"+filename)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(newimage)
win.wait()

