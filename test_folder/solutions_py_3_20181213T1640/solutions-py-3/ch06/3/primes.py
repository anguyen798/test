##
#  Identify and display all numbers that are not multiples of 2..100 (other 
#  than the numbers themselves).  This leaves just the prime numbers.
#

# Define constant values.
MAX_PRIME = 10000
MAX_MULTIPLE = 100

# Construct a list of all values from 2 to 10000.
values = []
for i in range(2, MAX_PRIME + 1) :
   values.append(i)

# Remove all of the multiples of 2 .. 100 (but not the values themselves).
for x in range(2, MAX_MULTIPLE) :
   i = 0
   while i < len(values) :
      if values[i] != x and values[i] % x == 0 :
         values.pop(i)
      else :
         i = i + 1

# Display the remaining values.
print(values)

