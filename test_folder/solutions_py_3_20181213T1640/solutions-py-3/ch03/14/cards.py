##
#  Convert from a card shorthand to its full description.
#

# Read input from the user.
card = input("Enter the card notation: ")

# Determine the value and the suit.
value = card[0]
if value == "1" :
   value = "10"

suit = card[len(card) - 1]

# Generate the full name of the card by first getting the full value.
if value == "J" :
   full_name = "Jack"
elif value == "Q" :
   full_name = "Queen"
elif value == "K" :
   full_name = "King"
elif value == "A" :
   full_name = "Ace"
else :
   full_name = value

# Add "of" before the suit.
full_name = full_name + " of "

# Now add the full name of the suit.
if suit == "S" :
   full_name = full_name + "Spades"
elif suit == "H" :
   full_name = full_name + "Hearts"
elif suit == "C" :
   full_name = full_name + "Clubs"
elif suit == "D" :
   full_name = full_name + "Diamonds"

# Display the result.
print(full_name)

