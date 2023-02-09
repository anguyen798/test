##
# Using the Audacity program described in Toolbox 6.1, produce recordings of
# yourself saying one, two, three, …, nine, ten, eleven, twelve, teen, twenty, thirty, …,
# fifty. Then write a program that asks the user to supply a time such as 9:53, and that
# produces a file announcing that time. In this example, you would put together the
# sounds for nine, fifty, and three.

import numpy
import scipy.io.wavfile

def dialog(word):
   if word=="time":
      for i in range(len(dataTheTimeIs)):
         outputdata.append(dataTheTimeIs[i])
   elif word=="and":
      for i in range(len(dataAnd)):
         outputdata.append(dataAnd[i])
   elif word=="seconds":
      for i in range(len(dataSeconds)):
         outputdata.append(dataSeconds[i])
      
def number(num):
   if num==0:
      for i in range(len(data00)):
         outputdata.append(data00[i])
   elif num==1:
      for i in range(len(data01)):
         outputdata.append(data01[i])
   elif num==2:
      for i in range(len(data02)):
         outputdata.append(data02[i])
   elif num==3:
      for i in range(len(data03)):
         outputdata.append(data03[i])
   elif num==4:
      for i in range(len(data04)):
         outputdata.append(data04[i])
   elif num==5:
      for i in range(len(data05)):
         outputdata.append(data05[i])
   elif num==6:
      for i in range(len(data06)):
         outputdata.append(data06[i])
   elif num==7:
      for i in range(len(data07)):
         outputdata.append(data07[i])
   elif num==8:
      for i in range(len(data08)):
         outputdata.append(data08[i])
   elif num==9:
      for i in range(len(data09)):
         outputdata.append(data09[i])
   elif num==10:
      for i in range(len(data10)):
         outputdata.append(data10[i])
   elif num==11:
      for i in range(len(data11)):
         outputdata.append(data11[i])
   elif num==12:
      for i in range(len(data12)):
         outputdata.append(data12[i])
   elif num==13:
      for i in range(len(data13)):
         outputdata.append(data13[i])
   elif num==14:
      for i in range(len(data14)):
         outputdata.append(data14[i])
   elif num==15:
      for i in range(len(data15)):
         outputdata.append(data15[i])
   elif num==16:
      for i in range(len(data16)):
         outputdata.append(data16[i])
   elif num==17:
      for i in range(len(data17)):
         outputdata.append(data17[i])
   elif num==18:
      for i in range(len(data18)):
         outputdata.append(data18[i])
   elif num==19:
      for i in range(len(data19)):
         outputdata.append(data19[i])
   elif 20 <= num < 30:
      for i in range(len(data20)):
         outputdata.append(data20[i])
      number(num-20)
   elif 30 <= num < 40:
      for i in range(len(data30)):
         outputdata.append(data30[i])
      number(num-30)
   elif 40 <= num < 50:
      for i in range(len(data40)):
         outputdata.append(data40[i])
      number(num-40)
   elif 50 <= num < 60:
      for i in range(len(data50)):
         outputdata.append(data50[i])
      number(num-50)
   


def main():

   # read input
   timeString = input("Enter the time: ")
   timeList = timeString.split(":")
   if len(timeList) == 2:  # hours and minutes
      hours = int(timeList[0])
      minutes = int(timeList[1])
      seconds = -1
   elif len(timeList)==3:
      hours = int(timeList[0])
      minutes = int(timeList[1])
      seconds = int(timeList[2])
   else:
      print("Time format incorrectly entered.")

   # process the sound file
   # first part:  "The time is..."
   dialog("time")

   if 1 <= hours <= 12:
      number(hours)
   else:
      print("Inappropriate number of hours")

   if 0 <= minutes < 10:   # handle minutes less than 10, with an "oh"
      number(0)
   if 0 <= minutes < 60:
      number(minutes)
   else:
      print("Incorrect number of minutes")
   if seconds == -1:  # do nothing
      pass
   elif 0 <= seconds < 60:
      dialog("and")
      number(seconds)
      dialog("seconds")
   else:
      print("Incorrect number of seconds")
      
      
   # output the sound file
   outputname = "time.wav"
   scipy.io.wavfile.write(outputname, samplerate, 
      numpy.asarray(outputdata, dtype="int16"))

    
# Start the program.
contents = scipy.io.wavfile.read("numbers/00oh.wav")
samplerate = contents[0]
data00 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/01one.wav")
data01 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/02two.wav")
data02 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/03three.wav")
data03 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/04four.wav")
data04 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/05five.wav")
data05 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/06six.wav")
data06 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/07seven.wav")
data07 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/08eight.wav")
data08 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/09nine.wav")
data09 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/10ten.wav")
data10 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/11eleven.wav")
data11 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/12twelve.wav")
data12 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/13thirteen.wav")
data13 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/14fourteen.wav")
data14 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/15fifteen.wav")
data15 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/16sixteen.wav")
data16 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/17seventeen.wav")
data17 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/18eighteen.wav")
data18 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/19nineteen.wav")
data19 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/20twenty.wav")
data20 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/30thirty.wav")
data30 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/40forty.wav")
data40 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/50fifty.wav")
data50 = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/and.wav")
dataAnd = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/seconds.wav")
dataSeconds = contents[1].tolist() 
contents = scipy.io.wavfile.read("numbers/thetimeis.wav")
dataTheTimeIs = contents[1].tolist()
outputdata = []

main()

