##  
# Generate 1000 random integers between 1 and 999,999.  Show a histogram
# with the number of times that the *first* digit of the result is 1, 2, 3,
# 4, 5, 6, 7, 8, or 9.  Use the technique of Worked Example 4.2.

from matplotlib import pyplot
import random
# Initialize the variables used to maintain the grade counts.
num1s = 0
num2s = 0
num3s = 0
num4s = 0
num5s = 0
num6s = 0
num7s = 0
num8s = 0
num9s = 0

numIntegers = 100
maxRange = 999999

for i in range(numIntegers):
    rand = random.randrange(maxRange) + 1
    #print("Starting:",rand)
    while rand > 10:
        rand /= 10
        #print("  Next:",rand)
    rand = int(rand)
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
    elif rand == 7:
        num7s += 1
    elif rand == 8:
        num8s += 1
    elif rand == 9:
        num9s += 1

# Plot the grade distribution.
pyplot.bar(1, num1s)
pyplot.bar(2, num2s)
pyplot.bar(3, num3s)
pyplot.bar(4, num4s)
pyplot.bar(5, num5s)
pyplot.bar(6, num6s)
pyplot.bar(7, num7s)
pyplot.bar(8, num8s)
pyplot.bar(9, num9s)

# Add axis labels.
pyplot.xlabel("First Digit")
pyplot.ylabel("Number of Occurrences")

# Add a title that indicates the total number of students.
pyplot.title("%d random integers\nFirst Digit Distribution" % numIntegers)

# Add the letter grades as labels under the bars.
pyplot.xticks([1.4, 2.4, 3.4, 4.4, 5.4, 6.4, 7.4, 8.4, 9.4],
              ["1", "2", "3", "4", "5", "6", "7", "8", "9"])

# Display the graph.
pyplot.show()

