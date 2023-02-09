#read in names and grades from txt file
#computes the average and writes names, grades and average to a csv file

#open the input text file
infile=open("grades.txt", "r")

#open the output csv file 
outfile=open("grades.csv","w",  newline='')
from csv import writer
csvWriter=writer(outfile)
#Write the course header
csvWriter.writerow(["Basket Weaving 101","","","",""])
#Write a blank row
csvWriter.writerow(["","","","",""])
#write the headers for the csv file
csvWriter.writerow(["Student", "Exam 1", "Exam 2", "Exam 3", "Average"])

#read first line
line=infile.readline()
while line !="":            #check for end of file
    outputrow=[]   #list to store output row for csv file
    studentname=line.rstrip() #remove the \n
    #add the name to the outputrow
    outputrow.append(studentname)
    
    #read the next line containing grades and remove \n
    line=infile.readline().rstrip()
    grades=line.split()  #add grades to a list by using split
    #calculate the average of the grades
    total=0.0
    for g in grades:
        testScore=float(g) #need to convert each grade from a string to float
        outputrow.append(testScore)  #add the test grade to the output list
        total=total+testScore
    average=total/len(grades)
    avg=round(average,2)
    #append the average to the output list
    outputrow.append(avg)
    #write the output
    csvWriter.writerow(outputrow)
    line=infile.readline() #read the next name

print("csv file created")

#close the files
infile.close()
outfile.close()

