import os


#method to write data to file
#creates a backup if the existing file has contents not the same as data
def saveWithBackup(data,file):
    #check if a file exists with the same name
    if os.path.exists(file):
        infile=open(file, 'r')
        #read the contents of the file into the string olddata
        olddata=infile.read()
        #close the file
        infile.close()
        
        #if the contents are not the same, create a bakup
        if olddata!=data:
            backupfilename=file+".bak"
            outfile=open(backupfilename,mode="w")
            outfile.write(olddata)
            print("Old file backed up and new file created")
            outfile.close()
        else:
            print("File is unchanged - skipping backup")
    #write the new data
    outfile=open(file, mode="w")
    outfile.write(data)
    outfile.close()

