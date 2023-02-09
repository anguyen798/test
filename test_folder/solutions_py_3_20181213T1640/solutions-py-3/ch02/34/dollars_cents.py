##
#  Extract the dollars and cents from a floating point price.
#

# Gather input from the user.
price = float(input("Enter a price: "))

# Compute the dollars and the cents.
dollars = int(price)
cents = int((price - dollars) * 100 + 0.5)

# Display the result.
print(dollars, "dollars", cents, "cents")

