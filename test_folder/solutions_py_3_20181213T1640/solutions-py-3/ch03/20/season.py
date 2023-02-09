##
#  Determine the season from a date.
#

# Read input from the user.
month = int(input("Enter the month as an integer: "))
day = int(input("Enter the day as an integer: "))

# Determine the season.
if month >= 1 and month <= 3 :
   season = "Winter"
elif month >= 4 and month <= 6 :
   season = "Spring"
elif month >= 7 and month <= 9 :
   season = "Summer"
elif month >= 10 and month <= 12 :
   season = "Fall"

if month % 3 == 0 and day >= 21 :
   if season == "Winter" :
      season = "Spring"
   elif season == "Spring" :
      season = "Summer"
   elif season == "Summer" :
      season = "Fall"
   else :
      season = "Winter"

# Display the result.
print("That day is in the", season)

