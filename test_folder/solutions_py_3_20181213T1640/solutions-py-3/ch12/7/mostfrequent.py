##
#  Find the most frequent element in a list.
#

# Test values for the algorithm.
values = [1, 2, 3, 1, 1, 2, 3, 4, 4, 1, 2, 3, 3, 2, 1]

# Find the most frequent value in the values list.
mostFrequent = 0
highestFrequency = 1
for i in range(len(values)) :
   count_rest = values[i + 1 : ].count(values[i])
   if count_rest > highestFrequency :
      highestFrequency = count_rest
      mostFrequent = values[i]

# Display the result.
print("The most frequent value is", mostFrequent)
print("Expected: 1")

