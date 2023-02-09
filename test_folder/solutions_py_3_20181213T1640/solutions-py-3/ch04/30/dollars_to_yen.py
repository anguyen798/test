##
#  Convert dollars to yen.
#

# Read the conversion rate from the user.
rate = float(input("How many yen in a dollar? "))

# Read dollar amounts from the user, converting each until the sentinel is
# entered.
dollars = float(input("Enter an amount in dollars (0 to quit): "))
while dollars != 0 :
   yen = dollars * rate
   print(dollars, "dollars is", yen, "yen")
   dollars = float(input("Enter an amount in dollars (0 to quit): "))

