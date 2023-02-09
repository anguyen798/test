##
# Write a program that reads a sound file and “fades in” the sound.
# Multiply the values of the first second with a factor that increases
# from 0 to 1.

import numpy
import scipy.io.wavfile

def main() :
   # read in sound file and convert
   inputname = input("Input file: ")
   contents = scipy.io.wavfile.read(inputname)
   samplerate = contents[0]
   data = contents[1].tolist() # Now it's a Python list
   outputdata = []
   
   # process the sound file
   for i in range(samplerate):
      outputdata.append(data[i]*i/samplerate)
   for i in range(samplerate,len(data)):
      outputdata.append(data[i])
      
   # output the sound file
   outputname = inputname.replace(".wav", ".out.wav")
   scipy.io.wavfile.write(outputname, samplerate, 
      numpy.asarray(outputdata, dtype="int16"))

    
# Start the program.
main()

