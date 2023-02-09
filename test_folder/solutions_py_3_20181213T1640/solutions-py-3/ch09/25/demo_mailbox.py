##
#  Demonstrate the mailbox class.
#
from mailbox import Mailbox
from message import Message

# Create a mailbox and messages to it.
mbox = Mailbox()
mbox.addMessage(Message("Bob", "Santa"))
mbox.addMessage(Message("Bob", "Tooth Fairy"))

# Display the messages.
print(mbox.getMessage(0).toString())
print(mbox.getMessage(1).toString())

