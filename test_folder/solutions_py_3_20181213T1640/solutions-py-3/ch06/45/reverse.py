##
# Write a program that reads a sound file, reverses all values, and saves the result. Try it
# out with the recording of speech or a song.

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
   for i in range(len(data)-1,-1,-1):
      outputdata.append(data[i])
      
   # output the sound file
   outputname = inputname.replace(".wav", ".out.wav")
   scipy.io.wavfile.write(outputname, samplerate, 
      numpy.asarray(outputdata, dtype="int16"))

    
# Start the program.
main()

