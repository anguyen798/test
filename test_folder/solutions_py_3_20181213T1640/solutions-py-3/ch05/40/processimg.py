##  
# Add a function to image processing toolkit that places 
# two copies of an image next to each other, and another
# function that places two copies of an image below each
# other. Use processimg.py program to test your function. 
from graphics import GraphicsImage, GraphicsWindow
from imgproctools import *

# Read the name of the file to be processed.
filename = input("Enter the name of the image file to be processed: ")

# Load the image from the file and display it in a window.
image = GraphicsImage(filename)

win = GraphicsWindow()
canvas = win.canvas()
canvas.drawImage(image)
done = False

while not done :
   # Prompt the user for the type of processing.
   print("How should the image be processed?")
   print("1 - create image negative")
   print("2 - adjust brigthness")
   print("3 - flip vertically")
   print("4 - rotate to the left")
   print("5 - place two copies next to each other")
   print("6 - place two copies one below the other")
   print("7 - save and quit")

   response = int(input("Enter your choice: "))
         
# Process the image and display the new image in the window.
   if response == 1 : 
      newImage = createNegative(image)
   elif response == 2 :
      amount = float(input("Adjustment between -1.0 and 1.0: "))
      newImage = adjustBrightness(image, amount)
   elif response == 3 :
      newImage = flipVertically(image)
   elif response == 4 :
      newImage = rotateLeft(image) 
   elif response == 5 :
      newImage = twoCopiesHorizontal(image)
   elif response == 6 :
      newImage = twoCopiesVertical(image)
   if response == 7 :
      newImage.save("output.gif")
      done = True
   else :
      canvas.drawImage(newImage)
      image = newImage

