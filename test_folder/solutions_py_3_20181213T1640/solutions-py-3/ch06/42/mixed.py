##
# Write a program that reads two sound files and mixes them. Average
# the sound values.  Your program should work even if the inputs
# have different lengths.  You can assume that the inputs have the
# same sampling rate.

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
   scipy.io.wavfile.write(outputname, samplerate1, 
      numpy.asarray(outputdata, dtype="int16"))

    
# Start the program.
main()

