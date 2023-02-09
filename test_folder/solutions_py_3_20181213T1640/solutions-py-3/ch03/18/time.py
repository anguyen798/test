##
#  Determine which of two times comes first.
#

# Read the times from the user.
hour1 = int(input("Enter the hour for the first time: "))
minute1 = int(input("Enter the minute for the first time: "))

hour2 = int(input("Enter the hour for the second time: "))
minute2 = int(input("Enter the minute for the second time: "))

# Determine which time comes first.
if hour1 < hour2 :
   first_hour = hour1
   first_minute = minute1
   second_hour = hour2
   second_minute = minute2
elif hour1 == hour2 :
   if minute1 < minute2 :
      first_hour = hour1
      first_minute = minute1
      second_hour = hour2
      second_minute = minute2
   elif minute1 == minute2 :
      first_hour = hour1
      first_minute = minute1
      second_hour = hour2
      second_minute = minute2
   else :
      first_hour = hour2
      first_minute = minute2
      second_hour = hour1
      second_minute = minute1
else :
   first_hour = hour2
   first_minute = minute2
   second_hour = hour1
   second_minute = minute1

# Display the result.
print("The first time is %02d:%02d" % (first_hour, first_minute))
print("The second time is %02d:%02d" % (second_hour, second_minute))

