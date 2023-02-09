## Bar width
# Use the bar width option to produce a graph with two sets of bars
# (with a different color for the low and high temperatures) using the
# Fairbanks data from Toolbox 3.2.

from matplotlib import pyplot

# Create bars for high temperatures
pyplot.bar(0.5,1.1,color="green", width=0.5)
pyplot.bar(1.5,10.0,color="green", width=0.5)
pyplot.bar(2.5,25.4,color="green", width=0.5)
pyplot.bar(3.5,44.5,color="green", width=0.5)
pyplot.bar(4.5,61.0,color="green", width=0.5)
pyplot.bar(5.5,71.6,color="green", width=0.5)
pyplot.bar(6.5,72.7,color="green", width=0.5)
pyplot.bar(7.5,65.9,color="green", width=0.5)
pyplot.bar(8.5,54.6,color="green", width=0.5)
pyplot.bar(9.5,31.9,color="green", width=0.5)
pyplot.bar(10.5,10.9,color="green", width=0.5)
pyplot.bar(11.5,4.8,color="green", width=0.5)

# Create bars for low temperatures
pyplot.bar(1,-16.9,color="blue", width=0.5)
pyplot.bar(2,-12.7,color="blue", width=0.5)
pyplot.bar(3,-1.5,color="blue", width=0.5)
pyplot.bar(4,20.6,color="blue", width=0.5)
pyplot.bar(5,37.8,color="blue", width=0.5)
pyplot.bar(6,49.3,color="blue", width=0.5)
pyplot.bar(7,52.3,color="blue", width=0.5)
pyplot.bar(8,46.4,color="blue", width=0.5)
pyplot.bar(9,35.1,color="blue", width=0.5)
pyplot.bar(10,16.5,color="blue", width=0.5)
pyplot.bar(11,-5.7,color="blue", width=0.5)
pyplot.bar(12,-12.9,color="blue", width=0.5)


# Change the x limits to give some padding
pyplot.xlim(-0.5, 13.5)

# Add descriptive information.
pyplot.title("Average high and low temperatures")
pyplot.xlabel("Month")
pyplot.ylabel("Temperature")

# Add the letter grades as labels under the bars.
pyplot.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
              ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Display the graph.
pyplot.show()

