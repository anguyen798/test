## 
#  This module defines the CashRegister class.
#

## A simulated cash register that tracks the item count and the total amount due.
#
class CashRegister :
   ## Constructs a cash register with cleared item count and total.
   # @param taxRate the tax rate to use with this cash register
   #
   def __init__(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      self._dayCount = 0
      self._dayTotal = 0.0
      
   ## Adds an item to this cash register.
   #  @param price the price of this item
   #
   def addItem(self, price) :
      # If we are starting a new sale, count it.
      if self._itemCount == 0 :
         self._dayCount = self._dayCount + 1
      self._dayTotal = self._dayTotal + price
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price 
      
   ## Gets the price of all items in the current sale.
   #  @return the total price
   #
   def getTotal(self) :
      return self._totalPrice
      
   ## Gets the number of items in the current sale.
   #  @return the item count
   #
   def getCount(self) :
      return self._itemCount

   ## Clears the item count and the total.
   #  
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0

   ## Gets the sales total for the day.
   #  @return the total value of sales for the day
   #
   def getSalesTotal(self) :
      return self._dayTotal

   ## Gets the count of the number of sales for the day.
   #  @return the number of sales for the day
   def getSalesCount(self) :
      return self._dayCount

   ## Clear the daily count and sales total.
   #
   def resetSales(self) :
      self._dayTotal = 0.0
      self._dayCount = 0

