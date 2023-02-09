##
#  Convert a postal bar code to its numeric zip code.
#
def main() :
   print(convertBarCode(input("Enter barcode: ")))
   #print(convertBarCode("||:|:::|:|:||::::::||:|::|:::|||"))
   #print(convertBarCode("|:::||::|:|::||::|::|:|:|::|:|:|"))
   #print(convertBarCode("|:||::|:::||::|:|:|::||:::||:::|"))

## Convert a string of 5 characters to the equivalent digit.
#  @param s the string to convert
#  @return the digit for the bar code, or -1 if the characters are not valid
#
def convertDigit(s) :
   if s == ":::||" :
      return 1
   if s == "::|:|" :
      return 2
   if s == "::||:" :
      return 3
   if s == ":|::|" :
      return 4
   if s == ":|:|:" :
      return 5
   if s == ":||::" :
      return 6
   if s == "|:::|" :
      return 7
   if s == "|::|:" :
      return 8
   if s == "|:|::" :
      return 9
   if s == "||:::" :
      return 0

   # Indicate an error by returing -1.
   return -1

## Convert a postal bar code to a numeric zip code.
#  @param barCode the bar code to convert
#  @return the numeric zip code, or -1 if the bar code is not valid
#
def convertBarCode(barCode) :
   # Verify the length and frame bars.
   if len(barCode) != 32 or barCode[0] != "|" or barCode[31] != "|" :
      return -1

   # Compute the total of the digits so that we can verify that the check
   # digit is correct.
   total = 0

   # Convert each of the 5 digits, forming the zip code.
   zipCode = 0
   for i in range(1, 22, 5) :
      zipCode = zipCode * 10
      digit = convertDigit(barCode[i : i + 5])
      if digit == -1 :
         return -1
      total = total + digit
      zipCode = zipCode + digit

   # Conver the check digit and verify that it is correct.
   checkDigit = convertDigit(barCode[26 : 31])
   if (total + checkDigit) % 10 != 0 :
      return -1

   # Return the numeric zip code.
   return zipCode

# Call the main function.
main()

