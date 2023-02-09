##
#  Define the customer class.
#

## The customer class keeps track of how much a customer spends and determines
#  his eligibility for a discount.
class Customer :
   ## Construct a new customer who has not yet purchased anything.
   #  
   def __init__(self) :
      self._purchased = 0

   ## Record a purchase made by the customer.
   #  @param amount the amount of the purchase
   #
   def makePurchase(self, amount) :
      self._purchased = self._purchased + amount

   ## Determine if the customer is eligible for the discount.
   #  @return True if eligible for the discount, False otherwise
   #
   def discountReached(self) :
      return self._purchased >= 100.00

