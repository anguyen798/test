##
#  Compute the cost to travel 100 miles, and how far a car can go on a tank
#  of gas.
#

# Gather input from the user.
tank_amount = float(input("Enter the amount of gas in the tank: "))
mpg = float(input("Enter the fuel efficiency in mpg: "))
price = float(input("Enter the cost of a gallon of gas: "))

# Compute the gas cost to drive 100 miles and the distance that can be
# drive with the gas in the tank.
cost100 = 100 / mpg * price
distance = tank_amount * mpg

# Display the result.
print("It take $%.2f of fuel to drive 100 miles." % cost100)
print("The car can travel", distance, "miles with the gas in the tank.")

