##
#  Count and display the number of vowels in a word.
#

# Read input from the user.
inputStr = input("Enter a word: ")

# Check each character in the string to see if it is a vowel.
vowelCount = 0
for ch in inputStr :
   if ch in "aeiouyAEIOUY" :
      vowelCount = vowelCount + 1

# Display the result.
print("The number of vowels is", vowelCount)

