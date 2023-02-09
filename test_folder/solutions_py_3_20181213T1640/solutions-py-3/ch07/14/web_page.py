##
#  Download a web page and save it to a file.
#
import urllib.request

# Gather input from the user.
url = input("Enter the URL of the webpage: ")
filename = input("Enter the name of the file to write: ")

# Open the web page and the file.
page = urllib.request.urlopen(url)
outf = open(filename, "w")

# Save the page to a file.
for line in page :
   line = str(line, "utf-8")
   outf.write(line)

# Close the file.
outf.close()

