##
#  Generate random integers and display them in different ways.
#
from random import randint

# Define constant variables.
NUM_INTEGERS = 10

# Generate the random integers.
values = []
for i in range(0, NUM_INTEGERS) :
   values.append(randint(0, NUM_INTEGERS))

# Display the elements at even index.
print("Elements at even index: ", end="")
for i in range(0, NUM_INTEGERS, 2) :
   print(values[i], end=" ")
print() 

# Display the even elements.
print("The even elements are: ", end="")
for i in range(0, NUM_INTEGERS) :
   if values[i] % 2 == 0 :
      print(values[i], end=" ")
print()

# Display the elements in reverse order.
print("In reverse order: ")
for i in range(NUM_INTEGERS - 1, -1, -1) :
   print(values[i], end=" ")
print()

# Display the first and last element.
print("First and last: ", values[0], values[len(values) - 1])

