##
#  Download a web page and display it, using the correct character encoding.
#
import sys
import urllib.request
from sys import exit

# Collect the url from the command line.
url = sys.argv[1]

# Open the web page and the file.
page = urllib.request.urlopen(url)
print(page.headers["content-type"])

# Try to determine the character set from the header.
encoding = ""
if "charset=" in page.headers["content-type"] :
   content_type = page.headers["content-type"]

   charset_start = content_type.index("charset=") + 8
   if ";" in content_type[charset_start : ] :
      charset_end = content_type.index(";", charset_start)
   else :
      charset_end = len(content_type)
   encoding = content_type[charset_start : charset_end]
else :
   # Try to determine the encoding from the first 2 or 3 bytes.
   content = str(page.read(), "latin_1")
   if content[0] == chr(255) and content[1] == chr(254) or \
      content[0] == chr(254) and content[1] == chr(255) :
      encoding = "utf-16"
   elif content[0] == chr(239) and content[1] == chr(187) and \
        content[2] == chr(191) :
      encoding = "utf-8"
   else :
      # Try and find the encoding somewhere in the file.
      for line in page :
         line = str(line, "latin_1")
         if "encoding=" in line :
            start = line.index("encoding=") + 10
            end = line.index("\"", start)
            encoding = line[start : end]
         if "charset=" in line :
            start = line.index("charset=") + 9
            end = line.index("\"", start)
            charset = line[start : end]

# If we failed to determine the encoding then the encoding variable is still
# an empty string.
if encoding == "":
   exit("Failed to determine the encoding for the page.")  

# Display the page.
print("The encoding for the page is", encoding)
for line in page :
   line = str(line, encoding)
   print(line, end="")

