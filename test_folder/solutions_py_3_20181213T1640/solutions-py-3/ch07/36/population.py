#program to read the companion file census.csv
#and output a newfile population.csv that contains
#name of a state and its populatiion

def main():
    convertCsv("census.csv", "population.csv")
    

def convertCsv(src,dst):
    #open the census file
    infile=open(src)
    from csv import reader
    csvReader=reader(infile)

    #open the output csv file which will contain only the name and population
    outfile=open(dst,"w",  newline='')
    from csv import writer
    csvWriter=writer(outfile)

    #Note that columns 5 and 6 of census.csv contain the name and population
    #We read a row from census.csv into a list called row
    #row[4] and row[5] will contain the name and population 
    for row in csvReader:
        line=[]   #new list to store a row for the output file
        line.append(row[4])  #add the state name
        line.append(row[5])  #add the state's population
        #print(line)
        csvWriter.writerow(line) #write the row to the output file
        
    #close the input file
    infile.close()
    #close the output file
    outfile.close()

main()

