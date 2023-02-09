##
#  Simulate a bank machine validating a user's PIN.
#
from sys import exit

# Define constants.
CORRECT_PIN = "1234"

# Read the PIN for the first time.
pin = input("Enter your PIN: ")

if pin == CORRECT_PIN :
   exit("Your PIN is correct")

print("Your PIN is incorrect")

# Read the PIN for the second time.
pin = input("Enter your PIN: ")

if pin == CORRECT_PIN :
   exit("Your PIN is correct")

print("Your PIN is incorrect")

# Read the PIN for the third time.
pin = input("Enter your PIN: ")

if pin == CORRECT_PIN :
   exit("Your PIN is correct")

print("Your bank card is blocked")

