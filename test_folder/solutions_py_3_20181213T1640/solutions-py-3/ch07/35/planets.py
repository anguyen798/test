#import the plotting library
import matplotlib.pyplot
import numpy

def plotPlanets(a):
    #open the planets file
    infile=open(a,"r")
    #The masses are in the second row
    #read the first row containing the names
    row=infile.readline().rstrip()
    #store it in a list called names by splitting over the commas
    names=row.split(",")

    #read the row containing the masses
    row2=infile.readline().rstrip()
    #store in a list called m
    m=row2.split(",")

    #remove the first element from each list since it only contains headers
    del(names[0])
    del(m[0])
    #convert to floats from strings
    masses=[]
    for i in m:
        masses.append(float(i))

    #done with the file, so close it
    infile.close()

    #plot the masses
    y_pos=numpy.arange(len(names))
    matplotlib.pyplot.bar(y_pos,masses,align='center', alpha=0.5, color='blue')
    matplotlib.pyplot.xticks(y_pos,names)
    matplotlib.pyplot.ylabel("Masses")
    matplotlib.pyplot.show()

