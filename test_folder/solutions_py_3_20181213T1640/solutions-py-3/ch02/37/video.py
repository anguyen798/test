##
#  Compute the discount used by a video club.
#

# Define constants.
MAX_DISCOUNT = 75

# Read input from the user.
rentals = int(input("Enter the number of movie rentals: "))
referrals = int(input("Enter the number of members referred to the video club: "))

# Compute the discount.
discount = min(rentals + referrals, MAX_DISCOUNT)

# Display the result.
print("The discount is equal to: %9.2f percent" % discount)

