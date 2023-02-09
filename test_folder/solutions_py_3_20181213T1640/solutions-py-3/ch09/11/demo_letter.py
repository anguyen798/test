##
#  Demonstrate the letter class.
#
from letter import Letter

# Construct the letter with two lines of text.
myLetter = Letter("Mary", "John")
myLetter.addLine("I am sorry we must part.")
myLetter.addLine("I wish you all the best.")

# Display the letter.
print(myLetter.getText())

