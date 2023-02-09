##
#  Simulate a bank transaction.
#
from sys import exit

# Read balances from the user and validate that it are reasonable.
ch_bal = float(input("Enter the initial balance for checking: "))
if ch_bal < 0 :
   exit("The balance must be non-negative")

sav_bal = float(input("Enter the initial balance for savings: "))
if sav_bal < 0 :
   exit("The balance must be non-negative")

# Read the transaction type.
trans = input("Do you want to Deposit, Withdraw or Transfer? ")

# Read the account that will be involved.
acc = input(trans + " to (C)hecking or (S)avings? ")

# Read the amount.
amt = float(input(trans + " how much? "))

# Perform the transaction.
if trans == "Deposit" and acc == "C" :
   ch_bal = ch_bal + amt
elif trans == "Deposit" and acc == "S" :
   sav_bal = sav_bal + amt
elif trans == "Withdraw" and acc == "C" :
   if amt > ch_bal :
      print("You can't do that -- there isn't that much money in the account!")
   else :
      ch_bal = ch_bal - amt
elif trans == "Withdraw" and acc == "S" :
   if amt > sav_bal :
      print("You can't do that -- there isn't that much money in the account!")
   else :
      sav_bal = sav_bal - amt
elif trans == "Transfer" and acc == "C" :
   if amt > sav_bal :
      print("You can't do that -- there isn't that much money in the account!")
   else :
      sav_bal = sav_bal - amt
      ch_bal = ch_bal + amt
elif trans == "Transfer" and acc == "S" :
   if amt > ch_bal :
      print("You can't do that -- there isn't that much money in the account!")
   else :
      ch_bal = ch_bal - amt
      sav_bal = sav_bal + amt

# Display the new balances.
print("After the transaction:")
print("  Savings balance:", sav_bal)
print("  Checking balance:", ch_bal)

