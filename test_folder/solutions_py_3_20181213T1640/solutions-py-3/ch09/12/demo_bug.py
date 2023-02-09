##
#  Demonstrate the Bug class.
#
from bug import Bug

# Create a new bug.
bugsy = Bug(10)

# Move it to position 12.
bugsy.move()
bugsy.move()

# Display its position.
print("Expected 12:  Actual: %d" % bugsy.getPosition())

# Move it to position 11.
bugsy.turn()
bugsy.move()

# Display its position.
print("Expected 11:  Actual: %d" % bugsy.getPosition())

