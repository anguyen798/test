##  
# Replicate an image four times
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
        newimage.setPixel(row,col, red, green, blue)
        newimage.setPixel(height+row,col, red, green, blue)
        newimage.setPixel(row,width+col, red, green, blue)
        newimage.setPixel(height+row,width+col, red, green, blue)
      
# Save the new image with a new name.
newimage.save("fourcopies-"+filename)

# Display the image on the screen.
win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(newimage)
win.wait()

