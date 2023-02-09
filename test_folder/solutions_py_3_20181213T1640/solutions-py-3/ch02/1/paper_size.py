##
#  Display the dimensions of a letter size sheet of paper in millimeters.
#
WIDTH_INCHES = 8.5
HEIGHT_INCHES = 11
MM_PER_INCH = 25.4

# Compute the width and height in millimeters.
width_mm = WIDTH_INCHES * MM_PER_INCH
height_mm = HEIGHT_INCHES * MM_PER_INCH

# Display the result.
print("Letter size paper is %.1fmm by %.1fmm" % (width_mm, height_mm))

