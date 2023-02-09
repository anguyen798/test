##
#  Compute and display the total price of a book order.
#

# Define constants.
TAX_RATE = 0.075
SHIPPING_PER_BOOK = 2.0

# Gather input from the user.
book_price = float(input("Enter the total book price: "))
num_books = int(input("Enter the number of books: "))

# Compute the total price.
tax = book_price * TAX_RATE
shipping = num_books * SHIPPING_PER_BOOK
total_price = book_price + tax + shipping

# Display the result.
print("The total cost of the order is $%.2f." % total_price)

