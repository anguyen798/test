##
#  Display the number of days in a month.
#

# Read input from the user.
month = int(input("Enter a month: "))

# Display the number of days.
if month == 2 :
   print("28 or 29 days")
elif month == 4 or month == 6 or month == 9 or month == 11 :
   print("30 days")
else :
   print("31 days")

