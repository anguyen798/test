##
#  Display the best customers of the day.
#

# Define constant variables.
NUM_NAMES = 3

def main() :
   sales = []
   names = []

   # Read the names and sales amounts, storing them in two lists.
   amount = float(input("Enter the sale amount: "))
   while amount != 0 :
      sales.append(amount)

      name = input("Enter the customer's name: ")
      names.append(name)

      amount = float(input("Enter the sale amount: "))

   # Compute and display the name of the best customers.
   bestNames = nameOfBestCustomers(sales, names, NUM_NAMES)
   print("The best customers were:")
   for name in bestNames :
      print(name)


## Identify the name of the best customer.
#  @param sales the list of sale amounts
#  @param customers the names of the customers
#  @return the name of the customer with the highest sale amount
#
def nameOfBestCustomers(sales, customers, topN) :
   best = []

   # Repeat until we have the number of customers desired, or all of the
   # customers.
   temp_sales = list(sales)
   temp_customers = list(customers)
   while len(temp_sales) > 0 and len(best) < topN :
      # Find the largest sale.
      largest = max(temp_sales)

      # Record the name of the best customer.
      for i in range(0, len(temp_sales)) :
         if temp_sales[i] == largest and len(best) < topN :
            best.append(temp_customers[i])

      # Remove the sales and the customers from the temp lists.
      while largest in temp_sales :      
         i = temp_sales.index(largest)
         temp_sales.pop(i)
         temp_customers.pop(i)
   
   return best

# Call the main function.
main()

