import csv
import scipy.stats
import matplotlib.pyplot

def main():
   pci = []  #percapitaincome
   lifeexp = [] #life expectancy
   tered=[] #tertiary education
   pgdp=[] #per capita GDP
   gini=[]  #gini

   reader = csv.reader(open("oecd.csv"))
   next(reader) # Skip header row
   for row in reader:
      pci.append(float(row[1]))
      lifeexp.append(float(row[2]))
      tered.append(float(row[3]))
      pgdp.append(float(row[5]))
      gini.append(float(row[6]))

   r = scipy.stats.linregress(pci, lifeexp)
   slope = r[0]
   intercept = r[1]
   correlation = r[2]
   print("Correlation coefficient for per capita income and life expectancy: %f" % coeff(pci,lifeexp))
   print("Correlation coefficient for per capita income and tertiary eduction: %f" % coeff(pci,tered))
   print("Correlation coefficient for per capita income and per capita GDP: %f" % coeff(pci,pgdp))
   print("Correlation coefficient for per capita income and gini: %f" % coeff(pci,gini))

def coeff(a,b):
   r = scipy.stats.linregress(a,b)
   return r[2]

main()

