##
#  Download a web page and extract the links from it.  Extract all the
#  links from the linked documents too.
#
import urllib.request

def main() :
   # Gather input from the user.
   url = input("Enter the URL of the webpage: ")

   # Print all of the links in the page entered by the user.
   print("Links in", url)
   linked = printAnchors(url)

   # Print all of the links in the pages linked to by the page entered by the
   # user, provided that the href is a fully qualified URL.
   for target in linked :
      print(target)
      if target.startswith("http://") :
         printAnchors(target)
      else :
         printAnchors(url + "/" + target)


## Find all of the anchors in a web page and get a list of the linked documents.
#  @param url the url of the web page to fetch
#  @return a list of all of the anchor targets
#
def printAnchors(url) :
   # Open the web page.
   page = urllib.request.urlopen(url)
  
   # Check each line to see if it contains an anchor.  If it does, print it out.
   retval = []
   for line in page :
      line = str(line, "utf-8")
      anchor_start = line.find("<a href=\"")
      anchor_end = line.find("\">", anchor_start)
      anchor_close = line.find("</a>", anchor_end)
  
      # The page contains an anchor if we were able to find all 3 of the parts.
      if anchor_start >= 0 and anchor_end >= 0 and anchor_close >= 0 :
         print(line[anchor_start : anchor_close + 4])
         retval.append(line[anchor_start + 9 : anchor_end])

   return retval

# Call the main function.
main()

