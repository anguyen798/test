##
# Repeat Exercise P6.40, but also fade out the sound at the end.

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
   for i in range(samplerate,len(data)-samplerate):
      outputdata.append(data[i])
   for i in range(len(data)-samplerate,len(data)):
      outputdata.append(data[i]*(len(data)-i)/samplerate)
      
   # output the sound file
   outputname = inputname.replace(".wav", ".out.wav")
   scipy.io.wavfile.write(outputname, samplerate, 
      numpy.asarray(outputdata, dtype="int16"))

    
# Start the program.
main()

