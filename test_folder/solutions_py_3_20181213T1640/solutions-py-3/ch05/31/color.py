##
#  Compute the color for a temperature value between 0 and 100.
#
def main() :
   print(colorForValue(0))
   print(colorForValue(10))
   print(colorForValue(25))
   print(colorForValue(40))
   print(colorForValue(50))
   print(colorForValue(65))
   print(colorForValue(75))
   print(colorForValue(90))
   print(colorForValue(100))

## Compute the color for a given temperature.
#  @param temperature the temperature value that needs a color
#  @return the color for the temperature
#
def colorForValue(temperature) :
   # Scale temperatures between 0 and 25 between blue and cyan.
   if temperature < 25 :
      red = interpolate(temperature, 0, 25, 0, 0)
      green = interpolate(temperature, 0, 25, 0, 255)
      blue = interpolate(temperature, 0, 25, 255, 255)
   # Scale temperatures between 25 and 50 between cyan and green.
   elif temperature < 50 :
      red = interpolate(temperature, 25, 50, 0, 0)
      green = interpolate(temperature, 25, 50, 255, 255)
      blue = interpolate(temperature, 25, 50, 255, 0)
   # Scale temperatures between 50 and 75 between green and yellow.
   elif temperature < 75 :
      red = interpolate(temperature, 50, 75, 0, 255)
      green = interpolate(temperature, 50, 75, 255, 255)
      blue = interpolate(temperature, 50, 75, 0, 0)
   # Scale temperatures between 75 and 100 between yellow and red.
   else :
      red = interpolate(temperature, 75, 100, 255, 255)
      green = interpolate(temperature, 75, 100, 255, 0)
      blue = interpolate(temperature, 75, 100, 0, 0)

   # Combine the red, green and blue components into a single number.
   return 65536 * red + 256 * green + blue

## Interpolate a value into a new range.
#  @param x the value to work with
#  @param a the lower bound of the original range
#  @param b the upper bound of the original range
#  @param c the lower bound of the new range
#  @param d the upper bound of the new range
#  @return a value scaled between c and d based on x relative to a and b
#
def interpolate(x, a, b, c, d) :
   # If the upper and lower end of the destination range are the same then the
   # output value of the interpolation is that value.
   if c == d :
      return c

   # Map the value of x from the range (a, b) into the range (c, d).
   z = (x - a) / (b - a)
   y = c + z * (d - c)
   return y

# Call the main function.
main()

