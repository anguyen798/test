import os

def main():
    beginBackup("test.txt")
    beginBackup("test.txt.bak")

    
def beginBackup(name):
    bakupname=name+".bak"
    backup(name, bakupname)
    print("Backed up to "+ bakupname)

def backup(file, backupname):
     #if the backup file already exists delete it
     if os.path.exists(backupname):
        os.remove(backupname)
     #open the original file
     infile=open(file, mode='r')
     
     #open the backup file
     outfile=open(backupname, mode='w')

     #read one line at a time from the original file and write it to the backup file
     for line in infile:
         outfile.write(line)

     #close both files
     infile.close()
     outfile.close()
     
         
        

