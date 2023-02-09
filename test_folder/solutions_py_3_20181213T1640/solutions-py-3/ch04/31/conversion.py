##
#  Convert dollars to yen and yen to dollars.
#

# Read the conversion rate from the user.
rate = float(input("How many yen in a dollar? "))

# Read dollar amounts from the user, converting each until the sentinel is
# entered.
dollars = float(input("Enter an amount in dollars (0 to stop): "))
while dollars != 0 :
   yen = dollars * rate
   print(dollars, "dollars is", yen, "yen")
   dollars = float(input("Enter an amount in dollars (0 to stop): "))

# Read yen amounts from the user, converting each until the sentinel is
# entered.
print()
yen = float(input("Enter an amount in yen (0 to quit): "))
while yen != 0 :
   dollars = yen / rate
   print(yen, "yen is", dollars, "dollars")
   yen = float(input("Enter an amount in yen (0 to quit): "))

