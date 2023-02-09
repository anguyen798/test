##
# Write a sound file that contains 44,100 data points alternating
# between 30,000 and -30,000 at a sampling rate of 44,100.  What sound do
# you get?  Repeat with 15,000 and -15,000.  What is the difference.  What
# happens when you double the sampling rate?  Cut it in half?

import numpy
import scipy.io.wavfile

def main() :

   outputdata = []
   outputname = "out.wav"
   samplerate = 44100
   value = 30000
   repeat = 10
   for f in range(int(44100 / repeat)) :
      for g in range(repeat) :
         outputdata.append(-value)
      for g in range(repeat) :
         outputdata.append(value)
   scipy.io.wavfile.write(outputname, samplerate, 
      numpy.asarray(outputdata, dtype="int16"))
    
# Start the program.
main()

