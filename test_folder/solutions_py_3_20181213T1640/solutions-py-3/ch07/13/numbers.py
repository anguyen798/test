##
#  Read numbers from the user, with error checking, and report the sum.
#

# Keep reading values from the user until they enter two consecutive
# non-numeric values.
quit = False
total = 0
while quit == False :
   # Read the value from the user with error checking.
   quit = False
   try :
      value = float(input("Enter a number, or 2 non-numbers to quit: "))
   except :
      try :
         value = float(input("Enter a number, or another non-number to quit: "))
      except :
         quit = True

   # If the number is valid, add it to the total.
   if not quit :
      total = total + value
   
# Display the total.
print("The total is", total)

