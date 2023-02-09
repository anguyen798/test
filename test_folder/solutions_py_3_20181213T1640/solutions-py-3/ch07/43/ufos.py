import csv
import scipy.stats
import matplotlib.pyplot

population = []
ufos = []

reader = csv.reader(open("states.csv"))
next(reader) # Skip header row
for row in reader:
   population.append(int(row[1]))
   ufos.append(int(row[2]))

r = scipy.stats.linregress(ufos,population)
slope = r[0]
intercept = r[1]
correlation = r[2]
print("Correlation coefficient: %f" % correlation)

matplotlib.pyplot.scatter(ufos,population)

x1 = min(ufos)
y1 = intercept + slope * x1
x2 = max(ufos)
y2 = intercept + slope * x2
matplotlib.pyplot.plot([x1,x2],[y1,y2])
matplotlib.pyplot.show()

