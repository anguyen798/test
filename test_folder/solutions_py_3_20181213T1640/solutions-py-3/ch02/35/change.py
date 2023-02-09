##
#  Compute the change due to a customer.
#

# Gather input from the user.
due = int(input("Enter the amount due in pennies: "))
received = int(input("Enter the amount received in pennies: "))

# Compute the number of dollars, quarters, dimes, nickels and pennies.
change = received - due

dollars = change // 100
change = change % 100

quarters = change // 25
change = change % 25

dimes = change // 10
change = change % 10

nickels = change // 5
pennies = change % 5

# Display the result.
print("The change is:")
print("  ", dollars, "dollars")
print("  ", quarters, "quarters")
print("  ", dimes, "dimes")
print("  ", nickels, "nickels")
print("  ", pennies, "pennies")

