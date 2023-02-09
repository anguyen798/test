##
#  Demonstrate the various appointment classes.
#

from appointment import Daily, Monthly, Onetime

# Create a list of appointments.
appList = []
appList.append(Daily(1, 1, 2013, "Do pushups"))
appList.append(Daily(15, 1, 2013, "Floss teeth"))
appList.append(Monthly(15, 12, 2012, "Backup data"))
appList.append(Onetime(21, 12, 2012, "Computer Science Final Exam"))
appList.append(Monthly(4, 2, 2013, "Call grandma"))
appList.append(Onetime(12, 4, 2013, "See dentist"))

# Read a date from the user and display all of its appointments until the user
# decides to quit.
day = int(input("Enter the day (0 to quit): "))
while day != 0 :
   month = int(input("Enter the month: "))
   year = int(input("Enter the year: "))

   # Find all of the appointments on the entered date.
   for app in appList :
      if app.occursOn(day, month, year) :
         print(app)
   
   day = int(input("Enter the day (0 to quit): "))

