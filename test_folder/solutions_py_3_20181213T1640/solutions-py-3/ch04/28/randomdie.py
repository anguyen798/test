##  
# Generate 1000 random die tosses and show a histogram with the number of
# times that the result is 1, 2, 3, 4, 5, or 6.  Use the technique of
# Worked Example 4.2.

from matplotlib import pyplot
import random
# Initialize the variables used to maintain the grade counts.
num1s = 0
num2s = 0
num3s = 0
num4s = 0
num5s = 0
num6s = 0

numRolls = 1000

for i in range(numRolls):
    rand = random.randrange(6) + 1
    if rand == 1:
        num1s += 1
    elif rand == 2:
        num2s += 1
    elif rand == 3:
        num3s += 1
    elif rand == 4:
        num4s += 1
    elif rand == 5:
        num5s += 1
    elif rand == 6:
        num6s += 1

# Plot the grade distribution.
pyplot.bar(1, num1s)
pyplot.bar(2, num2s)
pyplot.bar(3, num3s)
pyplot.bar(4, num4s)
pyplot.bar(5, num5s)
pyplot.bar(6, num6s)

# Add axis labels.
pyplot.xlabel("Die Roll")
pyplot.ylabel("Number of Rolls")

# Add a title that indicates the total number of students.
pyplot.title("%d die rolls\nDie Roll Distribution" % numRolls)

# Add the letter grades as labels under the bars.
pyplot.xticks([1.4, 2.4, 3.4, 4.4, 5.4, 6.4], ["1", "2", "3", "4", "5", "6"])

# Display the graph.
pyplot.show()

