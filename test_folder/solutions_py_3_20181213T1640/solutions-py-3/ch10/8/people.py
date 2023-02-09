##
#  Classes for storing various types of people.
#

## Represent a general person without additional specific properties.
#
class Person :
   ## Construct a new person with a name and year of birth.
   #  @param name the name of the person
   #  @param year the year in which the person was born
   #
   def __init__(self, name, year) :
      self._name = name
      self._year = year

   ## Construct a string representation of the person.
   #  @return a string containing the details of the person
   #
   def __repr__(self) :
      return self._name + ", born " + str(self._year)

## Represent a student with a major.
#
class Student(Person) :
   ## Construct a new student with a name, year of birth and major.
   #  @param name the name of the person
   #  @param year the year in which the person was born
   #  @param major the student's major
   #
   def __init__(self, name, year, major) :
      super().__init__(name, year)
      self._major = major

   ## Construct a string representation of the person.
   #  @return a string containing the details of the person
   #
   def __repr__(self) :
      return self._name + ", born " + str(self._year) + \
               " is a " + self._major + " major"

## Represent an instructor with a salary.
#
class Instructor(Person) :
   ## Construct a new instructor with a name, year of birth and salary.
   #  @param name the name of the person
   #  @param year the year in which the person was born
   #  @param salary the instructor's salary
   #
   def __init__(self, name, year, salary) :
      super().__init__(name, year)
      self._salary = salary

   ## Construct a string representation of the person.
   #  @return a string containing the details of the person
   #
   def __repr__(self) :
      return self._name + ", born " + str(self._year) + \
               " has a $%.2f" % self._salary + " salary"

