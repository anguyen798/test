POPULATION_FILE = "worldpop.txt"
AREA_FILE = "worldarea.txt"
from scipy import stats
def main() :
    # Open the files.
    popFile = open(POPULATION_FILE, "r")
    areaFile = open(AREA_FILE, "r")
    data=[[],[]]  #the first list in data will contain the area, the second the population
    # Read the first population data record.
    popData = extractDataRecord(popFile)
    while len(popData) == 2 :
        # Read the next area data record.
        areaData = extractDataRecord(areaFile)
        # Extract the data components from the two lists.
        population = popData[1]
        area=areaData[1]
        #add the area and population of this country to our two lists in data[]
        data[0].append(area)
        data[1].append(population)
        popData = extractDataRecord(popFile)

    #compute correlation between size and population
    r=stats.linregress(data[0], data[1])
    slope=r[0]
    intercept=r[1]
    correlation=r[2]
    print("The correlation between area and population is ", correlation)

    # Close the files.
    popFile.close()
    areaFile.close()

## Extracts and returns a record from an input file in which the data is
# organized by line. Each line contains the name of a country (possibly
# containing multiple words) followed by an integer (either population
# or area for the given country).
# @param infile the input text file containing the line oriented data
# @return a list containing the country (string) in the first element
# and the population (int) or area (int) in the second element. If the end of
# file was reached, an empty list is returned
#
def extractDataRecord(infile) :
    line = infile.readline()
    if line == "" :
        return []
    else :
        parts = line.rsplit(" ", 1)
        parts[1] = int(parts[1])
    return parts

main()

