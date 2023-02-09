##
#  Convert from meters to miles, feet and inches.
#
METERS_PER_MILE = 1609.34
METERS_PER_FOOT = 0.3048
METERS_PER_INCH = 0.0254

# Read input from the user.
meters = float(input("Enter a length in meters: "))

# Compute miles, feet and inches.
miles = meters / METERS_PER_MILE
feet = meters / METERS_PER_FOOT
inches = meters / METERS_PER_INCH

# Display the result.
print(meters, "meters is %.2f miles." % miles)
print(meters, "meters is %.2f feet." % feet)
print(meters, "meters is %.2f inches." % inches)

