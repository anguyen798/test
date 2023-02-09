##
#  Display the description of some radiation given its wavelength or frequency.
#

# Read unit from user.
unit = input("(W)avelength or (F)requency? ")

if unit == "W" :
   # Read input from the user.
   wavelength = float(input("Enter the wavelength: "))
   
   # Display the description of the radiation.
   if wavelength > 1e-1 :
      print("Radio Waves")
   elif wavelength > 1e-3 :
      print("Microwaves")
   elif wavelength > 7e-7 :
      print("Infrared")
   elif wavelength > 4e-7 :
      print("Visible Light")
   elif wavelength > 1e-8 :
      print("Ultraviolet")
   elif wavelength > 1e-11 :
      print("X-rays")
   else :
      print("Gamma rays")

else :
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

