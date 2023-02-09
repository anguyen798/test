##
#  Classes for storing various types of people.
#

## Represent an employee with a name and salary.
#
class Employee :
   ## Construct a new employee with a name and salary.
   #  @param name the name of the person
   #  @param year the year in which the person was born
   #
   def __init__(self, name, salary) :
      self._name = name
      self._salary = salary

   ## Construct a string representation of the employee.
   #  @return a string containing the details of the employee
   #
   def __repr__(self) :
      return self._name + " has a salary of %.2f" % self._salary

## Represent a manager with a department.
#
class Manager(Employee) :
   ## Construct a new manager with a name, salary and department.
   #  @param name the name of the manager
   #  @param salary the salary of the manager
   #  @param department the manager's department
   #
   def __init__(self, name, salary, department) :
      super().__init__(name, salary)
      self._department = department

   ## Construct a string representation of the manager.
   #  @return a string containing the details of the manager
   #
   def __repr__(self) :
      return self._name + " has a salary of %.2f" % self._salary + \
               " and manages the " + self._department + " department"

## Represent an executive.
#
class Executive(Manager) :
   ## Construct a string representation of the executive.
   #  @return a string containing the details of the executive
   #
   def __repr__(self) :
      return self._name + " has a salary of %.2f" % self._salary + \
               " and is the executive for the " + self._department + " department"

