import statistics
import scipy.stats

#initialize each race to track the number of responses
#for each category from 1-6 
white = [0,0,0,0,0,0]
black = [0,0,0,0,0,0]
asian = [0,0,0,0,0,0]


# Data from http://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014028
   
infile = open("US_ST12.TXT")
for line in infile :
   race = line[2331 : 2332]
   books = int(line[124:125])
   
   # check if response is in the valid range 1-6
   if books >=1 and books<=6:
      if race == "1" :
         #incremement the count for this category
         white[books-1]=white[books-1]+1
      elif race == "2" :
         black[books-1]=black[books-1]+1
      elif race == "3" :
         asian[books-1]=asian[books-1]+1
infile.close()
data=[]
data.append(white)
data.append(black)
data.append(asian)
#print(data)
#need to use Chi_square test here
#   print(scipy.stats.normaltest(boys))
p = scipy.stats.chi2_contingency(data)[1]

print("p = %f" % p)
if p>0.5:
   print("Differences in book counts are due to chance alone")
else:
   print("Differences in book counts reported are not due to chance")

