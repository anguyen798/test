##
#  Use a function to read a floating point value from the user.
#

def main() :
   salary = readFloat("pleaes enter your salary:")
   percentageRaise = readFloat("What percentage raise would you like?")
   print("The salary is", salary)
   print("The raise percentage is", percentageRaise)

## Read a floating point number from the user.
#  @param prompt the promtp to display for the user
#  @return the number entered by the user as a floating point value
#
def readFloat(prompt) :
   return float(input(prompt + " "))

# Call the main function.
main()

