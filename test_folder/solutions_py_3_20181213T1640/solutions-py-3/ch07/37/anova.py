import statistics
import scipy.stats

def mathscience(filename):
   white = []
   black = []
   asian = []
   boys = []
   girls = []

   # Data from http://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014028
      
   infile = open(filename)
   for line in infile :
      gender = line[46 : 47]
      race = line[2331 : 2332]
      minPerPeriodMath = int(line[252 : 256])
      periodsPerWeekMath = int(line[264 : 268])
      minPerPeriodSc=int(line[256:260])
      periodsPerWeekSc=int(line[268 : 272])
      
      # codes of 0 and >= 1000 are used for invalid responses
      if minPerPeriodMath > 0 and minPerPeriodMath < 1000 and \
         periodsPerWeekMath > 0 and periodsPerWeekMath < 1000 :
         hours = minPerPeriodMath * periodsPerWeekMath / 60
         if gender == "1" :
            girls.append(hours)
         elif gender == "2":
            boys.append(hours)
         if race == "1" :
            white.append(hours)
         elif race == "2" :
            black.append(hours)
         elif race == "3" :
            asian.append(hours)

      # codes of 0 and >= 1000 are used for invalid responses
      if minPerPeriodSc > 0 and minPerPeriodSc < 1000 and \
         periodsPerWeekSc > 0 and periodsPerWeekSc < 1000 :
         hours = minPerPeriodSc * periodsPerWeekSc / 60
         if gender == "1" :
            girls.append(hours)
         elif gender == "2":
            boys.append(hours)
         if race == "1" :
            white.append(hours)
         elif race == "2" :
            black.append(hours)
         elif race == "3" :
            asian.append(hours)
   infile.close()

   #   print(scipy.stats.normaltest(boys))

   print("Analysis for math and science instruction")
   print("White: %d responses, mean %f" % (len(white), statistics.mean(white)))
   print("Black: %d responses, mean %f" % (len(black), statistics.mean(black)))
   print("Asian: %d responses, mean %f" % (len(asian), statistics.mean(asian)))
   p = scipy.stats.f_oneway(white,black,asian)[1]
   print("p = %f" % p)

   print("Boys: %d responses, mean %f" % (len(boys), statistics.mean(boys)))
   print("Girls: %d responses, mean %f" % (len(girls), statistics.mean(girls)))
   p = scipy.stats.f_oneway(boys, girls)[1]
   print("p = %f" % p)

