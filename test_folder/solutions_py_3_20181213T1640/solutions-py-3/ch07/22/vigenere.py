##
#  Implement a Vigenere Cipher.
#

# Gather input from the user.
keyword = input("Enter the keyword: ").upper()
in_name = input("Enter the input file name: ")
out_name = input("Enter the output file name: ")
operation = input("(E)ncrypt or (D)ecrypt? ").upper()

# Read all of the text out of the file.
inf = open(in_name, "r")
text = inf.read()
inf.close()

# Encrypt or decrypt the string provided by the user.
result = ""
for i in range(0, len(text)) :
   # Handle uppercase letters.
   if text[i] >= "A" and text[i] <= "Z" :
      t_index = ord(text[i]) - ord("A")
      k_index = ord(keyword[i % len(keyword)]) - ord("A")

      if operation == "E" :
         result = result + chr(ord("A") + (t_index + k_index) % 26)
      elif operation == "D" :
         result = result + chr(ord("A") + (t_index - k_index) % 26)
   # Handle lowercase letters.
   elif text[i] >= "a" and text[i] <= "z" :
      t_index = ord(text[i]) - ord("a")
      k_index = ord(keyword[i % len(keyword)]) - ord("a")

      if operation == "E" :
         result = result + chr(ord("a") + (t_index + k_index) % 26)
      elif operation == "D" :
         result = result + chr(ord("a") + (t_index - k_index) % 26)
   # Handle anything that isn't a letter.
   else :
      result = result + text[i]

# Save the result.
outf = open(out_name, "w")
outf.write(result)
outf.close()

