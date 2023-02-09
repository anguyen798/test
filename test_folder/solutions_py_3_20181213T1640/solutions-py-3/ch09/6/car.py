##
#  This module defines the car class.
#

##
#  A car that tracks its fuel consumption as it is driven.
class Car :
   ## Constructs a new car with a given fuel efficiency.
   #  @param fuel_efficiency the fuel efficiency of the car
   #
   def __init__(self, fuel_efficiency) :
      self._fuel_efficiency = fuel_efficiency
      self._gas = 0

   ## Add gas to the car's tank.
   #  @param amount the amount of gas to add
   def addGas(self, amount) :
      self._gas = self._gas + amount

   ## Simulate driving the car.
   #  @param distance the distance the car is driven
   def drive(self, distance) :
      self._gas = self._gas - distance / self._fuel_efficiency

   ## Get the amount of gas in the tank.
   #  @return the amount of gas in the tank
   def getGasLevel(self) :
      return self._gas

