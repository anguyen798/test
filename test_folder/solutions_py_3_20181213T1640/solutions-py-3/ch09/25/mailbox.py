##
#  Define the mailbox class.
#
from message import Message

## The Mailbox class stores a collection of messages.
#
class Mailbox :
   ## Construct a new empty mailbox.
   #
   def __init__(self) :
      self._messages = []

   ## Add a new message to the mailbox.
   #  @param message the message to add
   #
   def addMessage(self, message) :
      self._messages.append(message)

   ## Get a message from the mailbox.
   #  @param index the index of the message to retrieve
   #  @return the message in the mailbox at the provided index
   #
   def getMessage(self, index) :
      return self._messages[index]

   ## Remove a message from the mailbox.
   #  @param index the index of the message to remove
   #
   def removeMessage(self, index) :
      self._messages.pop(index)

