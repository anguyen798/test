## 
#  This program processes a collection of sales data for flavors of ice cream
#  and prints a report sorted by flavor.
#

def main() : 
   (headings, salesData) = readData("icecream.txt")
   printReport(headings, salesData)

## Reads the tabular data.
#  @param filename name of the input file
#  @return a list of headings and a dictionary whose keys are ice cream flavors and whose values are sales data
#
def readData(filename) :
   # Create an empty dictionary.
   salesData = {}
   
   infile = open(filename, "r")
   
   # Read the header out of the file.
   header = infile.readline().rstrip()
   headings = header.split(":")

   # Read each record from the file.   
   line = infile.readline()
   while line != "" :
      fields = line.split(":")
      flavor = fields[0]
      salesData[flavor] = buildList(fields)
      line = infile.readline()

   infile.close()   
   return (headings, salesData)

## Builds a list of store sales contained in the fields split from a string.
#  @param fields a list of strings comprising the record fields
#  @return a list of floating-point values
#
def buildList(fields) :
   storeSales = []
   for i in range(1, len(fields)) :
      sales = float(fields[i])
      storeSales.append(sales)
      
   return storeSales
   
## Prints a sales report.
#  @param headings the store names for the columns of data
#  @param salesData a table composed of a dictionary of lists
#
def printReport(headings, salesData) :
   # Find the number of stores as the length of the longest store sales list.
   numStores = 0
   for storeSales in salesData.values() :
      if len(storeSales) > numStores :
         numStores = len(storeSales)

   # Create a list of store totals.
   storeTotals = [0.0] * numStores
   
   # Print the headings.
   print("%15s" % " ", end = "")
   for heading in headings :
      print("%16s" % heading, end="")
   print()

   # Print the flavor sales.
   for flavor in sorted(salesData) :
      print("%-15s" % flavor, end="")
      
      flavorTotal = 0.0
      storeSales = salesData[flavor]
      for i in range(len(storeSales)) :
         sales = storeSales[i]
         flavorTotal = flavorTotal + sales
         storeTotals[i] = storeTotals[i] + sales
         print("%16.2f" % sales, end="")
         
      print("%15.2f" % flavorTotal)
         
   # Print the store totals.
   print("%15s" % " ", end="")
   for i in range(numStores) :
      print("%16.2f" % storeTotals[i], end="")
   print()

# Start the program.   
main()

