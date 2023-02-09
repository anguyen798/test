##
#  Convert a number to Roman numerals.
#

def main() :
   # Read the number from the user.
   num = int(input("Enter an integer between 1 and 3999: "))

   # Convert the number to roman numerals.
   roman = romanDigit(num, "I", "V", "X")
   num = num // 10
   roman = romanDigit(num, "X", "L", "C") + roman
   num = num // 10
   roman = romanDigit(num, "C", "D", "M") + roman
   num = num // 10
   roman = romanDigit(num, "M", "", "") + roman

   # Display the result.
   print(roman)

## Convert one digit from an integer to a string of Roman numerals.
#  @param n the integer to convert
#  @param one the character to use to represent one
#  @param five the character to use to represent five
#  @param ten the character to use to represent ten
#  @return the right most digit of n as a roman numeral
#
def romanDigit(n, one, five, ten) :
   roman = ""
   num = n % 10
   if num == 9 :
      roman = roman + one + ten
      num = num - 9
   
   if num >= 5 :
      roman = roman + five
      num = num - 5
  
   if num >= 4 :
      roman = roman + one + five
      num = num - 4
   
   if num >= 1 :
      roman = roman + one
      num = num - 1
   if num >= 1 :
      roman = roman + one
      num = num - 1
   if num >= 1 :
      roman = roman + one
      num = num - 1

   return roman

# Call the main program.
main()

