#program to read the companion file google.csv
#and write all columns except maximum and minum
#to a new file new.csv

#open the census file
infile=open("google.csv")
from csv import reader
csvReader=reader(infile)

#open the output csv file which will contain only the name and population
outfile=open("new.csv","w",  newline='')
from csv import writer
csvWriter=writer(outfile)

#loop through each row skipping row[2] and row[3] (Maximum and Minimum columns)
for row in csvReader:
    line=[]   #new list to store a row for the output file
    line.append(row[0])  #add the date
    line.append(row[1])  #add the open
    line.append(row[4]) #add the closing price
    line.append(row[5]) #add the shares colum 
    #print(line)
    csvWriter.writerow(line) #write the row to the output file

#print
print("Done creating output csv file")
#close the input file
infile.close()

#close the output file
outfile.close()

