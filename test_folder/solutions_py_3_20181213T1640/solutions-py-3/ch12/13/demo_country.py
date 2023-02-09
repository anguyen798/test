##
#  Identify the country with the largest population, the largest area,
#  and the largest population density.
#
from country import Country

def main() :
   # Read the data form the file and construct a list of countries.
   countries = set()
   inf = open("data.txt", "r")
   for line in inf:
      parts = line.split("\t")
      name = parts[0]
      pop = int(parts[1].replace(",", ""))
      area = float(parts[2].replace(",", ""))
      countries.add(Country(name, pop, area))
   
   # Close the data file.
   inf.close()

   # Find and display the country with the largest population.
   countries = sorted(countries, key=Country.getPopulation, reverse=True)
   for c in countries :
      print(c)

# Call the main function.
main()

