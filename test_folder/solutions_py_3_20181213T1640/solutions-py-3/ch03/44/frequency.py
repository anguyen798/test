##
#  Display the description of some radiation given its frequency.
#

# Read input from the user.
frequency = float(input("Enter the frequency: "))

# Display the description of the radiation.
if frequency < 3e9 :
   print("Radio Waves")
elif frequency < 3e11 :
   print("Microwaves")
elif frequency < 4e14 :
   print("Infrared")
elif frequency < 7.5e14 :
   print("Visible Light")
elif frequency < 3e16 :
   print("Ultraviolet")
elif frequency < 3e19 :
   print("X-rays")
else :
   print("Gamma rays")

