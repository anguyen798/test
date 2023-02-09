##
#  Read a radius and compute properties of circles and spheres.
#
from math import pi

# Read the radius from the user.
radius = float(input("Enter the radius: "))

# Compute the area and circumference.
area = pi * radius * radius
circumference = 2 * pi * radius

# compute the volume and surface area.
volume = 4 / 3 * pi * radius ** 3
surface_area = 4 * pi * radius * radius

# Display the results.
print("The circle has area %.2f." %  area)
print("The circle has circumference %.2f." %  circumference)
print("The sphere has volume %.2f." %  volume)
print("The sphere has surface area %.2f." %  surface_area)

