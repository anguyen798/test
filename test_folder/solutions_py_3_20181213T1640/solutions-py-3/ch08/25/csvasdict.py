import csv
#method to read given csv student file using DictReader
#prints the IDs and names of the students with the highest and lowest scores
def main():
    readCsvAsDict("student.csv")
def readCsvAsDict(filename):

    infile=open(filename)
    #read using DictReader
    csvReader=csv.DictReader(infile)

    #initialize the high and low score
    highScore=None
    lowScore=None
    highId=""
    highName=""
    lowId=""
    lowName=""
    
    #read each row as a dictionary
    for row in csvReader:
        score=int(row['score'])
        if highScore==None or highScore<score:
            highScore=score
            highId=row['id'] #can fetch the id and name from the dictionary
            highName=row['name']
        
        if lowScore==None or lowScore>score:
            lowScore=score
            lowId=row['id'] #can fetch the id and name from the dictionary
            lowName=row['name']
        
        
    print("Student with the highest score is:")
    print("Name: "+ highName+ " Id: "+highId)
    print("Student with the lowest score is:")
    print("Name: "+ lowName+ " Id: "+lowId)

main()

