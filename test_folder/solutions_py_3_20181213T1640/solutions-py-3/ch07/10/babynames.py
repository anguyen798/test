##
#  This program displays the most common baby names. 
#

# The count limit to be extracted.
LIMIT = 2500000

def main() :
   
   filename = input("Enter the name of the input: ")
   inputFile = open(filename, "r")
   
   boyTotal = 0.0
   girlTotal = 0.0
   while boyTotal < LIMIT or girlTotal < LIMIT :      
      # Extract the data from the next line and split it.
      line = inputFile.readline()
      dataFields = line.split()

      # Extract the individual field values.
      rank = int(dataFields[0])
      boyName = dataFields[1]
      boyCount = float(dataFields[2].replace(",", ""))
      girlName = dataFields[3]
      girlCount = float(dataFields[4].replace(",", ""))
            
      # Process the data.            
      print("%3d " % rank, end="")
      boyTotal = processName(boyName, boyCount, boyTotal)
      girlTotal = processName(girlName, girlCount, girlTotal)
      print()
      
   inputFile.close()
   
## Prints the name if total >= 0 and adjusts the total.
#  @param name the boy or girl name
#  @param count the number of babies with this name
#  @param total the total count processed
#  @return the adjusted total
#
def processName(name, count, total) :
   if total < LIMIT :
      print("%-15s " % name, end="")

   total = total + count
   return total      
   
# Start the program.
main()

