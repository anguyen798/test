## Bridge bar chart
# Repeat Exercise P2.31 using pyplot to create the bar chart.

from matplotlib import pyplot

# Plot data on the graph.
pyplot.bar(1, 4200, color="blue")
pyplot.bar(2, 1595, color="green")
pyplot.bar(3, 2150, color="purple")
pyplot.bar(4, 3800, color="yellow")

# Add descriptive information.
pyplot.xlabel("Bridge")
pyplot.ylabel("Longest Span (ft)")

# Add a title that indicates the total number of students.
pyplot.title("Longest Bridges")

# Add the letter grades as labels under the bars.
pyplot.xticks([1.4, 2.4, 3.4, 4.4],
              ["Golden Gate", "Brooklyn", "Delaware Memorial", "Mackinac"])

# Display the graph.
pyplot.show()

