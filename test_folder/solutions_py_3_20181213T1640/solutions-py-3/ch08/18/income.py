##
#  Read a database of per capita income by country and allow the user to
#  query it.
#

# Load the data into a dictionary.
incomes = {}
inf = open("rawdata_2004.txt", "r")
for line in inf:
   parts = line.split("\t")

   # Remove the dollar sign and comma.
   parts[2] = parts[2].replace("$", "")
   parts[2] = parts[2].replace(",", "")

   # Add the country to the dictionary.
   incomes[parts[1].upper()] = float(parts[2])

# Create a dictionary that maps from the letters of the alphabet to the
# countries that with names that start with that letter.
letters = {}
for k in incomes.keys() :
   if k[0] not in letters :
      letters[k[0]] = set()
   letters[k[0]].add(k)

# Read queries from the user and respond to them.
country = input("Enter a country name (or type quit to quit): ").upper()
while country != "QUIT" :
   if len(country) == 1 :
      if country in letters :
         for name in sorted(letters[country]) :
            print(name)
      else :
         print("No countries start with that letter.")
   elif country in incomes :
      print("The per capita income is", incomes[country])
   else :
      print("That wasn't a recognized country.")
   print()

   # Read the next country from the user.
   country = input("Enter a country name (or type quit to quit): ").upper()

