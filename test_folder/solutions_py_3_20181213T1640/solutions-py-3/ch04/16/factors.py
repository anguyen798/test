##
#  Compute and display the factors of an integer.
#

# Read an integer from the user.
value = int(input("Enter an integer: "))

# Compute and display the factors.
print("The factors are:")
while value > 1 :
   divisor = 2
   found = False

   # Search for a factor (divisor) until we find one.
   while found == False :
      if value % divisor == 0 :
         print(divisor)
         value = value / divisor
         found = True
      divisor = divisor + 1

