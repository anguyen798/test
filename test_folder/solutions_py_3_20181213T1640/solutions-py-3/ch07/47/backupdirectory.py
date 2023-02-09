#Program that makes a backup of all files in a directory that are not already
#backup files.
#Appends the extension .bak to all backed-up files.
#skips directories
import os

def backup(src):
    #list of things in the directory
    srcContents=os.listdir(src)
    # loop through everything in the directory
    for name in srcContents:
        #create the full path for the file
        fullfilename = os.path.join(src, name)
        backupname= fullfilename+".bak"
        #check if name is a file
        if os.path.isfile(fullfilename):
            #create a backup if this is not already a *.bak file
            if "bak" not in fullfilename:
                print ("Backing up " + fullfilename)
                #create a backup
                copyfile(fullfilename,backupname)
            else:
                print("Skipping backup file "+ fullfilename )
        else:
            print("Skipping "+fullfilename+ " since it is a subdirectory")

#function to copy a file to another file
def copyfile(src, dst):
     #open the original file
     infile=open(src, mode='r')  
     #open the backup file
     outfile=open(dst, mode='w')
     #read one line at a time from the original file and write it to the backup file
     for line in infile:
         outfile.write(line)
     #close both files
     infile.close()
     outfile.close()
    

