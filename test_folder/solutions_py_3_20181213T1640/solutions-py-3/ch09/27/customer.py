##
#  Define the customer class.
#

## The customer class keeps track of how much a customer spends at 20 different
#  shops and determines his eligibility for a discount.
class Customer :
   ## Construct a new customer who has not yet purchased anything.
   #  
   def __init__(self) :
      self._purchased = [0] * 21

   ## Record a purchase made by the customer.
   #  @param amount the amount of the purchase
   #  @param shop the number of the shop where the purchase was made
   #
   def makePurchase(self, amount, shop) :
      self._purchased[shop] = self._purchased[shop] + amount

   ## Determine if the customer is eligible for the discount.
   #  @return True if eligible for the discount, False otherwise
   #
   def discountReached(self) :
      count = 0
      for amt in self._purchased :
         if amt != 0 :
            count = count + 1
      return count >= 3 and sum(self._purchased) >= 100.00

