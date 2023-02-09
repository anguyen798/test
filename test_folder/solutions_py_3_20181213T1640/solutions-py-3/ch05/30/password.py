##
#  Check whether a password has the required properties.
#

def main() :
   # Read input from the user.
   password1 = input("Enter your password: ")
   password2 = input("Re-enter your password: ")

   # Keep looping until the passwords match and have the desired properties.
   while password1 != password2 or not isValidPassword(password1) :
      print("That password didn't have the required properties.")

      # Read the next pair of passwords.
      password1 = input("Enter your password: ")
      password2 = input("Re-enter your password: ")

   # Display the final message.
   print("That pair of passwords will work.")

## Determine if a password has the desired properties: 8 characters long, at
#  least one uppercase letter, at least one lowercase letter and at least one
#  digit.
#  @param password the password to check
#  @return True if all properties are present, False otherwise
#
def isValidPassword(password) :
   if len(password) < 8 :
      return False

   # Assume that the password doesn't have the apporpriate characters until
   # we can demonstrate otherwise.
   hasDigit = False
   hasUpper = False
   hasLower = False

   # Check each character and record which type of character it is.
   for ch in password :
      if ch >= "A" and ch <= "Z" :
         hasUpper = True
      if ch >= "a" and ch <= "z" :
         hasLower = True
      if ch >= "0" and ch <= "9" :
         hasDigit = True

   # The password is only valid if all three types of characters are present.
   return hasUpper and hasLower and hasDigit

# Call the main function.
main()

