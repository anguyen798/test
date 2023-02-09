##
#  Count the number of people entering and leaving an oyster bar.
#

# Define constant variables.
LIMIT = 100

# Continue couting the people in the oyster bar until it reaches LIMIT exactly.
count = 0
while count != LIMIT :
   # Read the size of the group from the user, ensuring it is valid.
   group = int(input("How many people want to enter / leave the bar? "))
   while group + count > LIMIT or group + count < 0 :
      print("Sorry, that will make the number of people in the bar invalid.")
      group = int(input("How many people want to enter / leave the bar? "))

   count = count + group
   print("The current number of people in the bar is", count)

# Report that the bar is full.
print("The bar is full!")

