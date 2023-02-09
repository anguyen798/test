##
#  Implement the discount for a pet shop.
#

# Define constant variables.
DISCOUNT_FRACTION = 0.20

def main() :
   prices = []
   isPets = []

   # Read all of the prices and pet statuses from the user and store them in
   # two lists.
   price = float(input("Enter the price (-1 to quit): "))
   while price != -1 :
      prices.append(price)
      isPet = input("Is it a pet (Y / N)? ")

      if isPet.upper() == "Y" :
         isPets.append(True)
      else :
         isPets.append(False)
    
      price = float(input("Enter the price (-1 to quit): "))

   # Compute and display the discount amount.
   amount = discount(prices, isPets, len(prices))
   print("The discount is $%.2f." % amount)

## Compute the discount for a transaction.
#  @param prices the list of prices
#  @param isPet the list of True / False values indicating if it is a pet
#  @param nItems the number of items in the transaction
#  @return the amount that should be taken off as a discount
#
def discount(prices, isPet, nItems) :
   amount = 0

   # There is only a discount if the user has purchased a pet.
   if True in isPet :
      # Find all of the non-pet items and compute the discount on them.
      for i in range(0, nItems) :
         if not isPet[i] :
            amount = amount + prices[i] * DISCOUNT_FRACTION

   return amount

# Call the main function.
main()

