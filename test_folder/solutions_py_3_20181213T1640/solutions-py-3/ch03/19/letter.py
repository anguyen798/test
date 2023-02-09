##
#  Determine if a single character is a vowel or consonant.
#

# Read input from the user.
ch = input("Enter one character: ")
ch = ch.upper()

# Check and report the status of the character.
if len(ch) == 0 or len(ch) > 1 :
   print("That input didn't have a valid length.")
elif ch in "AEIOU" :
   print("Vowel")
elif ch >= "A" and ch <= "Z" :
   print("Consonant")
else :
   print("That was neither a vowel nor a consonant.")

