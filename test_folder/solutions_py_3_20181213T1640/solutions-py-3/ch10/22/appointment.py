##
#  Define classes for working with appointments.
#

## An appointment has a description and a date.
#
class Appointment :
   ## Construct a new appointment.
   #  @param day the day of the appointment
   #  @param month the month of the appointment
   #  @param year the year of the appointment
   #  @param desc the description of the appointment
   def __init__(self, day, month, year, desc) :
      self._day = day
      self._month = month
      self._year = year
      self._desc = desc

   ## Determine if an appointment occurs on a given day, month and year.
   #  @param day the day to check
   #  @param month the month to check
   #  @param year the year to check
   #  @return True if the appointment occurs on the provided date, False otherwise
   def occursOn(self, day, month, year) :
      return day == self._day and month == self._month and year == self._year

## An appointment that occurs only one time on a specific date.
#
class Onetime(Appointment) :
   ## Construct a new appointment.
   #  @param day the day of the appointment
   #  @param month the month of the appointment
   #  @param year the year of the appointment
   #  @param desc the description of the appointment
   #
   def __init__(self, day, month, year, desc) :
      super().__init__(day, month, year, desc)

   ## Generate a string representation of the appointment.
   #  @return a string representing the appointment
   #
   def __repr__(self) :
      return "One time appointment (%02d/%02d/%04d): %s" % (self._day, self._month, self._year, self._desc)

## An appointment that occurs daily.
#
class Daily(Appointment) :
   ## Construct a new appointment.
   #  @param day the day of the appointment
   #  @param month the month of the appointment
   #  @param year the year of the appointment
   #  @param desc the description of the appointment
   #
   def __init__(self, day, month, year, desc) :
      super().__init__(day, month, year, desc)

   ## Generate a string representation of the appointment.
   #  @return a string representing the appointment
   #
   def __repr__(self) :
      return "Daily appointment starting (%02d/%02d/%04d): %s" % (self._day, self._month, self._year, self._desc)

   ## Determine if an appointment occurs on a given day, month and year.
   #  @param day the day to check
   #  @param month the month to check
   #  @param year the year to check
   #  @return True if the appointment occurs on the provided date, False otherwise
   def occursOn(self, day, month, year) :
      if year > self._year :
         return True
      if year == self._year and month > self._month :
         return True
      if year == self._year and month == self._month and day >= self._day :
         return True
      return False

## An appointment that occurs monthly.
#
class Monthly(Appointment) :
   ## Construct a new appointment.
   #  @param day the day of the appointment
   #  @param month the month of the appointment
   #  @param year the year of the appointment
   #  @param desc the description of the appointment
   #
   def __init__(self, day, month, year, desc) :
      super().__init__(day, month, year, desc)

   ## Generate a string representation of the appointment.
   #  @return a string representing the appointment
   #
   def __repr__(self) :
      return "Monthly appointment starting (%02d/%02d/%04d): %s" % (self._day, self._month, self._year, self._desc)

   ## Determine if an appointment occurs on a given day, month and year.
   #  @param day the day to check
   #  @param month the month to check
   #  @param year the year to check
   #  @return True if the appointment occurs on the provided date, False otherwise
   def occursOn(self, day, month, year) :
      if year > self._year and day == self._day:
         return True
      if year == self._year and month >= self._month and day == self._day :
         return True
      return False

