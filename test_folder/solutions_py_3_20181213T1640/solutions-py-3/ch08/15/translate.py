## 
#  This program translates a single line of text from English to
#  text messaging abbreviations.
#

def main() :
   transMap = buildMapping("textabbv.txt")
   
   print("Enter a message to be translated:")
   message = input("")

   translation = message
   for k in transMap :
      translation = translation.replace(transMap[k], k)

   print("The translated text is:")
   print(translation)
      
## Extracts abbreviations and their corresponding English phrases from a 
#  file and builds a translation mapping.
#  @param filename name of the file containing the translations
#  @return a dictionary associating abbreviations with phrases
#
def buildMapping(filename) :
   transMap = {}
   infile = open(filename, "r")
   for line in infile :
      parts = line.split(":")
      transMap[parts[0]] = parts[1].rstrip()
      
   infile.close()
   return transMap

# Start the program.
main()

