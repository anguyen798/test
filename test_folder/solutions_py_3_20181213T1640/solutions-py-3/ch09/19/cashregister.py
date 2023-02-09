## 
#  This module defines the CashRegister class.
#

## A simulated cash register that tracks the number of items and the total 
#  cost by keeping a list of all the items.
#
class CashRegister :
   ## Constructs a cash register with cleared item count and total.
   # @param taxRate the tax rate to use with this cash register
   #
   def __init__(self) :
      self._prices = []
      
   ## Adds an item to this cash register.
   #  @param price the price of this item
   #
   def addItem(self, price) :
      self._prices.append(price)
      
   ## Gets the price of all items in the current sale.
   #  @return the total price
   #
   def getTotal(self) :
      return sum(self._prices)
      
   ## Gets the number of items in the current sale.
   #  @return the item count
   #
   def getCount(self) :
      return len(self._prices)

   ## Clears the item count and the total.
   #  
   def clear(self) :
      self._prices = []

   ## Display all of the prices in the current sale.
   #
   def displayAll(self) :
      for amt in self._prices :
         print(amt)

