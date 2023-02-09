##
#  Write a message to a file and then read it back.
#

# Define constant variables.
MESSAGE = "Hello World!"
FILENAME = "hello.txt"

# Write the message to the file.
outf = open(FILENAME, "w")
outf.write(MESSAGE + "\n")
outf.close()

# Read the message back and display it.
inf = open(FILENAME, "r")
message = inf.readline()
print("The file contained", message)

