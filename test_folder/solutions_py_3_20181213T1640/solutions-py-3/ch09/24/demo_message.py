##
#  Demonstrate the Message class.
#
from message import Message

# Create the message.
wishList = Message("Bob", "Santa")
wishList.append("For Christmas, I would like:")
wishList.append("Video games")
wishList.append("World peace")

# Display its contents.
print(wishList.toString())

