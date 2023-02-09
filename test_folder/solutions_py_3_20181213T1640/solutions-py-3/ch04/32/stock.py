##
#  Sell a stock when the desired target price is reached.
#

# Read the target price from the user.
target = float(input("Enter the target price: "))

# Keep reading the current price until it reaches the target.
current = float(input("Enter the current price: "))
while current < target :
   current = float(input("Enter the current price: "))

# Display the final message.
print("The current price reached the target.  Time to sell!")

