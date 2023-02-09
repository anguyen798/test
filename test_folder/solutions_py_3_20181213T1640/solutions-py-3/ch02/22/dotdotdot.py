##
#  Print the first 3 letters of a string, followed by ..., followed by the 
#  last 3 letters of a string.
#

# Initialize the string.
string = "Mississippi"

# Display the result.
print("%s...%s" % (string[0 : 3], string[len(string) - 3 : len(string)]))

