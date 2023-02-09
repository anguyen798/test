##
#  Perform unit conversions, rejecting incompatible units.
#
from sys import exit

# Read the unit to convert from and to.
fromUnit = input("Convert from? ")
toUnit = input("Convert to? ")

# Volume units.
if fromUnit == "fl. oz" and toUnit == "ml" :
   factor = 29.5735
elif fromUnit == "fl. oz" and toUnit == "l" :
   factor = 0.0295735
elif fromUnit == "gal" and toUnit == "ml" :
   factor = 3785.41
elif fromUnit == "gal" and toUnit == "l" :
   factor = 3.78541

# Weight / mass units.
elif fromUnit == "oz" and toUnit == "g" :
   factor = 28.3495
elif fromUnit == "oz" and toUnit == "kg" :
   factor = 0.0283495
elif fromUnit == "lb" and toUnit == "g" :
   factor = 453.592
elif fromUnit == "lb" and toUnit == "kg" :
   factor = 0.453592

# Distance units.
elif fromUnit == "in" and toUnit == "mm" :
   factor = 25.4
elif fromUnit == "in" and toUnit == "cm" :
   factor = 2.54
elif fromUnit == "in" and toUnit == "m" :
   factor = 0.0254
elif fromUnit == "in" and toUnit == "km" :
   factor = 0.0000254
elif fromUnit == "ft" and toUnit == "mm" :
   factor = 304.8
elif fromUnit == "ft" and toUnit == "cm" :
   factor = 30.48
elif fromUnit == "ft" and toUnit == "m" :
   factor = 0.3048
elif fromUnit == "ft" and toUnit == "km" :
   factor = 0.0003048
elif fromUnit == "mi" and toUnit == "mm" :
   factor = 1609344
elif fromUnit == "mi" and toUnit == "cm" :
   factor = 160934.4
elif fromUnit == "mi" and toUnit == "m" :
   factor = 1609.344
elif fromUnit == "mi" and toUnit == "km" :
   factor = 1.609344

# Incompatible units.
else :
   exit("Those units are not compatible.")
   
# Read the value to convert from the user.
value = float(input("Value? "))

# Compute the result.
result = value * factor

# Display the result.
print(value, fromUnit, "=", result, toUnit)

