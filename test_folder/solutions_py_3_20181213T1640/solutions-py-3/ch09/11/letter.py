##
#  Define a class for authoring a letter.
#

##
#  Create a letter which saves the sender, recipient and body.
class Letter :
   
   ## Construct a new letter with a sender and recipient.
   #  @param letterFrom the sender of the letter
   #  @param letterTo the recipient of the letter
   # 
   def __init__(self, letterFrom, letterTo) :
      self._sender = letterFrom
      self._recipient = letterTo
      self._body = []

   ## Add a line to the body of the letter.
   #  @param line the line of text to add to the letter
   def addLine(self, line) :
      self._body.append(line)

   ## Generate and return the complete text of the letter.
   #  @return the text of the letter in one long string
   def getText(self) :
      text = "Dear " + self._recipient + ":\n"
      text = text + "\n"

      for line in self._body :
         text = text + line + "\n"
      text = text + "\n"

      text = text + "Sincerely,\n"
      text = text + "\n"
      text = text + self._sender

      return text

