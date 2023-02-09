## 
# Add curves for the average high and low temperatures in your hometown to
# the line graph program in Toolbox 3.2

from matplotlib import pyplot

# Plot data on the graph for Fairbanks
pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            [1.1, 10.0, 25.4, 44.5, 61.0, 71.6, 72.7,
             65.9, 54.6, 31.9, 10.9, 4.8])
pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            [-16.9, -12.7, -1.5, 20.6, 37.8, 49.3,
             52.3, 46.4, 35.1, 16.5, -5.7, -12.9])

# Plot data on the graph for Bowling Green
pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            [29.5, 38.5, 53.6, 66.2, 81.4, 91.6, 92.4,
             89.9, 80.1, 59.7, 36.2, 33.1])
pyplot.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            [14.9, 18.7, 28.5, 50.6, 67.8, 79.3,
             82.3, 76.4, 65.1, 46.5, 25.7, 18.9])

# Change the x limits to give some padding
pyplot.xlim(0.8, 12.2)

# Add descriptive information.
pyplot.title("Average Temperatures for Fairbanks and Bowling Green")
pyplot.xlabel("Month")
pyplot.ylabel("Temperature")
pyplot.legend(["High FB", "Low FB", "High BG", "Low BG"])

pyplot.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
              ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
               "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

# Display the graph.
pyplot.show()

