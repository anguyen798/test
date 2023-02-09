##
#  Display a description of a sound given in either dB or Pa.
#
from math import log10

# Read input from the user.
sound_level = float(input("Enter the sound value: "))
unit = input("dB or Pa? ")

# Get the sound level in dB.
if unit == "dB" :
   dB = sound_level
else :
   dB = 20 * log10(sound_level / 20e-6)

# Display the closest description from the table.
if dB < 15 :
   print("Light leaf rustling.")
elif dB < 45 :
   print("Calm library.")
elif dB < 75 :
   print("Normal conversation.")
elif dB < 95 :
   print("Traffic on a busy roadway at 10m.")
elif dB < 110 :
   print("Jack hammer at 1m.")
elif dB < 125 :
   print("Possible hearing damage.")
else :
   print("Threshold of pain.")

