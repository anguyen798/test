## Pie Chart
# Draw a pie chart of the areas of all continents. Provide a legend for the chart. 

from matplotlib import pyplot

labels = ['Asia',
          'Africa',
          'North America',
          'South America',
          'Antarctica',
          'Europe',
          'Australia']
sizes = [44.6, 30.1, 24.2, 17.8, 13.2, 9.9, 8.1]
colors = ['red', 'brown', 'blue', 'green', 'white', 'orange','tan']
explode = (0, 0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Africa')

pyplot.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)
# Set aspect ratio to be equal so that pie is drawn as a circle.
pyplot.axis('equal')
pyplot.legend(labels, loc=6, fontsize=9)

pyplot.show()

