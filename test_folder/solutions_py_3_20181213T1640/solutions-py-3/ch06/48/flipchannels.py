##
# Write a program that reads in a stereo sound file and flips the left
# and right channels.

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
      outputdata.append([data[i][1],data[i][0]])
      
   # output the sound file
   outputname = inputname.replace(".wav", ".out.wav")
   scipy.io.wavfile.write(outputname, samplerate, 
      numpy.asarray(outputdata, dtype="int16"))

    
# Start the program.
main()

