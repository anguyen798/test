##
#  Define the country class.
#

## Represent a country, including its name, population and area.
#
class Country :
   ## Construct a new country.
   #  @param name the name of the country
   #  @param pop the population of the country
   #  @param area the area of the country
   #
   def __init__(self, name, pop, area) :
      self._name = name
      self._pop = pop
      self._area = area

   ## Get the name of the country.
   #  @return the name of the country
   #
   def getName(self) :
      return self._name

   ## Get the area of the country.
   #  @return the area of the country
   #
   def getArea(self) :
      return self._area

   ## Get the population of the country.
   #  @return the population of the country
   #
   def getPopulation(self) :
      return self._pop

   ## Get the population density of the country.
   #  @return the population density of the country
   #
   def getPopDensity(self) :
      return self.getPopulation() / self.getArea()

