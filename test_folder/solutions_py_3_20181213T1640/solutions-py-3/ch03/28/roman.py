##
#  Convert a number to Roman numerals.
#

# Read the number from the user.
num = int(input("Enter an integer between 1 and 3999: "))

# Convert it to Roman numerals.  Basic strategy: Start with an empty string
# and add the largest numeral to it that we legally can.  Then subtract the
# amount that was added.  Continue with the remaining smaller numerals.  Note
# that some amounts like 900, 400, 90, 40, 9 and 4 are actually add two
# numerals.

roman = ""

if num >= 1000 :
   roman = roman + "M"
   num = num - 1000
if num >= 1000 :
   roman = roman + "M"
   num = num - 1000
if num >= 1000 :
   roman = roman + "M"
   num = num - 1000

if num >= 900 :
   roman = roman + "CM"
   num = num - 900

if num >= 500 :
   roman = roman + "D"
   num = num - 500

if num >= 400 :
   roman = roman + "CD"
   num = num - 400

if num >= 100 :
   roman = roman + "C"
   num = num - 100
if num >= 100 :
   roman = roman + "C"
   num = num - 100
if num >= 100 :
   roman = roman + "C"
   num = num - 100

if num >= 90 :
   roman = roman + "XC"
   num = num - 90

if num >= 50 :
   roman = roman + "L"
   num = num - 50

if num >= 40 :
   roman = roman + "XL"
   num = num - 40

if num >= 10 :
   roman = roman + "X"
   num = num - 10
if num >= 10 :
   roman = roman + "X"
   num = num - 10
if num >= 10 :
   roman = roman + "X"
   num = num - 10

if num >= 9 :
   roman = roman + "IX"
   num = num - 9

if num >= 5 :
   roman = roman + "V"
   num = num - 5

if num >= 4 :
   roman = roman + "IV"
   num = num - 4

if num >= 1 :
   roman = roman + "I"
   num = num - 1
if num >= 1 :
   roman = roman + "I"
   num = num - 1
if num >= 1 :
   roman = roman + "I"
   num = num - 1

# Display the result.
print(roman)

