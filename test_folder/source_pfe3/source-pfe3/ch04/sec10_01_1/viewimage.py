##
#  This program provides a simple image viewer that loads an image from 
#  a file displays it in a window.
#

from ezgraphics import GraphicsImage, ImageWindow

filename = input("Enter the name of the image file: ")

# Load the image from the file.
image = GraphicsImage(filename)

# Display it in a window and wait for the user to close the window.
win = ImageWindow()
win.display(image)
win.wait()
