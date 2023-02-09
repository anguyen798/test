##
#  Display the state of water at a temperature provided by the user.
#

# Define constants.
FEET_TO_METERS = 0.3048
F_TO_C_OFFSET = 32
F_TO_C_FACTOR = 5 / 9
WATER_MP = 0

# Read the temperature, unit, altitude and unit from the user.
temperature = float(input("Enter the temperature: "))
temp_unit = input("Enter the unit (C or F): ")

altitude = float(input("Enter the altitude: "))
alt_unit = input("Enter the unit (m or ft): ")

# Convert to Celsius if the entered temperature was Fahrenheit.
if temp_unit == "F" :
   temperature = (temperature - F_TO_C_OFFSET) * F_TO_C_FACTOR

# Convert to meters if the altitude was entered in feet.
if alt_unit == "ft" :
   altitude = altitude * FEET_TO_METERS

# Determine the state.
boiling_point = 100 - altitude / 300
if temperature < WATER_MP :
   state = "solid"
elif temperature < boiling_point :
   state = "liquid"
else :
   state = "gaseous"

# Display the result.
print("At that temperature, the water is %s." % state)

