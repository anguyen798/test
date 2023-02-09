##
#  Print instructions for brewing coffee.
#

def main() :
   brewCoffee()

## Print instructions to brew coffee.
#
def brewCoffee() :
   print("Add water to the coffee maker.")
   print("Put a filter in the coffee maker.")
   grindCoffee()
   print("Put coffee in the filter.")
   print("Close the coffee maker.")
   print("Start the coffee maker.")

## Print instructions to grind coffee.
#
def grindCoffee() :
   beanType = input("What kind of beans do you want to use? ")
   print("Add", beanType, "beans to the grinder.")
   time = input("How long would you like to grind the coffee? ")
   print("Grind the coffee for", time)

# Call the main function.
main()

