##
# Write a program that reads in a stereo sound file and produces a mono
# file that contains (left-right)/2 for each sample.

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
   for i in range(len(data)):
      outputdata.append((data[i][0]-data[i][1])/2)
      
   # output the sound file
   outputname = inputname.replace(".wav", ".out.wav")
   scipy.io.wavfile.write(outputname, samplerate, 
      numpy.asarray(outputdata, dtype="int16"))

    
# Start the program.
main()

