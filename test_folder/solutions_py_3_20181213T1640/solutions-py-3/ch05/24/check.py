##
#  Print a pay cheque for an employee.
#
from int_name import intName

OVERTIME_LIMIT = 40

def main() :
   name = input("Enter the name of the employee: ")
   pay = computePay()
   printCheck(name, pay)

## Compute the pay amount for an employee, giving time an a half for overtime.
#  @return the pay amount
#
def computePay() :
   rate = float(input("Enter the hourly pay rate: "))
   hours = float(input("Enter the hours worked: "))
   pay = rate * min(hours, OVERTIME_LIMIT) + \
         rate * max(0, hours - OVERTIME_LIMIT) * 1.5
   return pay

## Display the pay cheque.
#
def printCheck(name, pay) :
   print()
   print("Fictitous Company    | 12345 Some Street")
   print("                     | Some State")
   print("                     | Some Country")
   print()
   print("Pay:                               Amount: %.2f" % pay)
   print()
   print(intName(pay // 1), "and", int((pay % 1) * 100), "/ 100")
   print()
   print("To the order of:", name)

# Call the main function.
main()

