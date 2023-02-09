##
#  Display a programmer's horoscope.
#

# Read input from the user.
print("Please enter you birthday:")
month = int(input("  month: "))
day = int(input("  day: "))

# Check each date range and display a fortune.
if month == 3 and day >= 21 or month == 4 and day <= 19 :
   print("Aries are easily frustrated by small bugs.")

elif month == 4 and day >= 20 or month == 5 and day <= 20 :
   print("Taurus will accomplish great things thanks to careful debugging.")

elif month == 5 and day >= 21 or month == 6 and day <= 20 :
   print("Gemini will regret his decision to write code before developing")
   print("an algorithm.")

elif month == 6 and day >= 21 or month == 7 and day <= 22 :
   print("Cancer will find a difficult bug by tracing the code by hand.")

elif month == 7 and day >= 23 or month == 8 and day <= 22 :
   print("Leo should spend more time coding and less time growling.")

elif month == 8 and day >= 23 or month == 9 and day <= 22 :
   print("Virgo will be frustrated by an infinite loop.")

elif month == 9 and day >= 23 or month == 10 and day <= 22 :
   print("Libra will find success by using elif instead of if.")

elif month == 10 and day >= 23 or month == 11 and day <= 21 :
   print("Scorpio will solve a difficult problem for a friend.")

elif month == 11 and day >= 22 or month == 12 and day <= 21 :
   print("Sagittarius will feel buried by bits and bytes, but will ultimately")
   print("triumph due to hard word.")

elif month == 12 and day >= 22 or month == 1 and day <= 19 :
   print("Capricorn will find success in their favorite game, but this will")
   print("cause a poor outcome for their latest programming assignment.")

elif month == 1 and day >= 20 or month == 2 and day <= 18 :
   print("Aquarius will learn that coffee and keyboards don't mix.")

elif month == 2 and day >= 19 or month == 3 and day <= 20 :
   print("Pisces will be stumped by a variable that is initialized to the")
   print("wrong value")

