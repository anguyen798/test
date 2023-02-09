##
#  Print the postal bar code for a zip code.
#
def main() :
   printBarCode(input("Enter a zipcode: "))

## Convert a digit to its equivalent postal bar code.
#  @param d the digit to convert
#  @return the postal bar code for a single digit
#
def printDigit(d) :
   if d == 1 :
      s = ":::||"
   if d == 2 :
      s = "::|:|"
   if d == 3 :
      s = "::||:"
   if d == 4 :
      s = ":|::|"
   if d == 5 :
      s = ":|:|:"
   if d == 6 :
      s = ":||::"
   if d == 7 :
      s = "|:::|"
   if d == 8 :
      s = "|::|:"
   if d == 9 :
      s = "|:|::"
   if d == 0 :
      s = "||:::"
   print(s, end="")

## Print a postal bar code.
#  @param zipCode the zip code to display
#
def printBarCode(zipCode) :
   # Initialize total and print the frame bar.
   total = 0
   print("|", end="")

   # Display each digit in the zip code and add it to the total.
   for ch in str(zipCode) :
      num = int(ch)
      printDigit(num) 
      total = total + num

   # Compute the check digit and print it.
   checkDigit = (50 - total) % 10
   printDigit(checkDigit)

   # Print the closing frame bar.
   print("|", end="")

# Call the main function.
main()

