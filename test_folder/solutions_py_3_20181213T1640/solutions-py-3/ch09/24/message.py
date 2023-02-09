##
#  Define the message class.
#

## A message with a sender, recipient and body.
#
class Message :
   ## Construct a new message.
   #  @param sender the sender of the message
   #  @param recipient the recipient of the message
   #
   def __init__(self, sender, recipient) :
      self._sender = sender
      self._recipient = recipient
      self._body = ""

   ## Append a line of text to the message.
   #  @param line the line of text to add to the message
   #
   def append(self, line) :
      self._body = self._body + line + "\n"

   ## Return the entire message as a string.
   #  @return a string representation of the entire message
   #
   def toString(self) :
      result = "From: " + self._sender + "\n"
      result = result + "To: " + self._recipient + "\n"
      result = result + self._body
      return result

