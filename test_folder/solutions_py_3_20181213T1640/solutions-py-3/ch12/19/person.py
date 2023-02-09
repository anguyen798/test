##
#  Compare people, finding the first and last people by name.
#

def main() :
   # Read 10 people from the user.
   people = []
   for i in range(0, 10) :
      p = Person(input("Enter the person's name: "))
      people.append(p)

   # Display the first and last person by the lexicographic ordering of their
   # name.
   print("The first person is:", min(people))
   print("The last person is:", max(people))

## Represent a person with a name.
#
class Person :
   ## Construct a new person.
   #  @param name the name of the person
   #
   def __init__(self, name) :
      self._name = name

   ## Compare two people for equality.
   #  @param other the other person to consider
   #  @return True if self == other, False otherwise
   #
   def __eq__(self, other) :
      return self._name == other._name

   ## Compare two people for inequality.
   #  @param other the other person to consider
   #  @return True if self != other, False otherwise
   #
   def __ne__(self, other) :
      return not self == other

   ## Compare two people, checking if one is less than the other.
   #  @param other the other person to consider
   #  @return True if self < other, False otherwise
   #
   def __lt__(self, other) :
      return self._name < other._name

   ## Compare two people, checking if one is less than or equal to the other.
   #  @param other the other person to consider
   #  @return True if self <= other, False otherwise
   #
   def __le__(self, other) :
      return self < other or self == other

   ## Compare two people, checking if one is greater than the other.
   #  @param other the other person to consider
   #  @return True if self > other, False otherwise
   #
   def __gt__(self, other) :
      return not self <= other

   ## Compare two people, checking if one is greater than or equal to the other.
   #  @param other the other person to consider
   #  @return True if self >= other, False otherwise
   #
   def __ge__(self, other) :
      return not self < other

   ## Generate a string representation of the person.
   #  @return a string containing the person's name
   #
   def __repr__(self) :
      return self._name

# Call the main function.
main()

