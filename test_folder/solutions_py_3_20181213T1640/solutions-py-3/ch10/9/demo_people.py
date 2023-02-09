##
#  Demonstrate different types of people.
#
from people import Employee, Manager, Executive

# Create an employee, manager and executive.
emp = Employee("John Smith", 45000.00)
man = Manager("Jane Doe", 60000.00, "Widgets")
exe = Executive("Weird Guy", 90000.00, "Thingies")

# Display the people.
print(emp)
print(man)
print(exe)

