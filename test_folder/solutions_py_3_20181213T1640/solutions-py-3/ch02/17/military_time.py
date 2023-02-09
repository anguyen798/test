##
#  Compute the difference between two military times.
#

# Read inputs from the user.
time1 = int(input("Please enter the first time: "))
time2 = int(input("Please enter the second time: "))

# The following if statement handles the part of the work needed for the
# extra credit portion of this question.
if time2 < time1 :
  time2 = time2 + 2360

# Compute the hours and minutes in the difference.
difference = time2 - time1
hours = difference // 100
minutes = difference % 100

# The following two statements handle the remainder of the work needed for
# extra credit by correcting any difference where the minutes value exceeds 60.
hours = hours + minutes // 60
minutes = minutes % 60

# Display the result.
print(hours, "hours", minutes, "minutes")

