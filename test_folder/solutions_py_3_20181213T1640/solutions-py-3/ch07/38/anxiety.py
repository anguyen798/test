import statistics
import scipy.stats

def anxietyAnalysis(filename):
   white = []
   black = []
   asian = []
   boys = []
   girls = []
      
   infile = open(filename)
   for line in infile :
      anxiety1 = int(line[147 : 148])
      anxiety2 = int(line[149 : 150])
      anxiety3 = int(line[151 : 152])
      anxiety4 = int(line[154 : 155])
      anxiety5=int(line[156:157])
      gender = line[46 : 47]
      race = line[2331 : 2332]
      #ensure student responded to all 5 questions
      if anxiety1>0 and anxiety1<=5 and anxiety2>0 and anxiety2<=5 and anxiety3>0 and anxiety3<=5 and anxiety4>0 and anxiety4<=5 and anxiety5>0 and anxiety5<=5:
         avganxiety=(anxiety1+anxiety2+anxiety3+anxiety4+anxiety5)/5
         if gender == "1" :
            girls.append(avganxiety)
         elif gender == "2":
            boys.append(avganxiety)
         if race == "1" :
            white.append(avganxiety)
         elif race == "2" :
            black.append(avganxiety)
         elif race == "3" :
            asian.append(avganxiety)
   print ("Average of anxiety responses analyzed 1(not anxious)- 5(very anxious)")
   print("White: %d responses, mean %f" % (len(white), statistics.mean(white)))
   print("Black: %d responses, mean %f" % (len(black), statistics.mean(black)))
   print("Asian: %d responses, mean %f" % (len(asian), statistics.mean(asian)))
   p = scipy.stats.f_oneway(white,black,asian)[1]
   print("p = %f" % p)

   print("Boys: %d responses, mean %f" % (len(boys), statistics.mean(boys)))
   print("Girls: %d responses, mean %f" % (len(girls), statistics.mean(girls)))
   p = scipy.stats.f_oneway(boys, girls)[1]
   print("p = %f" % p)

