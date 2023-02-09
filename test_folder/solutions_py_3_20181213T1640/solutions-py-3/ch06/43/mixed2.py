##
# Make the program of Exercise P6.42 work if the inputs have different
# sampling rates.  Use the higher of the two rates for the output.

import numpy
import scipy.io.wavfile

def main() :
   # read in sound file and convert
   input1name = input("Input file #1: ")
   contents1 = scipy.io.wavfile.read(input1name)
   samplerate1 = contents1[0]
   data1 = contents1[1].tolist() # Now it's a Python list
   input2name = input("Input file #2: ")
   contents2 = scipy.io.wavfile.read(input2name)
   samplerate2 = contents2[0]
   data2 = contents2[1].tolist() # Now it's a Python list
   outputdata = []
   samplerate = max(samplerate1,samplerate2)
   
   # process the sound file
   shortest = min(len(data1),len(data2))
   longest  = max(len(data1),len(data2))
   for i in range(shortest):
      outputdata.append(data1[i]/2 + data2[i]/2)
   for i in range(shortest,longest):
      if len(data1)>len(data2):
         outputdata.append(data1[i])
      else:
         outputdata.append(data2[i])
      
   # output the sound file
   outputname = "mixed.wav"
   scipy.io.wavfile.write(outputname, samplerate, 
      numpy.asarray(outputdata, dtype="int16"))

    
# Start the program.
main()

