##
# Write a program that reads a sound file and introduces an echo.  For
# each data value, add 80 percent of the value from 0.2 seconds ago.
# When you are done, rescale the result so no value is larger than 32,787.

import numpy
import scipy.io.wavfile

def main() :
   # read in sound file and convert
   inputname = input("Input file #1: ")
   contents = scipy.io.wavfile.read(inputname)
   samplerate = contents[0]
   data = contents[1].tolist() # Now it's a Python list

   echolength = 0.5  # seconds
   echosamplelength = int(samplerate * echolength)
   outputdata = []
   
   # process the sound file
   for i in range(echosamplelength):
      outputdata.append(data[i])
   for i in range(echosamplelength,len(data)):
      outputdata.append(data[i]-0.8*data[i-echosamplelength])
      
   # output the sound file
   outputname = "echo.wav"
   scipy.io.wavfile.write(outputname, samplerate, 
      numpy.asarray(outputdata, dtype="int16"))

    
# Start the program.
main()

