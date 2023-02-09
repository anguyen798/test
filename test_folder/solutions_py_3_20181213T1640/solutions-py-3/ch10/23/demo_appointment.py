##
#  Demonstrate the various appointment classes.
#

from appointment import Daily, Monthly, Onetime

def main() :
   # Create a list of appointments.
   appList = []

   choice = input("A)dd, L)ist or Q)uit? ").upper()
   while choice != "Q" :
      if choice == "L" :
         listAppointments(appList) 
      if choice == "A" :
         addAppointment(appList)

      choice = input("A)dd, L)ist or Q)uit? ").upper()

## Prompt the user for the information for an appointment and add it to the
#  list of appointments.
#  @param appList the list of appointments
#
def addAppointment(appList) :
   print("Adding a new appointment: ")
   day = int(input("  Day? "))
   month = int(input("  Month? "))
   year = int(input("  Year? "))
   desc = input("  Description? ")
   app_type = input("O)netime, D)aily or M)onthly? ").upper()

   if app_type == "O" :
      appList.append(Onetime(day, month, year, desc))
   elif app_type == "D" :
      appList.append(Daily(day, month, year, desc))
   elif app_type == "M" :
      appList.append(Monthly(day, month, year, desc))
   else :
      print("That wasn't a valid appointment type.")

## Ask the user for the day, month and year, then list all appointments on
#  the provided date.
#  @param appList the list of appointments to search
#
def listAppointments(appList) :
   # Read a date from the user and display all of its appointments.
   day = int(input("Enter the day: "))
   month = int(input("Enter the month: "))
   year = int(input("Enter the year: "))

   # Find all of the appointments on the entered date.
   for app in appList :
      if app.occursOn(day, month, year) :
         print(app)

# Call the main function.
main()

