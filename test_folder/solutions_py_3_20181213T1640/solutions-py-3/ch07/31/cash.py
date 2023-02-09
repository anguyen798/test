##
#  Check to see if cash transactions balance.
#

# Gather input from the user.
opening = float(input("Enter the opening cash balance: "))
closing = float(input("Enter the closing cash balance: "))
filename = input("Enter the file name: ")

# Open the file.
inf = open(filename, "r")

# Process all of the lines.
balance = opening
for line in inf :
   parts = line.split()
   amount = float(parts[1])
   if parts[2] == "R" :
      balance = balance + amount
   else :
      balance = balance - amount

# Display the result.
if closing == balance :
   print("The closing balance is correct. ")
else :
   print("The closing balance didn't match.")
   print("According to the file, it should be %.2f" % balance)

