##
#  Read the parts of a filename and display the complete filename.
#

# Gather input from the user.
drive = input("Enter the drive letter: ")
path = input("Enter the path: ")
filename = input("Enter the file name: ")
extension = input("Enter the extension: ")

# Generate the complete filename.
complete = drive + ":" + path + "\\" + filename + "." + extension

# Display the result.
print("The complete file name is", complete)

