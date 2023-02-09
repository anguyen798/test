##
#  Display the state of water at a temperature provided by the user.
#

# Read the temperature and unit from the user.
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C or F): ")

# Convert to Celsius if the entered temperature was Fahrenheit.
if unit == "F" :
   temperature = (temperature - 32) * 5 / 9

# Determine the state.
if temperature < 0 :
   state = "solid"
elif temperature < 100 :
   state = "liquid"
else :
   state = "gaseous"

# Display the result.
print("At that temperature, the water is %s." % state)

