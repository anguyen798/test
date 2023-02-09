##
#  Determine whether or not a year is a leap year.
#

def main() :
   print("1900 is a leap year:", isLeapYear(1900))
   print("2000 is a leap year:", isLeapYear(2000))
   print("2001 is a leap year:", isLeapYear(2001))
   print("2002 is a leap year:", isLeapYear(2002))
   print("2003 is a leap year:", isLeapYear(2003))
   print("2004 is a leap year:", isLeapYear(2004))

## Determine whether or not a year is a leap year.
#  @param year the year to check
#  @return True if the year is a leap year, False otherwise
#
def isLeapYear(year) :
   if year > 1582 and year % 400 == 0 :
      return True
   if year > 1582 and year % 100 == 0 : 
      return False
   if year % 4 == 0 :
      return True
   return False

# Call the main program.
main()

