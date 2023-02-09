##
#  Display the state of water at a temperature provided by the user.
#
from sys import exit

# Define constants.
FEET_TO_METERS = 0.3048
F_TO_C_OFFSET = 32
F_TO_C_FACTOR = 5 / 9
WATER_MP = 0

# Read the temperature from the user.
temperature = float(input("Enter the temperature: "))

# Read the temperature unit and verify that it is C or F (in any case).
temp_unit = input("Enter the unit (C or F): ")
temp_unit = temp_unit.upper()
if temp_unit != "C" and temp_unit != "F" :
   exit("That wasn't a valid temperature unit.")

# Read the altitude and verify that it is numeric.
inputStr = input("Enter the altitude: ")
if not inputStr.isdigit() :
   exit("That wasn't a valid altitude.")
altitude = float(inputStr)

# Read the altitude unit and verify that it is m or ft (in any case).
alt_unit = input("Enter the unit (m or ft): ")
alt_unit = alt_unit.upper()
if alt_unit != "M" and alt_unit != "FT" :
   exit("That wasn't a valid altitude unit.")

# Convert to Celsius if the entered temperature was Fahrenheit.
if temp_unit == "F" :
   temperature = (temperature - F_TO_C_OFFSET) * F_TO_C_FACTOR

# Convert to meters if the altitude was entered in feet.
if alt_unit == "FT" :
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

