## Color bars based on temp
# Change the color of the bar chart in Toolbox 3.2.  Draw the bars that
# stay below 32 degrees in blue, the othrers in yellow.

from matplotlib import pyplot

# Plot data on the graph.
pyplot.bar(1, 1.1, color="blue")
pyplot.bar(2, 10.0, color="blue")
pyplot.bar(3, 25.4, color="blue")
pyplot.bar(4, 44.5, color="yellow")
pyplot.bar(5, 61.0, color="yellow")

# Add descriptive information.
pyplot.xlabel("Month")
pyplot.ylabel("Temperature")

# Display the graph.
pyplot.show()

